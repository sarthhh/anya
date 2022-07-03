from __future__ import annotations

import typing as t

import aiomysql  # type: ignore
import hikari

from .base_model import DatabaseModel

__all__: t.Tuple[str, ...] = ("PrefixDatabase",)


class PrefixDatabase(DatabaseModel):
    """
    Class for managing server custom prefixes.

    Attributes
    ----------

        database_poll: :class:`aiomysql.Poll`
            The pool passed by the `.Bot` class for this class to function.
        prefix_cache: :class:`dict[int, str]`
            A dictionary with guild_id to prefix key, value pair.

    """

    database_pool: aiomysql.Pool
    prefix_cache: dict[int | hikari.Snowflake | None, str] = {}

    async def setup(self, bot: hikari.GatewayBot) -> aiomysql.Pool:
        """
        Setting up this database class for usage.

        Parameters
        ----------

            bot: :class:`hikari.GatewayBot`
                The bot class this prefix class is for.

        Returns
        -------

            :class:`aiomysql.Pool`

        """
        self.database_pool = bot.database_pool  # type: ignore

        await self.exec_write_query(
            """
            CREATE TABLE IF NOT EXISTS prefixes
            ( guild_id BIGINT, prefix VARCHAR (10) );
            """
        )

    async def get_prefix_by_id(self, guild_id: int | hikari.Snowflake | None) -> str:
        """
        Getting the prefix for the guild whose id is provided.

        This method look-ups into the cache first, if the prefix is not found in cache
        the method fetchs it from the database, and adds it to the cache

        Parameters
        ---------

            guild_id: :class:`int`
                Guild ID for which prefix is needed.

        Returns
        -------

            :class:`str`

        """
        cache = self.prefix_cache.get(guild_id)
        if cache:
            return cache
        data = await self.exec_fetchone(
            """
            SELECT * FROM prefixes
            WHERE guild_id = %s;
            """,
            (guild_id,),
        )

        if data:
            self.prefix_cache[guild_id] = data[1]
            return data[1]  # cache-ing and returning custom prefix
        else:
            self.prefix_cache[guild_id] = "anya"
            return "anya"  # cache-ing and returning default prefix

    async def set_prefix(self, guild_id: int | None, prefix: str) -> None:
        """
        Method used to update/set prefix for a server.

        This adds the updated prefix both in the cache and the database.

        Parameters
        ----------

            guild_id: :class:`int`
                ID of the guild to update prefix of
            prefix: :class:`str`
                The new prefix

        """
        self.prefix_cache[guild_id] = prefix  # updating the prefix in cache
        if await self.get_prefix_by_id(guild_id):
            await self.exec_write_query(
                """
                UPDATE prefixes
                SET prefix = %s
                WHERE guild_id = %s;
                """,
                (prefix, guild_id),
            )
        else:
            await self.exec_write_query(
                """
                INSERT INTO prefixes
                VALUES ( %s , %s );
                """,
                (guild_id, prefix),
            )
