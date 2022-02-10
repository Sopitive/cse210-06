"""
A module that contains the Paddle class
"""
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Paddle(Actor):
    """
    A paddle that only moves up and down to hit a ball.
    
    The responsibility the paddle is to move itself up and down.

    Attributes:
        _points (int): The number of points.
    """
    def __init__(self, starting_point, color):
        """ 
        """
        super().__init__()
        self.set_color(color)
        self._segments = []
        self._prepare_body(starting_point)

    def get_segments(self):
        """ 
        """
        return self._segments

    def move_next(self):
        """ 
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    # def get_head(self):
    #     """ 
    #     """
    #     return self._segments[0]

    # def grow_tail(self, number_of_segments):
    #     """ 
    #     """
    #     for i in range(number_of_segments):
    #         tail = self._segments[-1]
    #         velocity = tail.get_velocity()
    #         offset = velocity.reverse()
    #         position = tail.get_position().add(offset)
            
    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text("#")
    #         segment.set_color(self.get_color())
    #         self._segments.append(segment)

    # def turn_head(self, velocity):
    #     """ 
    #     """
    #     self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, starting_point):
        """ 
        """
        # x = int(constants.MAX_X / 2)
        # y = int(constants.MAX_Y / 2)
        x = starting_point.get_x()
        y = starting_point.get_y()

        for i in range(constants.paddle_LENGTH):
            position = Point(x, y - i * constants.CELL_SIZE)
            velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            color = self.get_color()
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)