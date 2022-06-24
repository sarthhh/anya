from __future__ import annotations

import typing as t

import lightbulb

__all__: t.Tuple[str, ...] = ("DoNothing", "NoChannelSetup", "InvalidChoice")


class DoNothing(BaseException):
    """Dummy exception where the handler should not handle the errors"""


class NoChannelSetup(BaseException):
    """
    This exception is raised when a user tries to setup logging elements
    without setting up logging channel.

    Paramaters
    ----------

        context: :class:`t.Union[lightbulb.PrefixContext, lightbulb.SlashContext]`
            The context which raised this exception.
        message: :class:`str`
            The error message.

    """

    def __init__(
        self, context: lightbulb.PrefixContext | lightbulb.SlashContext, message: str
    ) -> None:
        self.context = context
        super().__init__(message)


class InvalidChoice(BaseException):
    """
    This exception is raised when user enters an invalid choice for
    a prefix command option.

    Paramaters
    ----------

        context: :class:`t.Union[lightbulb.PrefixContext, lightbulb.SlashContext]`
            The context which raised this exception.
        message: :class:`str`
            The error message.

    """

    def __init__(
        self,
        context: lightbulb.PrefixContext | lightbulb.SlashContext,
        option: lightbulb.OptionLike,
        allowed: t.Tuple[str, ...],
        message: str,
    ) -> None:
        self.option = option
        self.allowed_options = allowed
        self.context = context
        super().__init__(message)
