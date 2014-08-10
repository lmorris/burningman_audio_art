__author__ = 'bm'

from glob import glob
import os
from subprocess import call, Popen, PIPE
import settings
# os.chdir("/home/bm/charm/burningman_audio_art/recordings")

files = glob("*.wav")
files.sort()
files.reverse()
print "Num files: %s" % len(files)
for file in files:
    p = Popen("sox %s -n stats" % file, shell=True, stderr=PIPE)

    avg_db = -32.0
    for line in p.stderr.readlines():
        if "RMS lev dB" in line:
            line = ''.join(line.split("RMS lev dB"))
            line = line.strip()
            avg_db = float(line)

    if avg_db > settings.AVG_DB_MAX:
        print file
        print "*************Rejected AVB DB: %s" % avg_db
        os.unlink(file)
    if avg_db > settings.AVG_DB_ADJUST:
        print os.path.abspath(file)
        print "*************Rejected AVB DB: %s" % avg_db
        call("sox %s %s gain -10" % (file, "1_"+file), shell=True)
    if avg_db < settings.AVG_DB_MIN:
        print file
        print "*************Rejected AVG DB: %s" % avg_db
        os.unlink(file)

