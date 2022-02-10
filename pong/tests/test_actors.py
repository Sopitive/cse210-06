"""
A module for testing methods within the Actor Class.
"""
import random
from game.shared.point import Point
from game.casting.actor import Actor
from game.shared.color import Color

def test_color():
    """
    Tests to see if the color given is the color returned
    """
    actor = Actor()
    ref_color = Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    actor.set_color(ref_color)
    ret_color = actor.get_color()
    assert ref_color.to_tuple() == ret_color.to_tuple()

def test_font_size():
    """
    Tests to see if the font size given is the font size returned
    """
    actor = Actor()
    ref_font = 16
    actor.set_font_size(ref_font)
    ret_font = actor.get_font_size()
    assert ref_font == ret_font

def test_text():
    """
    Tests to see if the text given is the text returned
    """
    actor = Actor()
    ref_text = "hello"
    actor.set_text(ref_text)
    ret_text = actor.get_text()
    assert ref_text == ret_text

def test_position():
    """
    Tests to see if the position given is the position returned
    """
    actor = Actor()
    ref_position = Point(0,0)
    actor.set_position(ref_position)
    ret_position = actor.get_position()
    assert ref_position.get_x() == ret_position.get_x()
    assert ref_position.get_y() == ret_position.get_y()

def test_velocity():
    """
    Tests to see if the velocity given is the velocity returned
    """
    actor = Actor()
    ref_velocity = Point(0,0)
    actor.set_velocity(ref_velocity)
    ret_velocity = actor.get_velocity()
    assert ref_velocity.get_x() == ret_velocity.get_x()
    assert ref_velocity.get_y() == ret_velocity.get_y()


