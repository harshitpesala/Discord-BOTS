import discord
from discord.ext.commands import Cog
from discord.ext.commands.errors import MissingRequiredArgument
from discord.ext.commands import command
import random

class Fun(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def roast(self, ctx, member:discord.Member):
		f = open("./data/fundata/roast_list.txt", "r")
		roastList = f.readlines()

		await ctx.send(f"{member.mention} {random.choice(roastList)}")

		f.close()

	@roast.error
	async def roast_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Please mention a member.")	

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("fun")

	@command()
	async def say(self, ctx, *, text):
		await ctx.message.delete()
		await ctx.send(f"{text}")


def setup(bot):
	bot.add_cog(Fun(bot))