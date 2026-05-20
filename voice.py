"""Voice I/O module for JARVIS - Speech to Text and Text to Speech"""

import io
import tempfile
import threading
from pathlib import Path

from gtts import gTTS
from mutagen.mp3 import MP3


class VoiceOutput:
    """Text-to-speech using gTTS"""

    def __init__(self, lang: str = "en", slow: bool = False):
        self.lang = lang
        self.slow = slow

    def speak(self, text: str) -> str:
        """Convert text to speech and return the audio file path"""
        tts = gTTS(text=text, lang=self.lang, slow=self.slow)
        
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            tts.save(f.name)
            return f.name

    def speak_and_play(self, text: str) -> None:
        """Convert text to speech and play it"""
        import subprocess
        import platform
        
        audio_file = self.speak(text)
        
        try:
            if platform.system() == "Darwin":
                subprocess.run(["afplay", audio_file])
            elif platform.system() == "Linux":
                subprocess.run(["aplay", audio_file])
            else:
                subprocess.run(["powershell", "-c", f"(New-Object Media.SoundPlayer '{audio_file}').PlaySync()"])
        finally:
            Path(audio_file).unlink(missing_ok=True)


class VoiceInput:
    """Speech-to-text using SpeechRecognition library
    
    Note: Requires internet for Google Speech Recognition API.
    For offline mode, consider using whisper or faster-whisper.
    """

    def __init__(self, timeout: int = 5, phrase_time_limit: int = 10):
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit

    def listen(self) -> str | None:
        """Listen for voice input and return transcribed text"""
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)
        
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None

    def listen_in_background(self, callback: callable, phrase_time_limit: int = 5) -> None:
        """Start listening in background thread"""
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def audio_callback(recognizer, audio):
            try:
                text = recognizer.recognize_google(audio)
                callback(text)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")
        
        stop_listening = recognizer.listen_in_background(microphone, audio_callback, phrase_time_limit=phrase_time_limit)
        return stop_listening