from willie import module

@module.rule('hello!?')
def hi(bot, trigger):
   bot.say('Hi, ' + trigger.nick)

@module.rule('does anyone know')
def notgoogle(bot, trigger):
  bot.reply('Does this look like Google to you?') 
