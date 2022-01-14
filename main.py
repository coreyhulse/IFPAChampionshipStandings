import discord
import os
import ifpachamps
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

help_message = '''I am the IFPA NACS & WNACS State and Provincial Championship Bot.  

Type $ifpachamps_nacs or $ifpachamps_wnacs followed by the following two inputs:
* Two-Letter State or Province Code
* Year

I will attempt to return the top 32 players for the year requested.
Example: $ipfachamps_nacs PA 2022
Example: $ipfachamps_wnacs PA 2022

The Womens standings relies on a lookup table stored in my GitHub repository.  If you see a state missing please log an issue on GitHub:
https://github.com/coreyhulse/IFPAChampionshipStandings
'''

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
  message_content = message.content.upper()  

  if f'$IFPAHELP' in message_content:
    await message.channel.send(help_message)
  
  if f'$IFPACHAMPS_NACS' in message_content:

    key_words, search_words, full_url = ifpa_champs.key_words_search_nacs(message_content)
    standings_data = ifpa_champs.search_nacs(key_words)
    
    await message.channel.send(f"I searched for '{search_words}'. I looked at this page for standings: {full_url}")
    if len(search_words) > 0:
      await message.channel.send(f"```\n{standings_data}\n```")
    else:
      await message.channel.send(help_message)
    await message.channel.send(f"I am version 2.0 of this bot.  $ifpachamps_nacs or $ifpachamps_wnacs to see standings; $ifpahelp for info.")

  if f'$IFPACHAMPS_WNACS' in message_content:

    key_words, search_words, message_response, open_url, womens_url = ifpa_champs.key_words_search_wnacs(message_content)
    standings_data_open = ifpa_champs.search_wnacs(key_words, open_url)

    standings_data_women = ifpa_champs.search_wnacs(key_words, womens_url)
    
    # Open Standings
    await message.channel.send(f"I searched for WNACS Standings for '{search_words}'. {message_response}I looked at this page for Open standings: {open_url}")
    if len(search_words) > 0:
      await message.channel.send(f"```\n{standings_data_open}\n```")
          
    # Womens Standings
    await message.channel.send(f"I searched for WNACS Standings for '{search_words}'. {message_response}I looked at this page for Womens standings: {womens_url}")
    if len(search_words) > 0:
      await message.channel.send(f"```\n{standings_data_women}\n```")
    else:
      await message.channel.send(help_message)
    
    await message.channel.send(f"I am version 2.0 of this bot.  $ifpachamps_nacs or $ifpachamps_wnacs to see standings; $ifpahelp for info.")

#This is where your Discord token will go
client.run(os.environ['TOKEN'])