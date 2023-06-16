import unittest
import src.shapes as sh
import src.misc.something


class TestRectangle(unittest.TestCase):

    def test_area(self):
        """Test that rectangle_area() returns the correct area."""
        self.assertEqual(sh.rectangle_area(2, 3), 6)

    def test_volume(self):
        """Test that rectangle_volume() returns the correct volume."""
        self.assertEqual(sh.rectangle_volume(2, 3, 4), 24)

    def test_area_error(self):
        """Test that rectangle_area() returns an error if there are too many parameters."""
        self.assertRaises(TypeError, sh.rectangle_area, 2, 3, 4)

    def test_volume_error(self):
        """Test that rectangle_volume() returns an error if there are too few parameters."""
        self.assertRaises(TypeError, sh.rectangle_volume, 2, 3)
