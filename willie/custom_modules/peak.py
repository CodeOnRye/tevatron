from willie import *
from collections import Counter
import re
import os

dbfile = os.path.dirname(os.path.realpath(__file__)) + '/peak.db'

def timestamp():
    lt = time.localtime(time.time())
    return "%02d.%02d.%04d %02d:%02d:%02d" % (lt[2], lt[1], lt[0], lt[3], lt[4], lt[5])

#def users(channel):
   

@module.event('JOIN')
@module.rule('.*')
def peak(bot, trigger):
    names = re.split(' ', trigger)
    channels = re.search('(#\S*)', bot.raw)
    if (channels is None):
        return
    channel = channels.group(1)
    users = bot.privileges[channel]
    pop = len(users)
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

@module.commands('peakusers')
@module.example('.peakusers')
def peakusers(bot, trigger):
    f = open(dbfile, 'r')
    count = f.read()
    bot.reply("The most meatbags I've seen were XX  here, give or take a few superior beings like me.")

@module.commands('peakdb')
@module.example('.peakdb')
def peakdb(bot, trigger):
   t = bot.db.table('tevatrondb', 'peak', 'count, date', 'count')
   #count = table.get(1,1);
   bot.reply("The count is")


#@module.commands('usercount')
#@module.example('.usercount')
#def usercount(bot, trigger):
#    bot.reply(db.users())
