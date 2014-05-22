from willie import *
from collections import Counter
import re

dbfile = '/home/tevatron/.willie/modules/peak.db'

def timestamp():
    lt = time.localtime(time.time())
    return "%02d.%02d.%04d %02d:%02d:%02d" % (lt[2], lt[1], lt[0], lt[3], lt[4], lt[5])



@module.event('JOIN')
@module.rule('.*')
def peak(bot, trigger):
    names = re.split(' ', trigger)
    channels = re.search('(#\S*)', bot.raw)
    if (channels is None):
        return
    channel = channels.group(1)
    pop = len(bot.privileges[channel])
    p = open(dbfile, 'r')
    current = p.read()
    peak = int(current)
    if pop > peak:
        popNotice = "Peak user count reached: %s" % pop
        bot.say(unicode(popNotice))
        f = open(dbfile, 'w')
        pop = str(pop)
        f.write(pop)
        f.close()

