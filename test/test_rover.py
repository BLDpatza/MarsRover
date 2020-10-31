from nose.tools import assert_equal

from src.rover import Rover


class TestRover:
    def rover_initialises_with_coordinates_and_orientation(self):
        r = Rover(4, 3, "N")
        assert_equal(3, r.x)
        assert_equal(3, r.y)
        assert_equal("N", r.direction)