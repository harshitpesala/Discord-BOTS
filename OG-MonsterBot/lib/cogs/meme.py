import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
import random
import praw

class MemeBot(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def meme(self,ctx, subred = "funny"):
		with open("./data/memedata/client_id.0", "r", encoding = "utf-8") as ci:
			client_id = ci.read()

		with open("./data/memedata/client_secret.0", "r", encoding = "utf-8") as cs:
			client_secret = cs.read()

		with open("./data/memedata/username.0", "r", encoding = "utf-8") as u:
			username = u.read()

		with open("./data/memedata/password.0", "r", encoding = "utf-8") as p:
			password = p.read()

		with open("./data/memedata/user_agent.0", "r", encoding = "utf-8") as ua:
			user_agent = ua.read()

		reddit = praw.Reddit(client_id = client_id,
					 	 client_secret = client_secret,
					     username = username,
					     password = password,
					     user_agent = user_agent)

		subreddit = reddit.subreddit(subred + "memes")

		top = subreddit.top(limit = 50)
		hot = subreddit.hot(limit=50)

		posts = []

		for post in hot:
			posts.append(post)

		meme = random.choice(posts)

		posts.clear()

		meme_title = meme.title
		meme_image = meme.url

		em = discord.Embed(title = meme_title)
		em.set_image(url = meme_image)

		await ctx.send(embed = em)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("meme")


def setup(bot):
	bot.add_cog(MemeBot(bot))