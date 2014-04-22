__author__ = 'studleemon'

import multiprocessing
import pydub
import pyaudio
import pygame
import wave
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
INSTRUCT = "instruct.wav"

class Recorder(object):

    filename = ""

    def __init__(self):
        self.player = pyaudio.PyAudio()

    def button_down(self):
        return True

    def button_up(self):
        return True

    def run(self):

        down = False
        while(True):

            if self.button_down() and not down:
                down = True
                # Play instructions
                # Stop audio
                # Start recording

            if self.button_up() and down:
                down = False
                # Stop recording
                # Mix audio
                # Start playing channels

            time.sleep(0.1)


class Player(object):

    def run(self):
        pass

class Mixer(object):

    def append(self, track1, track2):
        pass


class Runner(object):
    pass


if __name__ == "main":
    pass
