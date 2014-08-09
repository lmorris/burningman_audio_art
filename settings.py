__author__ = 'bm'

import pyaudio

RECORD_FILE = "recording.wav"
RECORD_DIR = "recordings"
LEFT_PLAY = "play_left.wav"
RIGHT_PLAY = "play_right.wav"
MIDDLE_PLAY = "play_middle.wav"
RECORD_SECONDS = 8
INSTRUCT = "instruct.wav"

TRACK_BLOCK = 10
DB_RANGE = range(-20, -30)
DB_LEN = len(DB_RANGE)

MAX_PROCESSED = 500
PLAY_BOTH = "play_both.wav"
BOTH_DIR = "both"
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
MAX_PLAY = 5

CROSS_FADE = 5000