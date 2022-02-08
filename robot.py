# This script initializes the robot kinematics

import math

snake_segment_lengths = [1000, 1000, 1000, 1000]
joint_dict = {0: [0, 130],
              1: [0, 200],
              2: [0, 200],
              3: [0, 200],
              4: [0, 120],
              }

# Instantiate a list of join lengths in mm
class robot_arm():
    def __init__(self,
                 segment_lengths,
                 joint_dict,
                 ):
        self.segment_lengths = segment_lengths
        self.joint_dict = joint_dict
    def inverse_kinematics(self):
        return
    def forward_kinematics(self):
        return

robo_snek = robot_arm(snake_segment_lengths, joint_dict)
