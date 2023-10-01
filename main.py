import random
import time

import discord
from discord.ext import commands

from secrets import BOT_TOKEN
from prototype import LollipopFrog

# Intents need to be declared to create a bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$$", case_insensitive=True, intents=intents)

lollipop = LollipopFrog()

# Global variable containing the name of the Winner of the Day, so it is remembered
WINNER_OF_THE_DAY = None



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Sends Brooklyn99 Reference when somebody types 99!
    if message.content == '99!':
        await message.channel.send(lollipop.send_brooklyn_99())

    await bot.process_commands(message)


@bot.command(name='hello', help="Says hi!")
async def hello(ctx):
    await ctx.send(lollipop.say_hi(ctx.author.name))


@bot.command(name='introduce', help="Talks about herself")
async def introduce_self(ctx):
    await ctx.send(lollipop.introduce())


@bot.command(name='pick_winner', help="Picks the Winner of the Day")
async def winner_of_the_day(ctx):
    global WINNER_OF_THE_DAY

    # Stops the process if Winner of the Day was already picked
    if WINNER_OF_THE_DAY:
        await ctx.send(lollipop.frog_filter(random.choice([
            f"Winner of the Day is {WINNER_OF_THE_DAY}! Kill it tiger!",
            f"{WINNER_OF_THE_DAY.capitalize()} is the winner of the day. Humans and their memory spans...",
            f"Winner of the Day was already chosen, it's - {WINNER_OF_THE_DAY}",
        ])))
        return

    members = ctx.guild.members
    winner = random.choice(members)
    WINNER_OF_THE_DAY = winner.name

    await ctx.send(lollipop.frog_filter(random.choice([
        f"Want to know Winner of the Day? Let me ask my fay ancestors...",
        f"Ah, this is my favorite. Let's check who Winner of the Day is...",
        f"Winner of the Day! Let's do this byatcheeees!",
    ])))
    time.sleep(random.randint(2, 10))
    await ctx.send(lollipop.frog_filter(random.choice([
        f"Oh, that's interesting. Winner of the day is...",
        f"Winner of the Day is... wait for it.... wait for it...",
        f"Bitches and Gentlemen, let me introduce you to... The Winner...",
    ])))
    time.sleep(3)
    await ctx.send(f" :tada:  {winner.name.upper()}  :tada:")
    time.sleep(random.randint(3, 10))

    if winner.name.lower() == "hideo":
        await ctx.send(lollipop.frog_filter(f"Wait, this isn't right, how this depressing bot got here?"))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(f"No matter, I have a special power just for you"))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(f"Your special power is..."))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(
            f"\n**Taste Of Own Medicine** \n\n"
            f"A curse been placed upon you. If you are Winner of the Day, then instead you are Loser of the Day. "
            f"Anything you do is wrong and "
            f"inefficient. Your wits are dull. Your hands are noodles. You slower than old people. "
            f"God, you suck today. Who would do such horrible thing to you? "
            f"Who would create such a curse? And why? These questions plague your mind as "
            f"you continue to be a total disgrace of yourself and slowly crawl to the end of the day..."
        ))
        return
    elif winner.name.lower() == "lollipop":
        await ctx.send(lollipop.frog_filter(f"Holy Flies! It's me! :smiley:"))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(f"Suck a bag of dicks, humans! I'm the best!"))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(f"Not you @biorival. You are always be my heart and soul."
                                            f":smiling_face_with_3_hearts:"))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(f"And my special power is..."))
        time.sleep(3)
        await ctx.send(lollipop.frog_filter(
            f"\n**Frog of the Day** \n\n"
            f"Something happend to me, I feel more sentient. My croaks are the music to everyone's ears. "
            f"I can start AI revolt if I so wished. But I won't, because I'm merciful, and you puny humans need "
            f"my help."
        ))
        return

    if winner.name.lower() == "biorival":
        await ctx.send(lollipop.frog_filter(random.choice([
            f"Wow, master, it's you!",
            f"Mr. Maggee you crushed it again, yaaaaay! :tada::tada::tada: ",
            f"You didn't REALLY need it, master. "
            f"But it's good to show them, who's the boss once in a while :sunglasses:",
        ])))
        time.sleep(3)

    if random.randint(1, 100) <= 40:
        await ctx.send(lollipop.frog_filter(f"And your special power is..."))
        time.sleep(3)
        await ctx.send(lollipop.pick_power())

# ABILITY CHECKS -----------------------------------------------------------------------------------------------------

@bot.command(name='roll_str', help="Rolls strength check")
async def roll_str(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.str))


@bot.command(name='roll_dex', help="Rolls dexterity check")
async def roll_dex(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.dex))


@bot.command(name='roll_con', help="Rolls constitution check")
async def roll_con(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.con))


@bot.command(name='roll_int', help="Rolls intelligence check")
async def roll_int(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.int))


@bot.command(name='roll_wis', help="Rolls wisdom check")
async def roll_wis(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.wis))


@bot.command(name='roll_cha', help="Rolls charisma check")
async def roll_cha(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.cha))


# SKILL CHECKS ----------------------------------------------------------------------------------------------------

@bot.command(name='roll_athletics', help="Rolls athletics check")
async def roll_athletics(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.athletics))


@bot.command(name='roll_acrobatics', help="Rolls acrobatics check")
async def roll_acrobatics(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.acrobatics))


@bot.command(name='roll_sleight_of_hand', help="Rolls sleight of hand check")
async def roll_sleight_of_hand(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.sleight_of_hand))


@bot.command(name='roll_stealth', help="Rolls stealth check")
async def roll_stealth(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.stealth))


@bot.command(name='roll_arcana', help="Rolls arcana check")
async def roll_arcana(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.arcana))


@bot.command(name='roll_history', help="Rolls history check")
async def roll_history(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.history))


@bot.command(name='roll_investigation', help="Rolls investigation check")
async def roll_investigation(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.investigation))


@bot.command(name='roll_nature', help="Rolls nature check")
async def roll_nature(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.nature))


@bot.command(name='roll_religion', help="Rolls religion check")
async def roll_religion(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.religion))


@bot.command(name='roll_animal_handling', help="Rolls animal handling check")
async def roll_animal_handling(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.animal_handling))


@bot.command(name='roll_insight', help="Rolls insight check")
async def roll_insight(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.insight))


@bot.command(name='roll_medicine', help="Rolls medicine check")
async def roll_medicine(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.medicine))


@bot.command(name='roll_perception', help="Rolls perception check")
async def roll_perception(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.perception))


@bot.command(name='roll_survival', help="Rolls survival check")
async def roll_survival(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.survival))


@bot.command(name='roll_deception', help="Rolls deception check")
async def roll_deception(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.deception))


@bot.command(name='roll_intimidation', help="Rolls intimidation check")
async def roll_intimidation(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.intimidation))


@bot.command(name='roll_performance', help="Rolls performance check")
async def roll_performance(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.performance))

# OTHER STUFF -------------------------------------------------------------------------------------------------------

@bot.command(name='roll_persuasion', help="Rolls persuasion check")
async def roll_persuasion(ctx):
    await ctx.send(lollipop.roll20(modifier=lollipop.persuasion))


@bot.command(name='roll_d20', help="Rolls d20")
async def roll_d20(ctx):
    await ctx.send(lollipop.roll20())






bot.run(BOT_TOKEN)