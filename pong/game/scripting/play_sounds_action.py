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
        self._is_game_over = False
        self._collisions = HandleCollisionsAction()
        self._won_played = False

    
    def execute(self, cast, script):
        """ Executes the play sounds action. 
        
        Args:
            cast (Cast): The cast of actors in the game.
            script (Script): The script of actions in the game.
        
        """
        self._collisions.execute(cast, script)
        self._is_game_over = self._collisions.get_game_over()
        if self._is_game_over and not self._won_played:
            self._game_over()
            self._won_played = True
        elif not self._is_game_over:
            self._ambient_sound()

        

    def _game_over(self):
        """ Sound to play when the game has ended. """
        self._sound_service.play_sound("won.wav")

    def _ambient_sound(self):
        """ The sound to play when the game has not ended. """
        self._sound_service.play_sound("tap.wav")
    
       

