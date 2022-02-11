"""
module for sound service
"""
import pyray
import threading
import time


class SoundService:
    """ Plays sounds when appropriate.

    The responsibility of the SoundService is to play sounds when dictated by the program.
    """

    def __init__(self, root_dir):
        """ Constructs a new SoundService. """
        self._root_dir = root_dir
        self._sound = ""
        pyray.init_audio_device()

    def load_sound(self, sound):
        """Loads a sound from the sounds directory"""
        return pyray.load_sound(f"{self._root_dir}\\sounds\\{sound}")

    def thread_call(self, sound, volume=1):
        """ Construct the thread to be called later.
        
        Args:
            sound (string): The name of the sound file to be played.
        
        """
        self._sound = self.load_sound(sound)
        pyray.set_sound_volume(self._sound, volume)
        #pyray.play_sound_multi(self._sound, volume)
        if not pyray.is_sound_playing(self._sound):
            pyray.play_sound(self._sound)
        else:
            pyray.stop_sound_multi()
            pyray.unload_sound(self._sound)


    def play_sound(self, sound, volume=1, interval=0):
        """ Play a sound from the sounds directory.
        Args:
            sound (string): The name of the sound file to be played.
        
        """
        t = threading.Thread(target=self.thread_call, args=(sound, volume), daemon=True)
        t.start()

