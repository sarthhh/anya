from __future__ import annotations

import hikari
import lightbulb

from core.bot import Bot
from core.exceptions import DoNothing, NoChannelSetup
from database.greetings_database import GreetingsHandler
from handlers.greetings_handler import GreetingMethods
from handlers.image_handlers import GreetingImage


class Plugin(lightbulb.Plugin):
    def __init__(self) -> None:
        super().__init__(name="Config", description="Bot configuration for you server.")
        self.pos = 1
        self.bot: Bot


plugin = Plugin()


@plugin.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_GUILD))
@lightbulb.option(
    name="new_prefix",
    description="The new server prefix",
    modifier=lightbulb.OptionModifier.CONSUME_REST,
)
@lightbulb.command(name="prefix", description="Change server prefix.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def change_prefix(
    context: lightbulb.PrefixContext | lightbulb.SlashContext,
) -> None:
    """Change the prefix of your server to the one you want.

    **Allowed Arguments:**
    `new_prefix`: The new prefix for the server.

    **Example Usage:** `anya prefix !`
    `!` is your new prefix now!

    Note: Discord markdown characters like `, #, @, *, / are not allowed.
    """

    if len(context.options.new_prefix) > 10 or any(
        (
            char in context.options.new_prefix
            for char in (
                "`",
                "/",
                "@",
                "#",
                "*",
            )
        )
    ):  # avoiding prefixes longer than 10 characters or with discord markdown.
        await context.respond(
            embed=hikari.Embed(
                color=plugin.bot.colors.dark_red,
                description=(
                    "This could be because your prefix,"
                    "- Is more than 10 characters in length"
                    "\n- Has `, /, @, #, * markdown in it."
                ),
            ).set_author(name="Unable to set prefix."),
            reply=True,
        )
        return

    await plugin.bot.prefix_db.set_prefix(context.guild_id, context.options.new_prefix)
    await context.respond(
        embed=hikari.Embed(
            color=plugin.bot.colors.green,
            description=f"Changed server prefix to `{context.options.new_prefix}`",
        ),
        reply=True,
    )


@plugin.command
@lightbulb.command(
    name="greetings",
    description="Greetings setting for the server,",
)
@lightbulb.implements(lightbulb.PrefixCommandGroup, lightbulb.SlashCommandGroup)
async def greetings(_: lightbulb.PrefixContext | lightbulb.SlashContext) -> None:
    """
    Welcome/Goodbye commands to have a log of new joins and leaves.

    - This module has 5 customisations: `channel`, `message`, `color`, `image` & `embed`

    **Example Usage:** `anya greetings channel <welcome/goodbye> <#channel>`

    """
    pass


@greetings.child
@lightbulb.option(
    name="channel",
    description="Channel to send logs in.",
    type=hikari.TextableGuildChannel,
    channel_types=[hikari.ChannelType.GUILD_TEXT],
)
@lightbulb.option(
    name="greeting",
    description="Greeting type to change.",
    choices=["welcome", "goodbye"],
)
@lightbulb.command(
    name="channel", description="Set channel for greetings log.", pass_options=True
)
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def set_channel(
    context: lightbulb.SlashContext | lightbulb.PrefixContext,
    greeting: str,
    channel: hikari.GuildTextChannel,
) -> None:
    if not greeting.lower() in ("welcome", "goodbye"):
        await context.respond(
            embed=hikari.Embed(
                description="Invalid choice, `welcome` and `goodbye` are only usable choice.",
                color=plugin.bot.colors.red_brown,
            ),
            reply=True,
        )
        return
    await GreetingMethods.set_channel(context, greeting, channel)


async def check_setup(
    context: lightbulb.SlashContext | lightbulb.PrefixContext, greeting
) -> None:
    if not (g_id := context.guild_id):
        return
    if not greeting.lower() in ("welcome", "goodbye"):
        await context.respond(
            embed=hikari.Embed(
                description="Invalid choice, `welcome` and `goodbye` are only usable choice.",
                color=plugin.bot.colors.red_brown,
            ),
            reply=True,
        )
        raise DoNothing("...")

    if not (data := await plugin.bot.greeting_db.get_greeting_data_for(greeting, g_id)):
        raise NoChannelSetup(
            context,
            f"You need to setup a greeting channel for `{greeting}` category before updating other elements.",
        )


@greetings.child
@lightbulb.option(
    name="message",
    description="The new message which will appear on greetings.",
    modifier=lightbulb.OptionModifier.CONSUME_REST,
)
@lightbulb.option(
    name="greeting",
    description="Greeting type to change.",
    choices=["welcome", "goodbye"],
)
@lightbulb.command(
    name="message", description="Customise greetings message.", pass_options=True
)
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def set_message(
    context: lightbulb.SlashContext | lightbulb.PrefixContext,
    greeting: str,
    message: str,
) -> None:
    await check_setup(context, greeting)
    message = message.replace("\\n", r"\n")
    await GreetingMethods.set_message(context, greeting, message)


@greetings.child
@lightbulb.command(
    name="image", description="Set the greeting image to appear in the message."
)
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def use_the_slash(
    context: lightbulb.PrefixContext,
) -> None:
    await context.respond(
        embed=hikari.Embed(
            description="Please use the slash version of this command for better functionality.",
            color=plugin.bot.colors.yellow_green,
        ),
        reply=True,
    )


@greetings.child
@lightbulb.option(
    name="attachment",
    description="The image to set for greeting messages. Preferred size: ()",
    type=hikari.Attachment,
)
@lightbulb.option(
    name="greeting",
    description="Greeting type to update.",
    choices=("welcome", "goodbye"),
)
@lightbulb.command(
    name="image",
    description="Set the greeting image to appear in the message.",
    pass_options=True,
    auto_defer=True,
)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def set_image(
    context: lightbulb.PrefixContext | lightbulb.SlashContext,
    greeting: str,
    attachment: hikari.Attachment,
) -> None:
    if not (guild_id := context.guild_id):
        return
    await check_setup(context, greeting)
    await context.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
    image = await GreetingImage.prepare_image_bytes(attachment, guild_id)
    await GreetingMethods.set_bytes(context, greeting, image)
    await context.respond(
        embed=hikari.Embed(
            description=f"Set `{greeting} image to`",
            color=plugin.bot.colors.pink_flamingo,
        ).set_image(hikari.Bytes(image, "image.png"))
    )


def load(bot: Bot) -> None:
    bot.add_plugin(plugin)


def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)


hikari.OptionType.ATTACHMENT
