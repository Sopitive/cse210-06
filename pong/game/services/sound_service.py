"""
module for sound service
"""
import os
import pyray


class SoundService:
    """ Plays sounds when appropriate.

    The responsibility of the SoundService is to play sounds when dictated by the program.
    """

    def __init__(self, root_dir):
        """ Constructs a new SoundService. """
        self._root_dir = root_dir
        pyray.init_audio_device()
        self.sounds = {}

    def add_sound(self, name, path):
        """ loads a sound into memory and assigns it a name
        Args:
            name (string): the assigned name for the sound
            path (string): the path to the sound file within the sounds directory
        """
        self.sounds[name] = pyray.load_sound(os.path.join(self._root_dir, "sounds", path))

    def load_sound(self, sound):
        """Loads a sound from the sounds directory"""
        return pyray.load_sound(f"{self._root_dir}\\sounds\\{sound}")

    def play_sound(self, sound, volume=1, interval=0):
        """ Play a sound from the sounds directory.
        Args:
            sound (string): The name of the sound file to be played.

        """
        pyray.set_sound_volume(self.sounds[sound], volume)
        pyray.play_sound(self.sounds[sound])


