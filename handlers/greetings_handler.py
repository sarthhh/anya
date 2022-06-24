from __future__ import annotations

import typing as t

import hikari
import lightbulb

__all__: t.Tuple[str, ...] = ("GreetingsMethods",)


class GreetingMethods:
    """Handler for welcome and goodbye messages."""

    @staticmethod
    async def set_channel(
        context: lightbulb.Context,
        greeting: str,
        channel: hikari.GuildTextChannel,
    ) -> None:
        """Helper function for commands used for setting greeting channels.

        Paramaters
        ----------

            context: :class:`lightbulb.Context`
                The context which awaited this coro.
            greeting: :class:`str`
                Type of greeting.
            channel: :class:`hikari.GuildTextChannel`
                The new channel to setup for greetings.

        """
        data = await context.bot.greeting_db.get_greeting_data_for(  # type: ignore
            greeting, context.guild_id
        )
        if not data:
            await context.bot.greeting_db.set_welcome_data_for_guild(  # type: ignore
                context.guild_id, channel.id
            )
        else:
            await context.bot.greeting_db.update_channel_for(  # type: ignore
                greeting, context.guild_id, channel.id
            )

        await context.respond(
            embed=hikari.Embed(
                description=f"Set {greeting} channel to **{channel.name}** (<#{channel.id}>",
                color=context.bot.colors.peach_yellow,  # type: ignore
            ),
            reply=True,
        )

    @staticmethod
    async def set_message(
        context: lightbulb.Context, greeting: str, message: str
    ) -> None:
        """
        Updating the greeting message in the database.

        Paramaters
        ----------

            context: :class:`lightbulb.Context`
                The context which called the command.
            greeting: :class:`str`
                Type of greeting ( welcome/ goodbye )
            message: :class:`str`
                The new message to set.

        """

        context.bot.greeting_db.update_message_for(  # type: ignore
            greeting, context.guild_id, message
        )
        await context.respond(
            embed=hikari.Embed(
                description=f"Set welcome message to: ```\n{message}```", color=context.bot.colors.green  # type: ignore
            ),
            reply=True,
        )

    @staticmethod
    async def set_color(
        context: lightbulb.Context, greeting: str, new_color: int
    ) -> None:
        """
        Updating the greeting color in the database.

        Paramaters
        ----------

            context: :class:`lightbulb.Context`
                The context which called the command.
            greeting: :class:`str`
                Type of greeting ( welcome/ goodbye )
            new_color: :class:`int`
                Hex/Int value of the color to set.


        """
        await context.bot.greeting_db.update_color_for(  # type: ignore
            greeting, context.guild_id, new_color
        )
        await context.respond(
            embed=hikari.Embed(
                description=f"Set {greeting} color to `{new_color}`", color=new_color  # type: ignore
            )
        )

    @staticmethod
    async def set_bytes(
        context: lightbulb.Context, greeting: str, data_bytes: bytes
    ) -> None:
        """
        Setting up welcome/goodbye image for the guild.

        Paramaters
        ----------

            context: :class:`lightbulb.Context`
                The context which called the command.
            greeting: :class:`str`
                Type of greeting.
            data_bytes: :class:`bytes`
                Bytes of the image data.

        """

        await context.bot.greeting_db.set_image_for(  # type: ignore
            greeting, context.guild_id, data_bytes
        )

    @staticmethod
    async def toggle_embed(
        context: lightbulb.Context, greeting: str, toggle: bool = True
    ) -> None:
        """
        Toggle between embed and text type log messages.

        Paramaters
        ----------

            context: :class:`lightbulb.Context`
                The context which called the command.
            greeting: :class:`str`
                Type of greeting.
            toggle: :class:`bool`
                Embed value: True/False.

        """

        await context.bot.greeting_db.set_embed_option(  # type: ignore
            greeting, context.guild_id, toggle
        )
        await context.respond(
            embed=hikari.Embed(
                description=f"Messages will now appear as `{'embed' if toggle is True else 'text'}` messages",
                color=context.bot.colors.green,  # type: ignore
            )
        )
