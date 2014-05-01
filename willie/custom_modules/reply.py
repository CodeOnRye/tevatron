from willie import module

@module.rule('hello!?')
def hi(bot, trigger):
   bot.say('Hi, ' + trigger.nick)
