from discord.ext import commands


class Main(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, context):
        await context.send("Hello, World!")


# this is the command used by cogs to load up this file
def setup(bot):
    bot.add_cog(Main(bot))
