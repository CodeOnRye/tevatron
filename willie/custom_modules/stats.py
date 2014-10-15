#!/usr/bin/env python
#
# TO DO:
#
# * Tevatron's own results keep artificially incrementing the word count.
#
#
from willie import *
import codecs, re


logfile = "/home/tevatron/.willie/logs/raw.log"
epoch = "Jan 29  2014"

@module.commands('stats')
@module.example('.stats')
def stats(bot, trigger):
        word = trigger.group(2)
        bot.reply('Scouring the archives for your request, this may take a minute.....')
	with codecs.open(logfile, 'r', 'utf-8') as f:
            strings = re.findall(r'%s' % word, f.read())
            total = len(strings)

	results = "The word %s has been mentioned %s times since %s." % (word, total, epoch)
	bot.reply(results)
	

