import typing as t

__all__: t.Tuple[str, ...] = (
    "ANSIEnums",
    "ANSIBuilder",
)


class ANSIEnums:
    """Enums for the ANSIBuilder."""

    BASE: t.ClassVar = "\033"
    RESET: t.ClassVar = "[0m"
    NORMAL_FORMAT: t.ClassVar = 0
    BOLD_FORMAT: t.ClassVar = 1
    UNDERLINE_FORMAT: t.ClassVar = 4
    GRAY_TEXT: t.ClassVar = 30
    RED_TEXT: t.ClassVar = 31
    GREEN_TEXT: t.ClassVar = 32
    YELLOW_TEXT: t.ClassVar = 33
    BLUE_TEXT: t.ClassVar = 34
    PINK_TEXT: t.ClassVar = 35
    CYAN_TEXT: t.ClassVar = 36
    WHITE_TEXT: t.ClassVar = 37
    FIREFLY_DARK_BLUE_BACKGROUND: t.ClassVar = 40
    ORANGE_BACKGROUND: t.ClassVar = 41
    MARBLE_BLUE_BACKGROUND: t.ClassVar = 42
    GREYISH_TURQUOISE_BACKGROUND: t.ClassVar = 43
    GRAY_BACKGROUND: t.ClassVar = 44
    INDIGO_BACKGROUND: t.ClassVar = 45
    LIGHT_GRAY_BACKGROUND: t.ClassVar = 46
    WHITE_BACKGROUND: t.ClassVar = 0


class ANSIBuilder:
    """
    This class is used to construct an ANSI codeblock for discord.
    """

    def __init__(
        self,
    ) -> None:
        self._bucket: t.List[str] = []

    def __enter__(self) -> "ANSIBuilder":
        return self.new()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        ...

    def new(self) -> "ANSIBuilder":
        """Clears all old components and creates a fresh Builder

        Returns
        -------

            :class:`ANSIBuilder`

        """
        self._bucket.clear()
        return self

    def set_format(
        self, *, background: int = 0, text_color: int, format: int = 0
    ) -> "ANSIBuilder":
        """
        Set format for the appearing ANSI text.

        Parameters
        ----------

            background: :class:`int`
                The background of the text.
            text_color: :class:`int`
                Color of the text.
            format: :class:`int`
                Text Style.

        Returns
        -------

            :class:`ANSIBuilder`


        """
        self._bucket.append(f"{ANSIEnums.BASE}[{format};{background};{text_color}m")
        return self

    def reset(self) -> "ANSIBuilder":
        """Removes ANSI effects from the builder

        Returns
        -------

            :class:`ANSIBuilder`

        """
        self._bucket.append(f"{ANSIEnums.BASE}{ANSIEnums.RESET}")
        return self

    def add_text(self, text: str, /) -> "ANSIBuilder":
        """
        Add text to the builder.

        Parameters
        ----------

            text: :class:`str`
                The text to add in the next lines.

        Returns
        -------

            :class:`ANSIBuilder`

        """
        self._bucket.append(str(text))
        return self

    def build(self) -> str:
        """
        Returns the ANSI string build yet as a normal string.

        Returns
        -------

            :class:`str`

        """
        self._bucket.append(f"{ANSIEnums.BASE}{ANSIEnums.RESET}")
        return "".join(self._bucket)

    def build_as_codeblock(self) -> str:
        """
        Returns the ANSI string build yet as a code block.

        Returns
        -------

            :class:`str`

        """
        self._bucket.append(f"{ANSIEnums.BASE}{ANSIEnums.RESET}")
        return f"```ansi\n{''.join(self._bucket)}\n```"
