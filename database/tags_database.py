import typing as t

import aiomysql  # type: ignore

from .base_model import DatabaseModel

if t.TYPE_CHECKING:
    from core.bot import Bot


class TagsDatabase(DatabaseModel):
    database_pool: aiomysql.Pool

    async def setup(self, bot: "Bot") -> None:
        """
        Setup for the Tags database.

        Parameters
        ----------

            bot: :class:`Bot`
                The bot class with database pool.

        Returns
        -------

            :class:`None`

        """

        self.database_pool = bot.database_pool

        await self.exec_write_query(
            """
            CREATE TABLE IF NOT EXISTS tags
            (
                guild_id BIGINT,
                user_id BIGINT,
                name VARCHAR(50),
                value VARHCAR(4000),
                uses INT
            )
            """
        )

    async def add_tag(self, guild_id: int, user_id: int, tag: str, value: str) -> None:
        """
        Add a new tag to the database.

        Parameters
        ----------

            guild_id: :class:`int`
                The ID of server related to the tag.
            user_id: :class:`int`
                The user ID of user who created this tag.
            tag: :class:`str`
                Name of the tag.
            value: :class:`str`
                The message to send on tag's invocation.

        """
        await self.exec_write_query(
            """
            INSERT INTO tags
            VALUES ( ?, ?, ?, ?, 0 )
            """,
            (
                guild_id,
                user_id,
                tag,
                value,
            ),
        )

    async def delete_tag(self, guild_id: int, name: str) -> None:
        """
        Deletes a tag in a given guild.

        Parameters
        ----------

            guild_id: :class:`int`
                The server ID for which the tag is to be deleted.
            name: :class:`str`
                Name of the tag.

        """

        await self.exec_write_query(
            """
            DELETE FROM tags
            WHERE guild_id = ? and name = ?
            """,
            (guild_id, name),
        )
