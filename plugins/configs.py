from __future__ import annotations

import hikari
import lightbulb

from core.bot import Bot
from core.exceptions import DoNothing, InvalidChoice, NoChannelSetup
from handlers.greetings_handler import GreetingMethods
from handlers.image_handlers import GreetingImage


class Plugin(lightbulb.Plugin):
    def __init__(self) -> None:
        super().__init__(name="Config", description="Bot configuration for you server.")
        self.pos = 1
        self.bot: Bot
        self.base_colors: dict[str, int]


plugin = Plugin()


def do_setups() -> None:
    plugin.base_colors: dict[str, int] = {  # type: ignore
        "blue": plugin.bot.colors.blue,
        "red": plugin.bot.colors.red,
        "yellow": plugin.bot.colors.yellow,
        "green": plugin.bot.colors.green,
        "black": plugin.bot.colors.black,
        "white": plugin.bot.colors.white,
        "grey": plugin.bot.colors.cool_grey,
    }


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
    """
    Setting up a channel for the particular greeting.

    **Allowed Arguments:**
    `greeting`: A choice between `welcome` and `goodbye`.
    `channel`: The channel to send the greetings in

    **Example Usage:** `anya greetings channel welcome #new_users
    """
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
        raise InvalidChoice(
            context,
            "greeting",
            ("welcome", "goodbye"),
            "Invalid choice, `welcome` and `goodbye` are only usable choice.",
        )

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
    """
    Edit the message for the content or embed description for a particular greeting.

    **Allowed Arguments:**
    `greeting`: The greeting to edit message for (`welcome`/`goodbye`)
    `message`: The new message.

    **Example Usage:** `anya greetings message welcome Hey $user, welcome to $server. Have a great stay.`
    """
    await check_setup(context, greeting)
    message = message.replace("\\n", "\n")
    await GreetingMethods.set_message(context, greeting, message)


@greetings.child
@lightbulb.command(
    name="image", description="Set the greeting image to appear in the message."
)
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def use_the_slash(
    context: lightbulb.PrefixContext,
) -> None:
    """
    Slash command only.
    """
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
        ).set_image(hikari.Bytes(image, "image.png")),
        reply=True,
    )


@greetings.child
@lightbulb.option(
    name="selection", description="Choose the message type", choices=("embed", "text")
)
@lightbulb.option(
    name="greeting",
    description="Greeting type to update.",
    choices=("welcome", "goodbye"),
)
@lightbulb.command(
    name="type", description="The message type for welcome.", pass_options=True
)
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def welcome_type(
    context: lightbulb.PrefixContext | lightbulb.SlashContext,
    greeting: str,
    selection: str,
) -> None:
    """
    Weather to send text or embed messages for greetings

    **Allowed Arguments:**
    `greeting`: The greeting to edit message for (`welcome`/`goodbye`)
    `type`: text or embed.

    **Example Usage:** `anya greetings type welcome text`
    """
    if not selection in (allowed := ("embed", "text")):
        raise InvalidChoice(
            context,
            "selection",
            allowed,
            f"Invalid choice `{selection}` was passed for the `selection` argument.",
        )

    sel = True if selection == "embed" else False
    await GreetingMethods.toggle_embed(context, greeting, sel)


@greetings.child
@lightbulb.option(name="color", description="The next for new color", autocomplete=True)
@lightbulb.option(
    name="greeting",
    description="Greeting type to update.",
    choices=("welcome", "goodbye"),
)
@lightbulb.command(
    name="color",
    description="The embed color for greeting message",
    aliases=["colour"],
    pass_options=True,
)
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def embed_color(
    context: lightbulb.PrefixContext | lightbulb.SlashContext, greeting: str, color: str
) -> None:
    """
    Setup color for greeting embeds.

    **Allowed Arguments:**
    `greeting`: The greeting to edit message for (`welcome`/`goodbye`)
    `color`: A color hex (or color name in slash commands.)

    **Example Usage:** `anya greetings color welcome FFFFFF`
    """
    await check_setup(context, greeting)
    try:
        c = int(color, 16)
        print(c)
    except ValueError:
        await context.respond(
            embed=hikari.Embed(
                description=f"`{color}` is not a valid color hex value.",
                color=plugin.bot.colors.red,
            ),
            reply=True,
        )
        return
    await GreetingMethods.set_color(context, greeting, c)


@embed_color.autocomplete("color")
async def callback(
    option: hikari.AutocompleteInteractionOption, inter: hikari.AutocompleteInteraction
) -> list[hikari.CommandChoice]:
    if not (a := option.value):

        return [
            hikari.CommandChoice(name=x, value=str(y))
            for x, y in plugin.base_colors.items()
        ]
    if isinstance(a, int):
        return []
    return [
        hikari.CommandChoice(name=x, value=str(y))
        for x, y in [
            (name, getattr(plugin.bot.colors, name))
            for name in dir(plugin.bot.colors)
            if a in name and name[:2] != "__"
        ]
    ][:25]


def load(bot: Bot) -> None:
    bot.add_plugin(plugin)
    do_setups()


def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)
