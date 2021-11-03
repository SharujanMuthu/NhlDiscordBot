import discord
import access
import WebScraper

TOKEN = "ODk0NjU5NzM2MTk1MTg2ODE4.YVtOzw.XwHAdRVLIxFYYSOMr_tSALgq5e0"

WebScraper.get_data()

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == "bot":
        if "stats" in user_message.lower():
            word = ""
            new_word = user_message.split()[:2]
            count = 0
            for name in new_word:
                word += name
                count += 1
                if count != 2:
                    word += " "
            #await message.channel.send(word)
            stat = access.get_stats(word)
            await message.channel.send(access.format_stats(stat))

    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return


client.run(TOKEN)


