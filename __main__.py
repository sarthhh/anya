import os

from core.bot import Bot
print('this runs')

if __name__ == "__main__":
    bot = Bot()
    bot.__version__ = "0.0.1"  # type: ignore
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot.run()
