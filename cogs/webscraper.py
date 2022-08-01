from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import os

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class Webscraper(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(help = " - _weather {unit} {city} #unit = imperial, metric, or standard")
    async def weather(self, ctx, units, *, city):
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.environ['weather_key']}&units={units}"
      await ctx.send(f"{url}")
      r = requests.get(url, headers = headers)
      data = r.json()

      try:
        sky = data['weather'][0]['main']
        skyDesc = data['weather'][0]['description']
        temp = data['main']['temp']
        feelTemp = data['main']['feels_like']
        # weather = data['weather'][1]['main']
        # weatherDesc = data['weather'][1]['description']
        humidity = data['main']['humidity']
        country = data['sys']['country']
        windspeed = data['wind']['speed']
        degreeSign = ""
        if units.lower() == 'imperial':
          degreeSign = "℉"
        elif units.lower() == 'metric':
          degreeSign = "℃" 
        elif units.lower() == 'standard':
          degreeSign = "K"
        else:
          await ctx.send('**ERROR: use actual valid unit. The three ones are imperial ||(fahrenheit)||, metric ||(celcius)||, and standard ||(kelvin)||.**')
          return
      except KeyError:
        await ctx.send(f'thats not a city <:thinking1:892138392953958460>')
      
      await ctx.send(f"""__**City**__: {city.capitalize()} ({country})
__**Units**__: {units.capitalize()} system
It is {sky.lower()} ({skyDesc.lower()}), temperature is {temp}{degreeSign} (but feels like {feelTemp}{degreeSign}). The humidity is {humidity}, and for those of you going surfing, the wind speed is {windspeed}.
      """)

  
    @commands.command(help = " - _stonks {stonck symbol} #Example: _stonks AMZN")
    async def stonks(self, ctx, Symbol):
        url = f'https://finance.yahoo.com/quote/{Symbol}'
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            # findAll always returns in a list form, so we can index it.
            price = soup.find('fin-streamer', class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)').text
            growth = soup.find('div', class_ = 'D(ib) Mend(20px)').findAll('span')[1].text
            await ctx.send(f'{Symbol.upper()}: ${price}, {growth}')
            
        except AttributeError:
            await ctx.send('You have an invalid stock symbol. Try putting in one that exists.')

    @commands.command(help = " - Example: _crypto dogecoin #checks dogecoin prices")
    async def crypto(self, ctx, Crypto):
      URL = f"https://coinmarketcap.com/currencies/{Crypto}/"
      r = requests.get(URL, headers = headers)

      try:
        soup = BeautifulSoup(r.text, 'lxml')
        price = soup.find('div', class_ = 'priceValue').findAll('span')[0].text
        await ctx.send(f'{Crypto.capitalize()}: {price}')
      except AttributeError:
        await ctx.send('argument should have valid ALL LOWERCASE crypto name. Example: _crypto dogecoin, _crypto ethereum')



def setup(client): 
    client.add_cog(Webscraper(client))