from willie import module

@module.event('JOIN')
@module.rule('.*')
def joinEvent(bot, trigger):
   bot.say('Someone Joined')
#   peakValue = bot.db.users()
#   bot.say(peakValue)

@module.event('PART')
@module.rule('.*')
def quitEvent(bot, trigger):
   bot.say('Someone Left')


@module.commands('peak')
def echo(bot, trigger):
    bot.reply('this is the peak')
