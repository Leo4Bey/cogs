import discord
from discord.ext import commands
from discord import app_commands


class merhaba(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="merhaba", description="size selam verir")
    async def merhaba(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Merhaba {interaction.user.mention}")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(merhaba(bot))