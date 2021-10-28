import discord

import asyncio
import random

from dotenv import load_dotenv
import os

# --------------------- SETUP --------------------- #

intents = discord.Intents.default()
client = discord.Bot(intents=intents)
load_dotenv()

# you can replace None with a list of server-IDs, to make the commands instantly available there
# example: guild_ids = [123456789, 987654321]
guild_ids = None

gibby_messages = ["My Mom thinks I'm awesome!",
                  "AHHHH! Don't! I'm just a Gibby!",
                  "I'm the Statue of Gibberty!",
                  "I couldn't find the tube!",
                  "What am I? A mushroom?",
                  "What are you? A cop?",
                  "This pudding rocks!",
                  "Wow... umm. I'm in love with this sauce. What is it?",
                  "I invented cheesecake!",
                  "Oh really? I have that too!"]


# --------------------- SLASH COMMANDS --------------------- #

@client.slash_command(guild_ids=guild_ids, name='gibby', description='gibby')
async def gibby(ctx):
    rand_int = random.randint(0, 6)

    await ctx.respond(f'https://edge.baxtmann.me/{rand_int}.gif')


@client.slash_command(guild_ids=guild_ids, name='heygibby', description='hey gibby')
async def heygibby(ctx):
    rand = random.randint(0, len(gibby_messages) - 1)

    await ctx.respond(gibby_messages[rand])


@client.slash_command(guild_ids=guild_ids, name='gibbytalk', description='gibby talk')
async def gibbytalk(ctx):
    await ctx.respond("Gibby is ready to unleash notification hell!")

    # spam a random gibby message
    for x in range(50):
        rand_spam = random.randint(0, len(gibby_messages) - 1)
        msg = gibby_messages[rand_spam]

        await ctx.channel.send(msg)

        # wait a few seconds
        await asyncio.sleep(5)


# --------------------- EVENTS --------------------- #

@client.event
async def on_message(message: discord.Message):
    if not message.guild or message.author == client.user:
        return

    if str(message.content).lower() == "who is your daddy":
        await message.channel.send("It's Brandon Axtmann! https://baxtmann.me")
        return

    # gibby replies to spencer quotes
    content = str(message.content).lower()
    reply = None

    if content == "well too bad! stairs, stairs, stairs!":
        reply = "Stairs! Stairs! Stairs!"
    elif content == "you're grounded for... till college!":
        reply = "But.. that'll be like 50 years!"
    elif content == "haha, look! his arm came off!":
        reply = "Woah! My arm looks funny when its not on my body!"
    elif content == "why? is santa clause here to tell me i'm ugly and have no freinds?":
        reply = "No, he's here to take all your butter..."
    elif content == "don't say pie for breakfast, say pie for breakfast!":
        reply = "CHEESECAKE FOR BREAKFAST!"
    elif content == "i once met a freaky rabi in vegas.":
        reply = "I once met my moms boyfreind... my dad didn't seem to like him. "
    elif content == "look, in my life, i've learned a few things about girls. like, when you break up with them, they do not like it when you ask out their sisters. that will get you a fork in your arm.":
        reply = "What about if you date their mom? "
    elif content == "i told you to breathe through the tube! oh wait... i forgot the tube.":
        reply = "*gasp* *gibby dies*"
    elif content == "she has magic feet!":
        reply = "Woah! They are magic!"
    elif content == "those thalia-manians taught you good.":
        reply = "Spending two years with them really was a good decision!"
    elif content == "toasty!":
        reply = "Buttery!"
    elif content == "don't worry, toasty. soon you'll be back and butter than ever!":
        reply = "Hey spencer... can I use toasty on my bagel?"
    elif content == "so? it's a pie shop, not a church.":
        reply = "The only thing I worship is CHEESECAKE!"
    elif content == "i made it into a squirrel":
        reply = "I made a squirrel into a squirrel!"
    elif content == "it's not just that. last week on a bus, a hobo spilled chili on me, then continuted to eat it... without a spoon!":
        reply = "Did he share the chili?"
    elif content == "behold the sign! are you beholding it?":
        reply = "I am beholding it!!"
    elif content == "well, i'm cooking/i'm cooking things/cooking things for people to eat/i'm cooking/i'm cooking things/things that people will chew.":
        reply = "Hey Spencer, don't you need food if you want to cook? Your just stirring sand in a  frying pan..."
    elif content == "if you're looking for a fun creative guy, well, you just took a right turn down lucky street. why don't you go ahead and put it in park? send me an email. write it, click it, send it...":
        reply = "Come here and give me a big kiss you beatiful guy!"

    if reply is not None:
        await message.channel.send(reply)


@client.event
async def on_ready():
    print('Logged in as:')
    print(" Username:", client.user.name)
    print(" ID:", client.user.id)
    print("To invite the bot in your server use this link:\n https://discord.com/api/oauth2/authorize?client_id" + str(
        client.user.id) + "&permissions=2147518464&scope=bot%20applications.commands")


# --------------------- RUN --------------------- #

if __name__ == "__main__":
    client.run(os.getenv('GIBBY_TOKEN'))
