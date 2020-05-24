import discord
import Token

token = Token.read_token()

client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(325925436804825111)

    if message.content.find("!Hello") != -1 :
        await message.channel.send("Hi")

    if message.content.find("Salut") != -1 :
        await message.channel.send("Salut !")

    if message.content.find("Bonjour") != -1 :
        await message.channel.send("Salut !")

    if message.content.find("Ca va ? ") != -1 :
        await message.channel.send("Oui et toi ?!")

    if message.content.find("What's up !") != -1 :
        await message.channel.send("Hey!")

    if message.content == "!users":
        await message.channel.send(id.member_count)

    if message.content == "super !":
        await add_reaction()

permission = discord.permission()

permission.create_instant_invite()
client.run(token)
