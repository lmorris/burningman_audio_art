__author__ = 'bm'

import os
import os.path as path
import glob
import datetime
import time
import settings
from pydub import AudioSegment
from subprocess import Popen, call
import random

class ArtMixer(object):
    def __init__(self):
        # self.last = self.timestamp()
        if not path.exists(settings.BOTH_DIR):
            os.mkdir(settings.BOTH_DIR)
        if not path.exists(settings.RECORD_DIR):
            os.mkdir(settings.RECORD_DIR)

    def timestamp(self):
        dt = datetime.datetime.fromtimestamp(time.time())
        return dt.strftime("%d%m%y%H%M%S")

    def gen(self, filename, vol="0", rand=True, odd=False, all=False, effects=False):
        recs = self.reclist()
        if not len(recs) > 0:
            return
        if rand:
            random.shuffle(recs)
        else:
            recs.sort()
            recs.reverse()
        count = 0
        cat_string = ""
        # effects = "gain %s" % vol
        cat_count = 0
        if not odd:
            skip = False
        else:
            skip = True
        for rec in recs:
            count += 1
            if not skip or all:
                cat_string += "%s " % rec
                cat_count+=1
                skip = True
            else:
                skip = False
            if count > settings.MAX_PROCESSED:
                break
        # cat_string += filename + " gain -h " + "-v " + str(vol)
        cat_string += filename + " gain " + str(vol)
        if effects:
            # TONY ADD effects here
            cat_string += " flanger echo"
        if cat_count == 1:
            # print "sox %s " % cat_string
            call("sox %s " % cat_string, shell=True)
        elif cat_count > 1:
            # print "sox --combine concatenate %s" % cat_string
            call("sox --combine concatenate %s" % cat_string, shell=True)


    # Tony don't touch this one
    def gen_left(self):
        self.gen(settings.LEFT_PLAY, vol="1", rand=False, all=True)

    def gen_right(self): # Tony play with volume here
        self.gen(settings.RIGHT_PLAY, vol="-2", rand=True, all=True)

    def gen_both(self):
        # self.gen(settings.MIDDLE_PLAY, vol="-h", all=True)

        # call("sox --combine mix %s %s %s gain -h" % (settings.LEFT_PLAY, settings.MIDDLE_PLAY, "mixed"+settings.LEFT_PLAY), shell=True)
        # call("sox --combine mix %s %s %s gain -h" % (settings.RIGHT_PLAY, settings.MIDDLE_PLAY, "mixed"+settings.RIGHT_PLAY), shell=True)
        call("sox --combine merge %s %s %s" % (settings.LEFT_PLAY, settings.RIGHT_PLAY, settings.PLAY_BOTH), shell=True)
        # call("sox --combine merge %s %s %s gain -h" % ("mixed"+settings.LEFT_PLAY, "mixed"+settings.RIGHT_PLAY, settings.PLAY_BOTH), shell=True)

    def reclist(self):
        return glob.glob("%s/*.wav" % settings.RECORD_DIR)

    def run(self):

        while True:
            if len(self.blist()) > settings.MAX_PLAY:
                self.gen_left()
                self.gen_right()
                self.gen_both()
            time.sleep(0.5)

