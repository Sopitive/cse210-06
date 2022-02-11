"""
module for sound service
"""
import pyray
import threading


class SoundService:
    """ Plays sounds when appropriate.

    The responsibility of the SoundService is to play sounds when dictated by the program.
    """

    def __init__(self, root_dir):
        """ Constructs a new SoundService. """
        self._root_dir = root_dir
        self._load_sound = ""

    def load_sound(self, sound):
        return pyray.load_sound(f"{self._root_dir}\\{sound}")

    def play_sound(self, sound):
        """ Play a sound from the sounds directory. 
        
        Args:
            sound (string): The name of the sound file to be played.
        
        """
        sound = load_sound(sound)
        threading.Thread(target=pyray.play_sound, args=(f"{self._root_dir}\\sounds\{sound}",), daemon=True).start()

