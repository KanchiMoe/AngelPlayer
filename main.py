'''Main file that actually runs the bot'''
import os
import mybot
import cmds

async def logger(cxt):
    '''Logs who did what'''
    mybot.LOGGER.info('%s:%s ran command %s with args %s',
                      cxt.message.author.name, cxt.message.author.discriminator,
                      cxt.command, cxt.args)

mybot.bot.before_invoke(logger)
mybot.bot.run(os.environ['TOKEN'])
