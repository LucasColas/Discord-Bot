import discord
import Token

token = Token.read_token()

client = discord.Client()
client.run(token)
