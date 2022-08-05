import discord
from discord.ext import commands, tasks
import datetime
import pytz
import requests
from bs4 import BeautifulSoup
import pandas
from discord_ui import UI
import matplotlib.pyplot as plt

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# class eth_button(discord.ui.View):
#   # class for the buttons with time frames for the graph of prices, put the buttons into the embed by 
#   # adding the "view = eth_button(timeout = optional_timeout_time)" field to the ctx.channel.send"
#   # gembed is an unadded function that creates the embed that corresponds to the button pressed
  
   
#     async def on_timeout(self):
#         for child in self.children:
#             child.disabled = True
#         await self.message.edit(view = self)

#     @discord.ui.button(label = "1 day", style = discord.ButtonStyle.gray)
#     async def button_press1(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(1))

#     @discord.ui.button(label = "1 week", style = discord.ButtonStyle.gray)
#     async def button_press2(self, button, interaction):
#         await interaction.response.edit_message(embed = gembed(2))

#     @discord.ui.button(label="2 weeks", style=discord.ButtonStyle.gray)
#     async def button_press3(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(3))

#     @discord.ui.button(label="1 month", style=discord.ButtonStyle.gray)
#     async def button_press4(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(4))

#     @discord.ui.button(label="3 months", style=discord.ButtonStyle.gray)
#     async def button_press5(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(5))

#     @discord.ui.button(label="6 months", style=discord.ButtonStyle.gray)
#     async def button_press6(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(6))

#     @discord.ui.button(label="1 year", style=discord.ButtonStyle.gray)
#     async def button_press7(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(7))

#     @discord.ui.button(label="All time", style=discord.ButtonStyle.gray)
#     async def button_press8(self, button, interaction):
#         await interaction.response.edit_message(embed=gembed(8))

#     @discord.ui.button(label = "Kill embed", style=discord.ButtonStyle.danger)
#     async def button_press9(self, button, interaction):
#         for child in self.children:
#             child.disabled = True
#         await interaction.response.edit_message(embed=gembed(9), view = self)

def timeStamp():
  tz = pytz.timezone('US/Eastern')
  time = datetime.datetime.now(tz)
  dateFormatted = time.strftime("%A %d %B %Y")
  timeFormatted = time.strftime("%I:%M %p + %Ss")
  return time, dateFormatted, timeFormatted

def getPrices():
  url = "https://coinmarketcap.com/currencies/ethereum/"
  r = requests.get(url, headers = headers)
  soup = BeautifulSoup(r.text, 'lxml')
  price = soup.find('div', class_ = 'priceValue').findAll('span')[0].text
  
  date, dateFormat, timeFormat = timeStamp()
  return price, date, dateFormat, timeFormat

def getData(id, currency, days, interval):
  cryptoids = check()

  if id in cryptoids:
    url = f'http://api.coingecko.com/api/v3/coins/{id}/market_chart'
    payload = {'vs_currency' : currency, 'days' : days, 'inverval' : interval}
    r = requests.get(url, params = payload, headers = headers)
    data = r.json()

    prices = []
    timestamps = []

    for i in data['prices']:
      prices.append(i[1])
      timestamps.append(datetime.datetime.fromtimestamp(i[0]/1000))

    rawData = {
      'Date' : timestamps,
      'Price' : prices
    }

    df = pandas.DataFrame(rawData)
    return df

  else: 
    print('crypto does not exist.')
    return 1

def plotGraph(days=1, interval='hourly', color='#00E7FF'):
  ethInfo = getData('ethereum', 'usd', days, interval)
  ethInfo.plot(x='Date', y='Price', color=color)
  plt.ylabel('Price')
  plt.title('i\'ll name this later')
  plt.savefig(r'ethPlot.png')

def check():
    url = f'https://api.coingecko.com/api/v3/coins'
    r = requests.get(url, headers = headers)
    data = r.json()
    cryptoids = []

    for i in data:
        cryptoids.append(i['id'])

    return cryptoids 
  
class ethereum_moniter(commands.Cog): 
    def __init__(self, client):
        self.client = client
        self.liveMoniter.start()
        self.count = 0

    def cog_unload(self):
        self.liveMoniter.cancel()

    # @commands.command()
    @tasks.loop(seconds=120)
    async def liveMoniter(self):
      ethMoniter = self.client.get_channel(1002742610160517130)

      try:
        plotGraph()

        price, date, dateFormat, timeFormat = getPrices()
        timestamp = f"""```fix\nTimestamp: {date}```"""
    
        if self.count%3 == 0 or self.count == 0:
          await ethMoniter.send(f"__**ETH**__: **{price}** as of {dateFormat}, {timeFormat} (US/Eastern time)", file=discord.File("ethPlot.png"))
          await ethMoniter.send(timestamp)
        else:
          await ethMoniter.send(f"__**ETH**__: **{price}** as of {dateFormat}, {timeFormat} (US/Eastern time)\nNOTE: add a note later\n{timestamp}")

        self.count += 1

      except Exception as e:
        await ethMoniter.send(f'ERROR: {e}')
        print(e)

      
 
    @liveMoniter.before_loop
    async def beforeMoniter(self):
        print('Waiting for bot...') 
        await self.client.wait_until_ready()


def setup(client): 
    client.add_cog(ethereum_moniter(client))
