#!/usr/bin/env python
#
# TO DO:
#
# * Tevatron's own results keep artificially incrementing the word count.
#
#
from willie import *
import codecs


logfile = "~/.willie/logs/raw.log"
epoch = "Jan 29  2014"

@module.commands('stats')
@module.example('.stats')
def stats(bot, trigger):
        word = trigger.group(2)
        bot.reply('Scouring the archives for your request, this may take a minute.....')
	total = 0
	with codecs.open(logfile, 'r', 'utf-8') as f:
	    for line in f:
	        finded = line.find(word)
	        if finded != -1 and finded != 0:
	            total += 1
	results = "The word %s has been mentioned %s times since %s." % (word, total, epoch)
	bot.reply(results)
	

