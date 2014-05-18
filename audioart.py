#!/usr/bin/env python
__author__ = 'studleemon'

import os
import os.path as path
import glob

import pyaudio
import pygame
from pygame.locals import KEYUP, KEYDOWN, K_RETURN, K_KP_ENTER, NOEVENT
import wave
import time
import datetime
import settings
import artmixer
pygame.init()
screen = pygame.display.set_mode([600,400])
pygame.event.pump()

class AudioArt(object):

    def __init__(self):
        if not path.exists(settings.BOTH_DIR):
            os.mkdir(settings.BOTH_DIR)
        if not path.exists(settings.RECORD_DIR):
            os.mkdir(settings.RECORD_DIR)

    def timestamp(self):
        dt = datetime.datetime.fromtimestamp(time.time())
        return dt.strftime("%y%m%d%H%M%S")

    def button_down(self):
        # raw_input("Button down")
        return False

    def play_instruction(self):
        self.play(settings.INSTRUCT)

    def record_instruction(self):
        self.record(settings.INSTRUCT)

    def play(self, filename):
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data = wf.readframes(settings.CHUNK)
        while data != '':
            stream.write(data)
            data = wf.readframes(settings.CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

    def start_play(self):
        wf = wave.open(settings.PLAY_BOTH, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        return p, wf, stream

    def stop_play(self, p, wf, stream):
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()
        
    def record(self, filename):
        p = pyaudio.PyAudio()
        stream = p.open(format=settings.FORMAT,
                        channels=settings.CHANNELS,
                        rate=settings.RATE,
                        input=True,
                        frames_per_buffer=settings.CHUNK)
        print("* recording: %s" % filename)
        frames = []
        for i in range(0, int(settings.RATE / settings.CHUNK * settings.RECORD_SECONDS)):
            data = stream.read(settings.CHUNK)
            frames.append(data)
        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(filename, 'wb')
        wf.setnchannels(settings.CHANNELS)
        wf.setsampwidth(p.get_sample_size(settings.FORMAT))
        wf.setframerate(settings.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def record_with_event(self, filename):
        p = pyaudio.PyAudio()
        stream = p.open(format=settings.FORMAT,
                        channels=settings.CHANNELS,
                        rate=settings.RATE,
                        input=True,
                        frames_per_buffer=settings.CHUNK)
        print("* recording: %s" % filename)
        frames = []
        while True:
            event = pygame.event.poll()
            # if event.type != NOEVENT:
            #     print event
            if event.type == KEYDOWN:
                break
            data = stream.read(settings.CHUNK)
            frames.append(data)

        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(filename, 'wb')
        wf.setnchannels(settings.CHANNELS)
        wf.setsampwidth(p.get_sample_size(settings.FORMAT))
        wf.setframerate(settings.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def print_info(self):
        p = pyaudio.PyAudio()
        print "Default Host API: %s" % p.get_default_host_api_info()
        print "Default Input Device: %s" % p.get_default_input_device_info()
        print "Default Output Device: %s" % p.get_default_output_device_info()
        p.terminate()

    def gen_play(self):
        print "Mixing audio"
        mix = artmixer.ArtMixer()
        mix.gen_left()
        mix.gen_right()
        mix.gen_both()

    def run(self):
        self.print_info()
        self.gen_play()
        mix = artmixer.ArtMixer()

        while True:
            p, wf, stream = self.start_play()
            data = wf.readframes(settings.CHUNK)
            while data != '':
                stream.write(data)
                data = wf.readframes(settings.CHUNK)
                event = pygame.event.poll()
                # if event.type != NOEVENT:
                #     print event

                if event.type == KEYDOWN:
                    self.stop_play(p, wf, stream)
                    # Play instructions
                    # self.play_instruction()
                    # Stop audio
                    self.record_with_event(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))

                    mix.gen_left()
                    mix.gen_right()
                    mix.gen_both()
                    p, wf, stream = self.start_play()
                    data = wf.readframes(settings.CHUNK)
            self.stop_play(p, wf, stream)
if __name__ == "__main__":
    art = AudioArt()
    art.run()

    # raw_input("Hit enter to record intro")
    # art.record_instruction()
    # raw_input("Hit enter to play intro")
    # art.play_instruction()
    # count = 1
    # raw_input("Record file %s" % count)
    # art.record(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))
    # count += 1
    # raw_input("Record file %s" % count)
    # art.record(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))
    # count += 1
    # raw_input("Record file %s" % count)
    # art.record(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))
    # count += 1
    # raw_input("Record file %s" % count)
    # art.record(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))
    # count += 1
    # raw_input("Record file %s" % count)
    # art.record(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))
    # count += 1
    # raw_input("Record file %s" % count)
    # art.record(path.join(settings.RECORD_DIR, art.timestamp()+settings.RECORD_FILE))
    # count += 1
    # raw_input("Push button")
    # mix = artmixer.ArtMixer()
    # mix.gen_left()
    # mix.gen_right()
    # mix.gen_both()
    #
    # art.play("both/*play_both.wav")
