#!/usr/bin/env python3
import discord
import os
import asyncio
import config
from discord.ext import commands
import time
import datetime
import random

# Use ! to invoke custom bot commands (none implemented at this time)
bot = commands.Bot(command_prefix="!",pm_help=True, case_insensitive=True)
# removing default help command imported by discord python library
bot.remove_command("help")


@bot.event
async def on_message(message: discord.Message):
        # if not message.author.bot:
            if message.guild:
                if str(message.content).lower() == "gibby":
                    rand1 = random.randrange(0, 7)#setting range and generating random number
                    randstr = str(rand1)#converting int to string to we can add to url of gif
                    await message.channel.send("https://edge.baxtmann.me/"+(randstr)+".gif")#generates gif to display
                if str(message.content).lower() == "hey gibby":#when hey spencer is typed we will randomly generate a number and select a chat line to send to discord
                    rand = random.randrange(0, 11)#generating random number
                    if rand == 4:
                            await message.channel.send("My Mom thinks I'm awesome!")
                    if rand == 1:
                            await message.channel.send("AHHHH! Don't! I'm just a Gibby!")
                    if rand == 2:
                            await message.channel.send("I'm the Statue of Gibberty!")
                    if rand == 3:
                            await message.channel.send("I couldn't find the tube!")
                    if rand == 5:
                            await message.channel.send("What am I? A mushroom?")
                    if rand == 6:
                            await message.channel.send("What are you? A cop?")
                    if rand == 7:
                            await message.channel.send("This pudding rocks!")
                    if rand == 8:
                            await message.channel.send("Wow... umm. I'm in love with this sauce. What is it?")
                    if rand == 9:
                            await message.channel.send("I invented cheesecake!")
                    if rand == 10:
                            await message.channel.send("Oh really? I have that too!")
                if str(message.content).lower() == "who is your daddy":
                            await message.channel.send("It's Brandon Axtmann! https://baxtmann.me")
                if str(message.content).lower() == "gibby talk":
                            await message.channel.send("Gibby is ready to unleash notification hell!")
                            for x in range(50):#this will loop spenver chats spam responces 50 times
                                randSpam = random.randrange(0, 11)#generating random number to randomly choose spencer chat line
                                if randSpam == 4:
                                        await message.channel.send("My Mom thinks I'm awesome!")
                                if randSpam == 1:
                                        await message.channel.send("AHHHH! Don't! I'm just a Gibby!")
                                if randSpam == 2:
                                        await message.channel.send("I'm the Statue of Gibberty!")
                                if randSpam == 3:
                                        await message.channel.send("I couldn't find the tube!")
                                if randSpam == 5:
                                        await message.channel.send("What am I? A mushroom?")
                                if randSpam == 6:
                                        await message.channel.send("What are you? A cop?")
                                if randSpam == 7:
                                        await message.channel.send("This pudding rocks!")
                                if randSpam == 8:
                                        await message.channel.send("Wow... umm. I'm in love with this sauce. What is it?")
                                if randSpam == 9:
                                        await message.channel.send("I invented cheesecake!")
                                if randSpam == 10:
                                        await message.channel.send("Oh really? I have that too!")
                                time.sleep(10)#tell loop to sleep for 10s so it doesnt go to fast/so discord cant give us shit for being a spam bot
                #reactions for when hey gibby is triggered - when gibby says one of his quotes, spencer will respond based on what gibby says
                if str(message.content).lower() == "well too bad! stairs, stairs, stairs!":
                        await message.channel.send("Stairs! Stairs! Stairs!")
                if str(message.content).lower() == "you're grounded for... till college!":
                        await message.channel.send("But.. that'll be like 50 years!")
                if str(message.content).lower() == "haha, look! his arm came off!":
                        await message.channel.send("Woah! My arm looks funny when its not on my body!")
                if str(message.content).lower() == "why? is santa clause here to tell me I'm ugly and have no freinds?":
                        await message.channel.send("No, he's here to take all your butter...")
                if str(message.content).lower() == "don't say pie for breakfast, say pie for breakfast!":
                        await message.channel.send("CHEESECAKE FOR BREAKFAST!")
                if str(message.content).lower() == "i once met a freaky rabi in vegas.":
                        await message.channel.send("I once met my moms boyfreind... my dad didn't seem to like him. ")
                if str(message.content).lower() == "look, in my life, i've learned a few things about girls. like, when you break up with them, they do not like it when you ask out their sisters. that will get you a fork in your arm.":
                        await message.channel.send("What about if you date their mom? ")
                if str(message.content).lower() == "i told you to breathe through the tube! oh wait... i forgot the tube.":
                        await message.channel.send("*gasp* *gibby dies*")
                if str(message.content).lower() == "she has magic feet!":
                        await message.channel.send("Woah! They are magic!")
                if str(message.content).lower() == "those thalia-manians taught you good.":
                        await message.channel.send("Spending two years with them really was a good decision!")
                if str(message.content).lower() == "toasty!":
                        await message.channel.send("Buttery!")
                if str(message.content).lower() == "don't worry, toasty. soon you'll be back and butter than ever!":
                        await message.channel.send("Hey spencer... can I use toasty on my bagel?")
                if str(message.content).lower() == "so? it's a pie shop, not a church.":
                        await message.channel.send("The only thing I worship is CHEESECAKE!")
                if str(message.content).lower() == "i made it into a squirrel":
                        await message.channel.send("I made a squirrel into a squirrel!")
                if str(message.content).lower() == "it's not just that. last week on a bus, a hobo spilled chili on me, then continuted to eat it... without a spoon!":
                        await message.channel.send("Did he share the chili?")
                if str(message.content).lower() == "behold the sign! Are you beholding it?":
                        await message.channel.send("I am beholding it!!")
                if str(message.content).lower() == "well, i'm cooking/i'm cooking things/cooking things for people to eat/i'm cooking/i'm cooking things/things that people will chew.":
                        await message.channel.send("Hey Spencer, don't you need food if you want to cook? Your just stirring sand in a  frying pan...")
                if str(message.content).lower() == "if you're looking for a fun creative guy, well, you just took a right turn down lucky street. why don't you go ahead and put it in park? send me an email. write it, click it, send it...":
                        await message.channel.send("Come here and give me a big kiss you beatiful guy!")

@bot.event
async def on_ready():
    print('\nLogged in as:')#debug info stated when bot starts in cli
    print(" Username",bot.user.name)
    print(" User ID",bot.user.id)
    print("To invite the bot in your server use this link:\n https://discordapp.com/oauth2/authorize?&client_id="+str(bot.user.id)+"&scope=bot&permissions=0")

def run_client(token):
    global bot
    
    print("Starting at time",str(datetime.datetime.now()))
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bot.start(token))
    except Exception as e:
        print("Error", e)
        loop.run_until_complete(bot.logout())
        
if __name__ == "__main__":
            
    run_client(config.discordtoken)
