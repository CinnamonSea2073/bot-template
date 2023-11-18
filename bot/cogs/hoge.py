import discord
from discord.ext import commands 
from discord.commands import Option, OptionChoice, SlashCommandGroup

# クラス名にCogと付けたほうが分かりやすい
class HogeCog(commands.Cog):

    def __init__(self, bot:commands.bot):
        print(f"init -> {self.__class__}")
        self.bot = bot

    # nameは全て小文字
    group = SlashCommandGroup(name="name", description="description")

    # コマンド名は全て小文字。関数名の重複に注意。
    @group.command(name="ping", description="通信テスト")
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.response.send_message(content="pong!")

def setup(bot: commands.bot):
    bot.add_cog(HogeCog(bot))