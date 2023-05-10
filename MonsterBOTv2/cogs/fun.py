import discord
from discord.ext import commands

import random

import praw

with open("./data/reddit_data/reddit_password.0", "r", encoding = "utf-8") as pf:
	reddit_password = pf.read()

with open("./data/reddit_data/reddit_client_id.0", "r", encoding = "utf-8") as cf:
	reddit_client_id = cf.read()

with open("./data/reddit_data/reddit_client_secret.0", "r", encoding = "utf-8") as sf:
	reddit_client_secret = sf.read()

reddit = praw.Reddit(client_id = reddit_client_id,
					 client_secret = reddit_client_id,
					 username = "harshit_pesala",
					 password = reddit_password,
			 		 user_agent = "MonsterBOT")


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def meme(self, ctx, subred = "memes"):
		subreddit = reddit.subreddit(subred)

		top = subreddit.top(limit = 10)

		all_posts = []

		for post in top:
			all_posts.append(post)

		random_post = random.choice(all_posts)

		name = random_post.title
		image = random_post.url

		em = discord.Embed(title = name)

		em.set_image(url = image)

		await ctx.send(embed = em)

	@commands.command()
	async def roast(self, ctx, member : discord.Member):
		r = open("./data/fundata/roast_list.txt","r")
		roastList = r.readlines()

		if member.mention == "<@775642982228819969>":
			await ctx.send(f"I can't roast myself, so joke is on you {ctx.message.author.mention}")

		elif member.mention == "<@210351564018155521>":
			await ctx.send(f"No.")

		else:
			await ctx.send(f"{member.mention} {random.choice(roastList)}")

		r.close()

def setup(bot):
	bot.add_cog(Fun(bot))