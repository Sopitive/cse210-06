"""
module for sound service
"""
from playsound import playsound
import threading


class SoundService:
    """ Plays sounds when appropriate.

    The responsibility of the SoundService is to play sounds when dictated by the program.
    """

    def __init__(self, root_dir):
        """ Constructs a new SoundService. """
        self._root_dir = root_dir


    def play_sound(self, sound):
        """ Play a sound from the sounds directory. 
        
        Args:
            sound (string): The name of the sound file to be played.
        
        """
        threading.Thread(target=playsound, args=(f"{self._root_dir}\\sounds\{sound}",), daemon=True).start()
        # t = multiprocessing.Pool(processes=3)
        # result = t.apply_async(func=winsound.PlaySound, args=(f"{self._root_dir}\sounds\{sound}", winsound.SND_ASYNC))
        # t.close()
        # t.join()
        # print(f"{self._root_dir}\sounds\{sound}")

