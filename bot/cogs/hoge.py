import discord
from discord.ext import commands 
from discord.commands import Option, OptionChoice, SlashCommandGroup


class Hoge(commands.Cog):

    def __init__(self, bot:commands.bot):
        print(f"init -> {self.__class__}")
        self.bot = bot

    group = SlashCommandGroup(name="name", description="description")

    @group.command(name="ping", description="通信テスト")
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.response.send_message(content="pong!")

def setup(bot: commands.bot):
    bot.add_cog(Hoge(bot))