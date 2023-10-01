# Lollipop the Frog
Simple Discord chat bot. Rolls DnD ability checks for self, picks the Winner of the Day. Is sassy.
<br><br>
Based on Lollipop a frog created by Find Familiar spell in DnD Team Trouble compaign.

## Install
Use IDA, preferably PyCharm or VSCode. <br>
Have Python interpeter 3.11 or higher. <br>
Create bot account following [this official guide](https://discordpy.readthedocs.io/en/stable/discord.html) :  <br>
Clone the project. Add secrets.py to main folder next to main.py and create a variable BOT_TOKEN with your bot's token as a string. <br>
Now you are ready to go!

## How to Use
Once you added Lollipop to your server you can start using **commands**: <br>
> $$help - Shows list of commands  
> $$hello - Lollipop says hi.  
> $$introduce - Lollipop makes an introduction of self.  
> $$pick_winner - Picks the Winner of the Day out of members on a server(including self). Has 40% chance to assign a special power.  
### Rolls
> $$roll_d20 - Rolls d20
### Ability checks/saving-throws 
> $$roll_str - Rolls strength check  
> $$roll_dex - Rolls dexterity check  
> $$roll_con - Rolls constitution check  
> $$roll_int - Rolls intelligence check  
> $$roll_wis - Rolls wisdom check  
> $$roll_cha - Rolls charisma check  
### Skill checks
> Strength
> $$roll_athletics - Rolls athletics check
> <br>
> Dexterity  
> $$roll_acrobatics - Rolls acrobatics check  
> $$roll_sleight_of_hand - Rolls sleight of hand check  
> $$roll_stealth - Rolls stealth check
> <br>
> Intelligence  
> $$roll_arcana - Rolls arcana check  
> $$roll_history - Rolls history check  
> $$roll_investigation - Rolls investigation check  
> $$roll_nature - Rolls nature check  
> $$roll_religion - Rolls religion check  
> $$roll_animal_handling - Rolls animal handling check  
> $$roll_insight - Rolls insight check  
> $$roll_medicine - Rolls medicine check
> <br>
> Wisdom  
> $$roll_perception - Rolls perception check  
> $$roll_survival - Rolls survival check
> <br>
> Charisma  
> $$roll_deception - Rolls deception check  
> $$roll_intimidation - Rolls intimidation check  
> $$roll_performance - Rolls performance check  
> $$roll_persuasion - Rolls persuasion check  

## Additional features
* Lollipop croaks. 1% chance to croak between words, 10% chance to croak at the end of a message.
* When somebody types "99!" in chat, Lollipop references tv-show Brooklyn 99, because she simply can't resist.
