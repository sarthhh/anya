import hikari
import lightbulb

from core.bot import Bot
from core.exceptions import *


class Plugin(lightbulb.Plugin):
    def __init__(self) -> None:
        super().__init__("Error Handler")
        self.ignored = True
        self.bot: Bot


plugin = Plugin()


@plugin.listener(lightbulb.CommandErrorEvent)
async def error_handler(event: lightbulb.CommandErrorEvent) -> None:
    exc = event.exception
    context = event.context


def load(bot: Bot) -> None:
    bot.add_plugin(plugin)
