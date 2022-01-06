import discord
import os
import ifpachamps
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

help_message = '''I am the IFPA NACS State and Provincial Championship Bot.  Type $ifpachamps followed by the following two inputs:
* Two-Letter State or Province Code
* Year
I will attempt to return the top 32 players for the year requested.
Example: $ipfachamps PA 2022'''

# instantiate IFPAChampsStandings
ifpa_champs = ifpachamps.IFPAChampsStandings()

@client.event
async def on_ready():
  print(f'{client.user} is now online!')

@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  if message.content.startswith(f'$ifpahelp'):
    await message.channel.send(help_message)
  
  if f'$ifpachamps' in message_content:

    key_words, search_words, full_url = ifpa_champs.key_words_search_words(message_content)
    standings_data = ifpa_champs.search(key_words)
    
    await message.channel.send(f"I searched for '{search_words}'. I looked at this page for standings: {full_url}")
    if len(search_words) > 0:
      await message.channel.send(f"```\n{standings_data}\n```")
    else:
      await message.channel.send(help_message)
    await message.channel.send(f"I am version 1.0 of this bot.  https://github.com/coreyhulse/IFPAChampionshipStandings")

#This is where your Discord token will go
client.run(os.environ['TOKEN'])