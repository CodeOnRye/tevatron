from willie import *
import random

qdb = "/home/tevatron/.willie/modules/quote.db"

@module.commands('addquote')
@module.example('.addquote <beekar> I love peanutbutter and jelly.')
def addquote(bot, trigger):
        quote = trigger.group(2)
        f = open(qdb, 'a')
        f.write("\n%s" % quote)
        f.close()
        bot.reply('Added it...')

@module.commands('quote')
@module.example('.quote')
def quote(bot, trigger):
        f = open(qdb, 'r')
        line = random.choice(list(open(qdb)))
        bot.reply(line)

