import os
import discord

# intents
intents = discord.Intents.default()
intents.messages = True
intents.typing = False
intents.presences = False

# client
client = discord.Client(intents=intents)


# print when active
@client.event
async def on_ready():
  print('discord version: ' + discord.__version__)
  print('Ready!')


# send message to DM on bookmark emoji reaction
@client.event
async def on_raw_reaction_add(payload):
  # if bookmark emoji
  if str(payload.emoji) == '🔖':
    guild = client.get_guild(payload.guild_id)
    # channel for bot post
    channel = client.get_channel(payload.channel_id)
    emoji = payload.emoji
    # member that reacted
    reactor = payload.member
    # message that was reacted
    message = await channel.fetch_message(payload.message_id)
    if channel is not None:
      # send message in channel
      # mention reactor and message poster
      # link to message
      await channel.send(reactor.mention + ' bookmarked ' +
                         message.author.mention + ' message ' +
                         message.jump_url)
      # send message to DM
      # link to message
      # message content
      await reactor.send('hello, you bookmarked ' + message.jump_url + '\n' +
                         message.content)


# run client
client.run(os.environ['DISCORD_BOT'])
