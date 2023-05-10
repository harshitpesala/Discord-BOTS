import discord

from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix=">" , case_insensitive=True, intents=intents)

@client.event
async def on_ready():
	activity = discord.Activity(type=discord.ActivityType.listening, name="m0nster")
	await client.change_presence(status=discord.Status.online, activity=activity)
	print("MonsterBOTv2 is ready.")

cog_list = ["fun"]

for cog in cog_list:
	client.load_extension(f"cogs.{cog}")
	print(f"{cog} cog loaded succesfully")


with open("./data/bot_token/token.0", "r", encoding = "utf-8") as tf:
	TOKEN = tf.read()

client.run(TOKEN)