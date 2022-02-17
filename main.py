import discord
import os 
import requests
import json
from keep_alive import keep_alive;

client=discord.Client()

def quote_code():
  response=requests.get("https://zenquotes.io/api/random");
  data_=json.loads(response.text);
  quote=data_[0]['q']+"-"+data_[0]['a']
  return(quote);

@client.event
async def on_ready():
  print("born ready")

@client.event
async def on_message(message):
  if message.author == client.user:
    return;
  msg=message.content;
  if msg.startswith(".i"):
    if (msg[3:].lower()=="r u there" and str(message.author)=="IshtiaqSamdani#8441"):
      await message.channel.send("at your service always sir🐱‍👤");
      
    elif msg==".i hello":
      await message.channel.send("Hello folks");
    elif msg[3:].lower().startswith("who r you") or msg[3:].lower().startswith("who r u") or msg[3:].lower().startswith("who are you"):
      await message.channel.send("I am first ever bot of Ishtiaq Ahmed alias TS");
      await message.channel.send("know more about me by command .i commads");
    elif msg[3:].lower()=="commands":
      await message.channel.send("here are some commands")
      await message.channel.send(".i <query> to talk to me😘");
      await message.channel.send(".i inspire for a quote🤟");
      await message.channel.send(".p <song name> to play a song😊");
      await message.channel.send("My sir is still working on me but we will be in touch💕");
    elif msg[3:]=="inspire":
      quote=quote_code();
      await message.channel.send(quote);
    else:
      await message.channel.send("I am down on internet "+str(message.author)[:-5])
  if msg.startswith(".p"):
    await message.channel.send("Enjoy the music sir🎸");
    await message.channel.send(".play"+msg[2:]);

keep_alive();
client.run(os.environ['TOKEN'])


