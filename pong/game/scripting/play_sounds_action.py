""" Module for playing sounds """

from game.scripting.action import Action
from game.scripting.handle_collisions_action import HandleCollisionsAction

class PlaySoundsAction(Action):

    def __init__(self, sound_service):
        """ Constructs a new PlaySound.
        
        Args:
            sound_service (SoundService): An instance of SoundService.
        
        """
        self._sound_service = sound_service
        self._edges_collision = False
        self._paddles_collision = False
        self._lost_round = False
        self._collisions = HandleCollisionsAction()

    
    def execute(self, cast, script):
        """ Executes the play sounds action. 
        
        Args:
            cast (Cast): The cast of actors in the game.
            script (Script): The script of actions in the game.
        
        """
        self._collisions.execute(cast, script)
        
        self._edges_collision = self._collisions.get_edges_collision()
        self._lost_round = self._collisions.get_lost_round()
        self._paddles_collision = self._collisions.get_paddle_collided()

        if self._edges_collision:
            self._edges_collided_sound()
        if self._paddles_collision:
            self._paddle_collided_sound()
        if self._lost_round: 
            self._lost_sound()

        

    def _edges_collided_sound(self):
        """ The sound to play when the ball has collided with the top or bottom of the screen. """
        self._sound_service.play_sound("edges.wav", volume=0.5)

    def _paddle_collided_sound(self):
        """ The sound to play when the ball has collided with one of the paddles. """
        self._sound_service.play_sound("paddles.wav", volume=0.5)

    def _lost_sound(self):
        """ The sound to play when the ball has collided with the left or right of the screen. """
        self._sound_service.play_sound("lost.wav", volume=0.5)
    
       

