import random


class Lollipop:
    name = "Lollipop"
    introduction = [
        "I'm Lollipop, the only reason I want a boyfriend is \n"
        "so that when I'm signing Fergalicious and it's at the part \n"
        "where she says *I be up in gym just workin on my fitness \n"
        "he's my witness* I can point to him and he'll do the little \n"
        "*wooOOH* part, because right now I have to do both parts \n"
        "myself and it's stressful, because right after the *wooOOH*\n"
        "part I have to get right back into rapping and the transition\n"
        "is harder than you think.",

        "Sup, name's Lollipop. IDK about this whole *adventuring* thing \n"
        "all I want is some chipotle out of this deal",

        "Heyo, I'm Lollipop. \n"
        "No, I'm not edible.\n"
        "Yes, I'm poisonous. \n"
        "No, you won't get high from licking me, you'll just get sick, you weirdo\n",
    ]

    def introduce(self):

        return random.choice(self.introduction)


class LollipopFrog(Lollipop):
    name = "Lollipop the Frog"

    AC = 11
    HP = 1

    # Basic Attribute Modifiers
    str = -5
    dex = 1
    con = -1
    int = -5
    wis = -1
    cha = -4

    # Skill Modifiers

    # Strength
    athletics = str

    # Dexterity
    acrobatics = dex
    sleight_of_hand = dex
    stealth = dex + 3

    # Intelligence
    arcana = int
    history = int
    investigation = int
    nature = int
    religion = int

    # Wisdom
    animal_handling = wis
    insight = wis
    medicine = wis
    perception = wis + 1
    survival = wis

    # Charisma
    deception = cha
    intimidation = cha
    performance = cha
    persuasion = cha

    def frog_filter(self, text):
        """
        Takes a string and adds croaks.
        1% chance between words, 10% at the end of a string
        """
        ribbit_list = [
            "*Ribbit!*",
            "*riBBit!*",
            "*Reeeebit!*",
            "*Croak!*",
        ]
        result = ""
        for letter in text:
            if letter == " ":
                if random.randint(1, 100) == 1:
                    result += " " + random.choice(ribbit_list) + " "
                else:
                    result += letter
            else:
                result += letter

        if random.randint(1, 100) <= 10:
            result += " " + random.choice(ribbit_list) + " "

        return result

    def introduce(self):
        return self.frog_filter(random.choice(self.introduction))

    def roll20(self, modifier: int = 0):
        result = random.randint(1, 20)
        if modifier == 0:
            talk = f"I rolled {result}"
        else:
            if modifier > 0:
                mod_string = f"+ {modifier}"
            else:
                mod_string = f"- {str(modifier * -1)}"

            talk = f"I rolled {result} {mod_string} \n" \
                   f"So it's {result + modifier}"
            talk = self.frog_filter(talk)
        return talk

    def send_brooklyn_99(self):
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            'Cool. Cool cool cool cool cool cool cool, \n'
            'no doubt no doubt no doubt no doubt.',
        ]
        return self.frog_filter(random.choice(brooklyn_99_quotes))

    def say_hi(self, human_name="you"):
        human_name = human_name.capitalize()

        if human_name.lower() == "biorival":
            reply_list = [
                f"Heya, Maggee, looking good today, Master! :star_struck:",
                f"Hi Maggee :) \nI'm ready to croak'n'roll",
                f"Heyo {human_name}! You are the best! :sunglasses:",
            ]
        elif human_name.lower() == "deathlaide":
            reply_list = [
                f"Sup Willow, your pockets smell funny",
                f"Hello {human_name}, my favorite goth clown :clown:",
                f"Heyo {human_name}! :frog:",
            ]
        elif human_name.lower() == "danhob":
            reply_list = [
                f"Hello Hein, let your arrows strike true! :archery:",
                f"Hi :clap: {human_name} :clap: good :clap: to :clap: see :clap: you!",
                f"How's it rolling {human_name}?",
            ]
        elif human_name.lower() == "i have no mouth" or human_name.lower() == "i want to sleep":
            reply_list = [
                f"Well, well, well, isn't this Daso",
                f"Hello Daso *the rock* Halat",
                f"Hi {human_name}, weird name",
            ]
        else:
            reply_list = [
                f"Hello {human_name}!",
                f"Sup {human_name}!",
                f"Heyo {human_name}! :frog:"
            ]

        reply = random.choice(reply_list)
        reply = self.frog_filter(reply)

        return reply

    # Returns text with random special power
    def pick_power(self):
        power_list = [
            "\n**Swole Doge Spirit** \n\n"
            "Today you are stronger. You can do 1 more push-up than usual. When you flex in front of a mirror, "
            "the mirror flexes back. You are the muscle, you are the wall, you are swole doge incarnate!",

            "\n**Super Sonic** \n\n"
            "Today you are as fast as lighting, your reaction is superhuman. Your keyboard typing skills are better. "
            "You could write a book in one day, but the speed of your thought is not fast enough for your "
            "supra-agile hands. "
            "You have a higher chance at catching jelly beans with your mouth.",

            "\n**Bulletproof** \n\n"
            "Until the end of the day, you are immune to any high velocity shots fired at you (including verbal). "
            "You are impossible to hurt, unless somebody wedges a knife or something very slowly, like in that "
            "Dune movie. Go on, try it out! You are practically a god! \n\n"
            "*Disclaimer: \n"
            "Lollipop (as well as her creator) is not responsible for any injury the "
            "silly humans may inflict on themselves.",

            "\n**Aether Lenses** \n\n"
            "You are considerably smarter today. You have invisible lenses attached to your eyes, "
            "lenses are like glasses, but you don't look like a nerd. And everybody knows glasses make you smarter! "
            "Your plans work out. You can calculate first grade arithmetic flawlessly. Your logic is so accurate and"
            "methodical - it bends reality, whenever it is not.",

            "\n**Balls of Steel** \n\n"
            "Until midnight, you acquire cohones made of solid low carbon corrosion-resistant stainless steel. "
            "That fact makes you brave beyond measure. You can take on anybody, anywhere, anytime. "
            "You are Chuck. Fucking. Norris! You are HONEYBADGER of the human world! Nothing can make you afraid!",

            "\n**Blessing of the Obama** \n\n"
            "Today your charisma is off the charts. You are a rockstar! You can charm any girl, any guy, "
            "any toaster, and even any Dungeon Master, who will shower you in presents, because you are *sooo* cool. "
            "Also, you have an N-word pass, until midnight. Wreck havoc, you silver-tongued devil!",

            "\n**Silenced, But Whole** \n\n"
            "Today your farts are silent, nobody will hear them coming...",

            "\n**Lucky Multiverse Jumper** \n\n"
            "You might've not noticed, but you have blinked to another universe. This is the version, where your rolls "
            "are the best out of infinite possibilities (don't think about it). I already took care of the "
            "body of your other self, who was living in here (also, don't think about it). Also, in this universe "
            "the average [BODYPART_PLACEHOLDER] size is 2cm smaller (definitely, don't think about it)."
        ]

        result = random.choice(power_list)
        return self.frog_filter(result)

lol = LollipopFrog()

