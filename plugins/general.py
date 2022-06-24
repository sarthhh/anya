from __future__ import annotations

import sys

import hikari
import lightbulb
import psutil  # type: ignore

from core.bot import Bot


class Plugin(lightbulb.Plugin):
    def __init__(self) -> None:
        super().__init__(name="General", description="Commands for general purpose.")
        self.bot: Bot
        self.pos = 3  # type: ignore


plugin = Plugin()


@plugin.command
@lightbulb.command(
    name="ping", description="Latency of the bot in ms", aliases=["latency"]
)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping_cmd(context: lightbulb.PrefixContext | lightbulb.SlashContext) -> None:
    """Check the heartbeat latency of the bot.

    **Example Usage:** `anya ping`
    """
    await context.respond(
        embed=hikari.Embed(
            color=plugin.bot.colors.rose_pink,
            description=f"{plugin.bot.cache.get_emoji(981301275482284042)} Pong! `{round(context.bot.heartbeat_latency*1000, 2)}ms`",
        )
    )


@plugin.command
@lightbulb.command(
    name="info", description="Some info about the bot", aliases=["botinfo", "about"]
)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def botstats(context: lightbulb.PrefixContext | lightbulb.SlashContext) -> None:
    """
    Some basic info about the bot including its stats and other data.

    **Example Usage**: `anya info`

    Note: The information returned can, or cannot be accurate depending upon the bot's cache.
    """

    v = sys.version_info
    info = f"""

    anya is a multipurpose anime based discord bot with awesome features like Shoob commands and server automations. 
    Use `anya commands` to get a list of all commands.
    Read more here: https://sarthhh.github.io/anya

    **__STATS AND INFO__** 

    **Bot Uptime**: {plugin.bot.uptime}
    **Server Count**: {len(plugin.bot.cache.get_guilds_view())}
    **CPU Usage**: {psutil.cpu_percent()}%
    **Memory Usage**: {int(psutil.virtual_memory().percent)}% , {int(psutil.virtual_memory().used*0.00000095367432)}mb /{int(psutil.virtual_memory().total*0.00000095367432)}mb
    **Python Version**: {f'{v.major}.{v.minor}.{v.micro}.{v.releaselevel}'}
    **Hikari Version**: {hikari.__version__}
    **Lightbulb Version**: {lightbulb.__version__}
    """.replace(
        "\t", ""
    )
    embed = (
        hikari.Embed(
            color=plugin.bot.colors.peach_yellow, description=info.strip("    ")
        )
        .set_thumbnail(plugin.bot.get_me().avatar_url)  # type: ignore
        .set_image(
            "https://raw.githubusercontent.com/sarthhh/anya/main/docs/assets/banner.png"
        )
        .set_footer(
            text=f"Requested by {context.author}", icon=context.author.avatar_url
        )
    )
    await context.respond(embed=embed, reply=True)


@plugin.command
@lightbulb.command(name="commands", description="A list of all bot commands.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def list_commands(
    context: lightbulb.PrefixContext | lightbulb.SlashContext,
) -> None:
    """A list of all the prefix commands in the bot.
    For slash commands you can use `/` and navigate to bot's menu on discord to view its slash commands.

    **Example Usage:** `anya commands`
    """
    embed = (
        hikari.Embed(
            color=plugin.bot.colors.peach_yellow,
            description=(
                "This is a list of all Prefix commands. "
                "You can use `/` and navigate to bot's menu on discord to view its slash commands."
            ),
        )
        .set_author(name="COMMAND LIST", icon=plugin.bot.get_me().avatar_url)  # type: ignore
        .set_thumbnail("https://cdn.discordapp.com/emojis/981311615821565973.webp")
        .set_image(
            "https://raw.githubusercontent.com/sarthhh/anya/main/docs/assets/commands.png"
        )
        .set_footer(
            text=f"Requested by {context.author}", icon=context.author.avatar_url
        )
    )
    plugins = [
        plugin
        for plugin in context.bot.plugins.values()
        if getattr(plugin, "pos", None)
    ]
    plugins.sort(key=lambda p: p.pos)  # type: ignore
    for plgn in plugins:
        if getattr(plgn, "ignored", None):
            continue
        embed.add_field(
            name=f"{plgn.name.upper()} COMMANDS",
            value=f"```yaml\n{', '.join({cmd.name for cmd in plgn.all_commands})}\n```",
        )
    buttons = plugin.bot.rest.build_action_row()
    buttons.add_button(hikari.ButtonStyle.LINK, plugin.bot.invite_url).set_label(
        "Invite"
    ).set_emoji(981281185630134282).add_to_container()
    buttons.add_button(
        hikari.ButtonStyle.LINK, "https://sarthhh.github.io/anya"
    ).set_label("Docs").set_emoji(981281950255964170).add_to_container()
    await context.respond(embed=embed, reply=True, component=buttons)


def load(bot: Bot) -> None:
    bot.add_plugin(plugin)


def unload(bot: Bot) -> None:
    bot.remove_plugin(plugin)
