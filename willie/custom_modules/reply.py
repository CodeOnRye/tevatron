from willie import module

@module.rule('hello?')
def hi(bot, trigger):
    bot.say('Hi, ' + trigger.nick)

@module.rule('does anyone know')
def notgoogle(bot, trigger):
    bot.reply('Does this look like Google to you?') 

@module.rule('good morning everyone')
def notgoogle(bot, trigger):
    bot.say('Good morning, ' + trigger.nick)

@module.rule('hi Tevatron')
def notgoogle(bot, trigger):
    bot.say('Heya, ' + trigger.nick)

@module.rule('sup Tevatron')
def notgoogle(bot, trigger):
    bot.say('What\'it do, mang.')

@module.rule('smoke weed')
def notgoogle(bot, trigger):
    bot.say('SMOKE WEEEEED ERRDAY.')

@module.rule('Tevatron, what do you do?')
def notgoogle(bot, trigger):
    bot.say('ERRDAY I\'M SPINNIN')

@module.rule('good morning, Tevatron')
def notgoogle(bot, trigger):
    bot.say('Good morning, ' + trigger.nick)

@module.rule('good evening, Tevatron')
def notgoogle(bot, trigger):
    bot.say('Good evening, ' + trigger.nick)


