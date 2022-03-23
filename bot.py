import discord
import createEvent
import os
import bottoken

client = discord.Client()

callsign = '%'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    input = message.content.lower()
    if message.author == client.user:
        return
    
    if input.startswith(callsign + 'exit'):
        await send(message, 'Exiting')
        os._exit(0)

    if input.startswith(callsign + 'event'):
        await send(message, 'Creating calendar event')
        await send(message, createEvent.createEvent())

    if input.startswith(callsign + 'help'):
        inputarray = input.split(' ')
        if len(inputarray) == 1:
            await send(message, '1')
            return
        match inputarray[1]:
            case _:
                await send(message, 'success')

async def send(message, response):
    await message.channel.send(response)


# client = MyClient()
client.run(bottoken.token.value)