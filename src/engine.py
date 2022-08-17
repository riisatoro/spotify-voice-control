from importlib.resources import is_resource
from os import getenv

from spotipy import Spotify, SpotifyOAuth
from speech_recognition import Microphone, Recognizer


class SpotifyEngine:
    def __init__(self):
        scope = getenv('SCOPE')
        self.spotify = Spotify(oauth_manager=SpotifyOAuth(scope=scope))
    
        self.recognizer = Recognizer()
        self.microphone = Microphone()

        self.is_running = True

    def start(self):
        while self.is_running:
            with self.microphone as microphone:
                self.recognizer.adjust_for_ambient_noise(microphone)
                voice_line = self.recognizer.listen(microphone)
                raw_text = self.recognizer.recognize_google(voice_line)
                print(raw_text)

