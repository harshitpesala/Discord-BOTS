from asyncio import sleep
from discord import Intents
from glob import glob
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from discord.ext.commands.errors import MissingRequiredArgument
from apscheduler.triggers.cron import CronTrigger

from ..db import db

PREFIX = ">"

OWNER_IDS = [210351564018155521]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Ready(object):
	def __init__(self):
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		setattr(self, cog, True)
		print(f"{cog} cog ready")

	def all_ready(self):
		return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.cogs_ready = Ready()
		self.scheduler = AsyncIOScheduler()

		db.autosave(self.scheduler)
		super().__init__(
			command_prefix=PREFIX, 
			owner_ids=OWNER_IDS,
			intents = Intents.all()
		)

	def setup(self):
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f"{cog} cog loaded.")

		print("Setup Complete.")

	def run(self, version):
		self.VERSION = version

		print("Running setup....")
		self.setup()

		with open("./lib/bot/token.0", "r", encoding = "utf-8") as tf:
			self.TOKEN = tf.read()

		print("Running Bot....")
		super().run(self.TOKEN, reconnect=True)

	async def print_message(self):
		channel = self.get_channel(778192860343828511)
		await channel.send("I am a timed notification.")

	async def on_connect(self):
		print("Bot is connected.")

	async def on_disconnect(disconnect):
		print("Bot is disconnected")

	async def on_error(self, err, *args, **kwargs):
		if err == "on_command_error":
			await args[0].send("Something went wrong!")
			
		else:
			channel = self.get_channel(778192860343828511)
			await channel.send("A random error occured")
			
		raise
			
	async def on_command_error(self, ctx, exc):
		if isinstance(exc, CommandNotFound):
			await ctx.send("Sorry that command doesnt exist.")
			pass

		elif isinstance(exc, MissingRequiredArgument):
			pass

		else:
			raise exc

	async def on_ready(self):
		activity = discord.Activity(type=discord.ActivityType.listening, name="MONSTERFPV")
		await super().change_presence(status=discord.Status.online, activity=activity)



		if not self.ready:
			channel = self.get_channel(775654576761602050)
			await channel.send("Im online now!")

			while not self.cogs_ready.all_ready():
				await sleep(0.5)

			self.ready = True

			print("Bot is ready.")

		else:
			print("Bot reconnected.")


bot=Bot()