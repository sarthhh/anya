from __future__ import annotations

import typing as t

import aiomysql  # type: ignore

__all__: t.Tuple[str, ...] = ("DatabaseModel",)


class DatabaseModel:
    database_pool: aiomysql.Pool

    async def exec_write_query(
        self, query: str, data: t.Tuple[t.Any, ...] | None = None
    ) -> None:
        """Executing a MySQL write query.

        Parameters
        ----------

            `query`: :class:`str`
                The sql query to execute
            `data`: :class:`tuple`
                The arguments to provide in the execute method.

        """
        async with self.database_pool.acquire() as conn:  # conn: aiomysql.Connection
            async with conn.cursor() as cursor:  # cursor: aiomysql.Cursor
                await cursor.execute(query, data)
            await conn.commit()

    async def exec_fetchone(
        self, query: str, data: t.Tuple[t.Any, ...] | None = None
    ) -> tuple[t.Any, ...]:
        """Executing a MySQL .fetchone() query.

        Parameters
        ----------

            `query`: :class:`str`
                The sql query to execute
            `data`: :class:`tuple`
                The arguments to provide in the execute method.

        """
        async with self.database_pool.acquire() as conn:  # conn: aiomysql.Connection
            async with conn.cursor() as cursor:  # cursor: aiomysql.Cursor
                await cursor.execute(query, data)
            return await cursor.fetchone()

    async def exec_fetchmany(
        self, num: int, query: str, data: t.Tuple[t.Any, ...] | None = None
    ) -> list[tuple[t.Any, ...]]:
        """Executing a MySQL .fetchmany() query.

        Parameters
        ----------
            `num`: :class:`int`
                Amount of queries to fetch
            `query`: :class:`str`
                The sql query to execute
            `data`: :class:`tuple`
                The arguments to provide in the execute method.

        """
        async with self.database_pool.acquire() as conn:  # conn: aiomysql.Connection
            async with conn.cursor() as cursor:  # cursor: aiomysql.Cursor
                await cursor.execute(query, data)
            return await cursor.fetchmany(num)

    async def exec_fetchall(
        self, query: str, data: t.Tuple[t.Any, ...] | None = None
    ) -> list[tuple[t.Any, ...]]:
        """Executing a MySQL .fetchall() query.

        Parameters
        ----------

            `query`: :class:`str`
                The sql query to execute
            `data`: :class:`tuple`
                The arguments to provide in the execute method.

        """
        async with self.database_pool.acquire() as conn:  # conn: aiomysql.Connection
            async with conn.cursor() as cursor:  # cursor: aiomysql.Cursor
                await cursor.execute(query, data)
            return await cursor.fetchall()
