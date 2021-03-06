from __future__ import annotations

import datetime
import typing as t

import hikari

__all__: t.Tuple[str, ...] = ("Greeting",)


class Greeting:
    """
    Object construtor for data fetched from the MySQL database.

    Parameters
    ----------

        bot: :class:`hikari.GatewayBot`
            The bot class to make this class for.
        data: :class:`tuple`
            Raw tuple response from the database.

    """

    def __init__(
        self,
        bot: hikari.GatewayBot,
        data: tuple[int, int, str, int, bytes | None, int],
    ) -> None:
        self.data = data
        self.bot = bot

    @property
    def channel(self) -> hikari.GuildChannel | None:
        if (guild := self.bot.cache.get_guild(self.data[0])) is not None:
            return guild.get_channel(self.data[1])
        return None

    @property
    def message(self) -> str:
        return self.data[2]

    @property
    def color(self) -> hikari.Color:
        return hikari.Color(self.data[3]) if self.data[3] is not None else 0x00000

    @property
    def welcome_bytes(self) -> hikari.Bytes | None:
        return hikari.Bytes(self.data[4], "greeting.png") if self.data[4] else None

    @property
    def is_embed(self) -> bool:
        return True if self.data[5] == 1 else False


class CardSpawn:
    def __init__(self, data_tuple) -> None:
        self.data = data_tuple

    @property
    def guild_id(self) -> int:
        return self.data[0]

    @property
    def spawn_ts(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.data[1])

    @property
    def name(self) -> str:
        return self.data[2]

    @property
    def tier(self) -> int:
        return self.data[3]

    @property
    def url(self) -> str:
        return self.data[4]

    @property
    def v(self) -> int:
        return self.data[5]

    @property
    def claimer_id(self) -> int:
        return self.data[6]
