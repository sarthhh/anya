import asyncio
from io import BytesIO

import hikari
from PIL import Image  # type: ignore


class GreetingImage:
    @staticmethod
    async def prepare_image_bytes(
        attachment: hikari.Attachment, guild_id: int
    ) -> bytes:
        """Preparing resized bytes for the Attachment object.

        Parameters
        ----------

            attachment: :class:`hikari.Attachment`
                The attachment resize to build bytes for.
            guild_id: :class:`int`
                ID of the server related to this trigger.

        Returns
        -------

            class:`bytes`

        """
        loop = asyncio.get_event_loop()
        byted = await loop.run_in_executor(
            None, GreetingImage._pillow_conversion, (await attachment.read()), guild_id
        )
        return byted

    @staticmethod
    def _pillow_conversion(initial_bytes: bytes, guild_id: int) -> bytes:
        b_io = BytesIO(initial_bytes)
        Image.open(b_io).save(f"image{guild_id}.png")  # saving initial bytes to a file

        image = (
            Image.open(f"image{guild_id}.png").convert("RGB").resize((500, 200))
        )  # change file size and baseformat.
        image.save(f"image{guild_id}.png")
        new_b_io = BytesIO()
        image = Image.open(f"image{guild_id}.png")
        image.save(new_b_io, "PNG")
        return new_b_io.getvalue()
