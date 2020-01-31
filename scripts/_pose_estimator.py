# -*- coding: utf-8 -*-
"""
Created on Jul 13 16:20 2017

@author: Denis Tome'
"""
from . import utils
import cv2
import numpy as np
import tensorflow as tf

import abc
ABC = abc.ABCMeta('ABC', (object,), {})

__all__ = [
    'PoseEstimatorInterface',
    'PoseEstimator'
]


class PoseEstimatorInterface(ABC):

    @abc.abstractmethod
    def initialise(self):
        pass

    @abc.abstractmethod
    def estimate3Dfrom2D(self, estimated_2d_pose, visibility):
        return

    @abc.abstractmethod
    def close(self):
        pass


class PoseEstimator(PoseEstimatorInterface):

    def __init__(self, image_size, session_path, prob_model_path):
        """Initialising the graph in tensorflow.
        INPUT:
            image_size: Size of the image in the format (w x h x 3)"""

        self.session = None
        self.poseLifting = utils.Prob3dPose(prob_model_path)
        self.sess = -1
        self.orig_img_size = np.array(image_size)
        self.scale = utils.config.INPUT_SIZE / (self.orig_img_size[0] * 1.0)
        self.img_size = np.round(
            self.orig_img_size * self.scale).astype(np.int32)
        self.image_in = None
        self.heatmap_person_large = None
        self.pose_image_in = None
        self.pose_centermap_in = None
        self.pred_2d_pose = None
        self.likelihoods = None
        self.session_path = session_path

    def initialise(self):
        """Load saved model in the graph
        INPUT:
            sess_path: path to the dir containing the tensorflow saved session
        OUTPUT:
            sess: tensorflow session"""

        tf.reset_default_graph()
        with tf.variable_scope('CPM'):
            # placeholders for person network
            self.image_in = tf.placeholder(
                tf.float32, [1, utils.config.INPUT_SIZE, self.img_size[1], 3])

            heatmap_person = utils.inference_person(self.image_in)

            self.heatmap_person_large = tf.image.resize_images(
                heatmap_person, [utils.config.INPUT_SIZE, self.img_size[1]])

            # placeholders for pose network
            self.pose_image_in = tf.placeholder(
                tf.float32,
                [utils.config.BATCH_SIZE, utils.config.INPUT_SIZE, utils.config.INPUT_SIZE, 3])

            self.pose_centermap_in = tf.placeholder(
                tf.float32,
                [utils.config.BATCH_SIZE, utils.config.INPUT_SIZE, utils.config.INPUT_SIZE, 1])

            self.pred_2d_pose, self.likelihoods = utils.inference_pose(
                self.pose_image_in, self.pose_centermap_in,
                utils.config.INPUT_SIZE)

        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess, self.session_path)

        self.session = sess

    def estimate3Dfrom2D(self, estimated_2d_pose, visibility):
        """
        Estimate 2d and 3d poses on the image.
        INPUT:
            image: RGB image in the format (w x h x 3)
            sess: tensorflow session
        OUTPUT:
            pose_2d: 2D pose for each of the people in the image in the format
            (num_ppl x num_joints x 2) visibility: vector containing a bool
            value for each joint representing the visibility of the joint in
            the image (could be due to occlusions or the joint is not in the
            image) pose_3d: 3D pose for each of the people in the image in the
            format (num_ppl x 3 x num_joints)
        """
        sess = self.session

        ## koko wo tsukaeba ii
        transformed_pose2d, weights = self.poseLifting.transform_joints(
            estimated_2d_pose.copy(), visibility)

        pose_3d = self.poseLifting.compute_3d(transformed_pose2d, weights)

        return visibility, pose_3d

    def close(self):
        self.session.close()
