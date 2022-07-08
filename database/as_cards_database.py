import datetime
import typing as t

import aiomysql  # type: ignore
import lightbulb

if t.TYPE_CHECKING:
    from core.bot import Bot

from core.objects import CardSpawn

from .base_model import DatabaseModel

__all__: t.Tuple[str, ...] = ("ShoobCardDatabase",)


class ShoobCardDatabase(DatabaseModel):
    database_pool: aiomysql.Pool

    async def setup(self, bot: "Bot") -> None:
        """
        Setting up this database class for usage.
        Parameters
        ----------
            bot: :class:`lightbulb.BotApp`
                The bot class this class is for.


        """
        self.database_pool = bot.database_pool
        await self.exec_write_query(
            """
            CREATE TABLE IF NOT EXISTS cardspawns
            (
                guild_id BIGINT,
                spawn_ts BIGINT,
                card_name VARCHAR(40),
                tier INT,
                card_url VARCHAR(100),
                card_v BIGINT,
                claimer_id BIGINT
            );
            """
        )

    async def insert_spawn_data(
        self,
        guild_id: int,
        spawn_ts: int,
        card_name: str,
        tier: int,
        card_url: str,
        card_v: int | None = None,
        claimer_id: int | None = None,
    ) -> None:
        """
        Inserting new card spawn and claim data in the database.
        Parameters
        ----------
            guild_id: :class:`int`
                ID of the guild where card spawned
            spawn_ts :class:`int`
                Timestamp of time at which the card was claimed
            card_name: :class:`str`
                Name of the card
            tier: :class:`int`
                Tier of the card that got spawned
            card_v: :class:`int`
                Version of the card
            claimer_id :class:`typing.Optional[int]
                ID of the user who claimed the card
        """
        await self.exec_write_query(
            """
            INSERT INTO cardspawns
            VALUES ( %s, %s, %s,%s, %s, %s, %s )
            """,
            (guild_id, spawn_ts, card_name, tier, card_url, card_v, claimer_id),
        )

    async def recent_guild_spawns(self, guild_id, limit=5) -> list[CardSpawn]:
        """Getting recent spawns in the server.
        Parameters
        ----------
            guild_id: :class:`int`
                ID of the server.
            limit: :class:`int`
                Max number of card data to get.
        Returns
        -------
            :class:`CardSpawn`
        """
        data_list = await self.exec_fetchmany(
            limit,
            """
            SELECT * FROM cardspawns
            WHERE guild_id = %s
            ORDER BY spawn_ts DESC
            """,
            (guild_id,),
        )

        return [CardSpawn(data) for data in data_list if data]

    async def recent_guild_claims(self, guild_id: int, limit=5) -> list[CardSpawn]:
        """Getting recent claims in the server.
        Parameters
        ----------
            guild_id: :class:`int`
                ID of the server.
            limit: :class:`int`
                Max number of card data to get.
        Returns
        -------
            :class:`CardSpawn`
        """
        data_list = await self.exec_fetchmany(
            limit,
            """
            SELECT * FROM cardspawns
            WHERE guild_id = %s AND claimer_id IS NOT NULL
            ORDER BY spawn_ts DESC
            """,
            (guild_id,),
        )

        return [CardSpawn(data) for data in data_list if data]

    async def recent_guild_despawns(
        self, guild_id: int, limit: int = 5
    ) -> list[CardSpawn]:
        """Getting recent despawns in the server.
        Parameters
        ----------
            guild_id: :class:`int`
                ID of the server.
            limit: :class:`int`
                Max number of card data to get.
        Returns
        -------
            :class:`CardSpawn`
        """
        data_list = await self.exec_fetchmany(
            limit,
            """
            SELECT * FROM cardspawns
            WHERE guild_id = %s AND claimer_id IS NULL
            ORDER BY spawn_ts DESC
            """,
            (guild_id,),
        )

        return [CardSpawn(data) for data in data_list if data]

    async def recent_tier_spawns(
        self, guild_id: int, tier: int, limit: int = 5
    ) -> list[CardSpawn]:
        """Getting recent spawns of a tier in the server.
        Parameters
        ----------
            guild_id: :class:`int`
                ID of the server.
            tier: :class:`int`
                Tier to get spawns for
            limit: :class:`int`
                Max number of card data to get.
        Returns
        -------
            :class:`CardSpawn`
        """
        data_list = await self.exec_fetchmany(
            limit,
            """
            SELECT * FROM cardspawns
            WHERE guild_id = %s AND tier = %s
            ORDER BY spawn_ts DESC
            """,
            (guild_id, tier),
        )

        return [CardSpawn(data) for data in data_list if data]

    async def get_all_spawns(self, guild_id: int) -> list[CardSpawn]:
        """
        Getting all the spawns in the server.

        Parameters
        ----------
            guild_id: :class:`int`
                ID of the server.
        Returns
        -------
            :class:`CardSpawn`
        """
        data_list = await self.exec_fetchall(
            """
            SELECT * FROM cardspawns
            WHERE guild_id = %s
            """,
            (guild_id,),
        )

        return [CardSpawn(data) for data in data_list if data]
