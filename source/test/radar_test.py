# child_module.py
import sys
import os

# Add the parent folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the parent_module
from radar import is_within_radar


import unittest
import harfang as hg

class TestRadarLogic(unittest.TestCase):

    def test_range(self):
        a_loc = hg.Vec3(100,100,100)
        radar_loc = hg.Vec3(0,0,0)
        radar_rot = hg.Vec3(45,45,45)
        radar_range = 100
        field_of_view = 360
        self.assertEqual(is_within_radar(a_loc,radar_loc,radar_rot,radar_range,field_of_view), False)

    def test_angle(self):
         a_loc = hg.Vec3(100,100,100)
         radar_loc = hg.Vec3(0,0,0)
         radar_rot = hg.Vec3(0,0,0)
         radar_range = 200
         field_of_view1 = 44
         field_of_view2 =  45

         self.assertEqual(is_within_radar(a_loc,radar_loc,radar_rot,radar_range,field_of_view1), False)
         self.assertEqual(is_within_radar(a_loc,radar_loc,radar_rot,radar_range,field_of_view2), True)

    def test_angle_big(self):
         a_loc = hg.Vec3(100,100,100)
         radar_loc = hg.Vec3(0,0,0)
         radar_rot = hg.Vec3(-2,20,0)
         radar_range = 200
         field_of_view1 = 0
         field_of_view2 = 50

         self.assertEqual(is_within_radar(a_loc,radar_loc,radar_rot,radar_range,field_of_view1), False)
         self.assertEqual(is_within_radar(a_loc,radar_loc,radar_rot,radar_range,field_of_view2), True)


if __name__ == '__main__':
        unittest.main()