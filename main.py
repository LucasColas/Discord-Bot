import discord
import Token

token = Token.read_token()

client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(325925436804825111)
    if message.author == client.user:
        return

    #ch = client.get_channel(427899196985704450)
    #if message.author.id == 427899196985704450:
    if message.content.find("!Test") != -1 :
      await message.channel.send("Operational !")
      
    if message.content.find("!Hello") != -1 :
      await message.channel.send("Hi")

    if message.content == "!users": #Number of users
      await message.channel.send(f"users : {id.member_count}.")


    
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
