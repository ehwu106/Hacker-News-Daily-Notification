import feedparser
import discord
import pytz
from pytz import timezone
from datetime import datetime, date
from dateutil import parser

def run_bot(notification):
    try:
        TOKEN = '{YOUR_TOKEN}'
        client = discord.Client(intents=discord.Intents.default())
        @client.event
        async def on_ready():
            print(f'{client.user} is now running!')
            server = client.get_guild('{YOUR_SERVER_ID}')
            channel = server.get_channel('{YOUR_CHANNEL_ID}')
            await channel.send("```"+notification+"```")
            # await channel.send(notification)
            await client.close()
        client.run(TOKEN)
    except:
        print("Unable to Send Discord Message")

def feed_parser():
    feed = feedparser.parse('https://feeds.feedburner.com/TheHackersNews')
    title = feed['feed']['title']
    link = feed['feed']['link']
    articles=[]
    now = datetime.now(pytz.timezone('US/Pacific'))
    articles.append(f'Daily Cybersecurity News From: {title} | Date: '+format(now.strftime('%Y/%m/%d'))+'\n\n\n')
    for entry in feed['entries']:
        article_date = parser.parse(entry.published).date()
        if article_date== date.today():
            title = entry['title']
            link = entry['link']
            articles.append(f'Article title: {title}'+'\n'+f'Article link: {link}\n\n')
    run_bot(''.join(articles))

if __name__ == "__main__":
    feed_parser()

