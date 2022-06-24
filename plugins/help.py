import inspect
import typing as t

import hikari
import lightbulb

from core.bot import Bot

__all__: t.Tuple[str, ...] = ("Help",)


class Help(lightbulb.BaseHelpCommand):
    def __init__(self, app: lightbulb.BotApp) -> None:
        super().__init__(app)
        self.bot: Bot

    async def send_bot_help(self, context: lightbulb.Context) -> None:
        _p = await self.bot.prefix_db.get_prefix_by_id(context.guild_id)
        prefix = _p if _p != "anya" else "anya "

        embed = (
            hikari.Embed(color=self.bot.colors.peach_yellow).set_author(
                name=self.bot.get_me().username, icon=self.bot.get_me().avatar_url  # type: ignore
            )
            # .set_thumbnail(self.bot.get_me().avatar_url)
        )
        embed.description = (
            f"Hey there {context.author.username}, thanks for using **{self.bot.get_me().username}**!\n"  # type: ignore
            f"To get a list of all commands use `{prefix}commands`\n\n"
            f"For a better explanation about commands and bot functionality please visit https://sarthhh.github.io/anya"
        )

        embed.set_image(
            "https://raw.githubusercontent.com/sarthhh/anya/main/docs/assets/banner.png"
        )

        buttons = self.bot.rest.build_action_row()
        buttons.add_button(hikari.ButtonStyle.LINK, self.bot.invite_url).set_label(
            "Invite"
        ).set_emoji(981281185630134282).add_to_container()
        buttons.add_button(
            hikari.ButtonStyle.LINK, "https://sarthhh.github.io/anya"
        ).set_label("Docs").set_emoji(981281950255964170).add_to_container()
        await context.respond(embed=embed, reply=True, component=buttons)
        return await super().send_bot_help(context)

    async def send_command_help(
        self, context: lightbulb.Context, command: lightbulb.Command
    ) -> None:
        desc = f"```ini\n[{command.description} ]\n```\n"
        embed = (
            hikari.Embed(
                color=self.bot.colors.peach_yellow,
                description=desc + t.cast(str, inspect.getdoc(command.callback)),
            )
            .set_author(name=f"{command.name.upper()} COMMAND")
            .set_thumbnail(self.bot.get_me().avatar_url)  # type: ignore
            .set_footer(
                f"Requested by {context.author}", icon=context.author.avatar_url
            )
        )
        await context.respond(embed=embed, reply=True)
        return await super().send_command_help(context, command)

    async def send_group_help(self, context: lightbulb.Context, group) -> None:
        return await super().send_group_help(context, group)

    async def send_plugin_help(
        self, context: lightbulb.Context, plugin: lightbulb.Plugin
    ) -> None:
        return await super().send_plugin_help(context, plugin)


def load(bot: Bot) -> None:
    bot.help_command = Help(bot)


def unload(bot: Bot) -> None:
    ...
