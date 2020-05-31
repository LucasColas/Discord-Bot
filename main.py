import discord
import Token

token = Token.read_token()

client = discord.Client()

@client.event
async def on_message(message):
    spec_channel = client.get_channel(427899196985704450)
    id = client.get_guild(325925436804825111)
    #id_autobots = 427899196985704450

    if message.author == client.user:
        return

    if message.channel == spec_channel:
      if message.content == "!Test":
        await spec_channel.send("Yes")
      
      if message.content.find("!Hello") != -1 :
        await spec_channel.send("Hi")

      if message.content == "!users": #Number of users
        await spec_channel.send(f"users : {id.member_count}.")

    
    if message.content.find("Salut") != -1 :
        await message.channel.send("Salut !")

    if message.content.find("Bonjour") != -1 :
        await message.channel.send("Salut !")

    if message.content.find("Ca va ?") != -1 :
        await message.channel.send("Oui et toi ?!")

    if message.content.find("What's up !") != -1 :
        await message.channel.send("Hey!")

    if message.content == "Super !":
        await message.add_reaction('\U0001F44D')

    if message.content == "GG":
        await message.channel.send('👍')

    if message.content == "Ah !":
        await message.add_reaction('<:Ah:327155261049536532>')

    if message.content == "Test":
        await voice.connect()

    if message.content == "merde":
        await message.channel.send("Ouai c'est la merde")

client.run(token)
