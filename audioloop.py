__author__ = 'studleemon'

import multiprocessing
import pydub


class Recorder(object):

    filename = ""

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
