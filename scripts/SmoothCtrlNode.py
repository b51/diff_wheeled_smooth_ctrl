#!/usr/bin/env python

import rospy
import diff_wheeled_smooth_ctrl

if __name__ == '__main__':
    rospy.init_node('smooth_ctrl');
    SmoothCtrlNode = diff_wheeled_smooth_ctrl.SmoothCtrl();
    SmoothCtrlNode.spin();
