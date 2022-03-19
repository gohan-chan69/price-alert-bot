'''import requests
api_key = 'api key'
def get_price(symbol):
    api_url = f'https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD&api_key={api_key}'
    r = requests.get(api_url).json()
    return r['USD']
def get_data(symbol):
    base_url = 'https://www.cryptocompare.com'
    api_url = f'https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms={symbol}&tsyms=USD&api_key={api_key}'
    r = requests.get(api_url).json()
    full_name = r['Data'][symbol]['CoinInfo']['FullName']
    img_url = r['Data'][symbol]['CoinInfo']['ImageUrl']
    full_img_url = base_url+img_url
    url = r['Data'][symbol]['CoinInfo']['Url']
    chrt_url = base_url+url
    coines_Mined = r['Data'][symbol]['CoinInfo']['TotalCoinsMined']
    Launch_Date = r['Data'][symbol]['CoinInfo']['AssetLaunchDate']
    supply = r['Data'][symbol]['CoinInfo']['MaxSupply']   
    return full_name, full_img_url, chrt_url,coines_Mined,Launch_Date,supply

def send_to_discord(symbol):
    price = get_price(symbol)
    full_name, full_img_url, chrt_url,coines_Mined,Launch_Date,supply = get_data(symbol)
    json1 = {"content": "@here","tts": False,'avatar_url': "https://cdn.discordapp.com/attachments/929686954726031393/949732158195527700/gojo_1.png","embeds": [{"type": "rich","title": symbol,"description": "all info was scraped from cryptocompare api","url": chrt_url,"color": 0xdaa6f6,"fields": [{"name": 'info!',"value": f"full_name: {full_name}\nprice: {price}\ncoines Mined: {coines_Mined}\nLaunch Date: Launch_Date\n Max Supply: {supply}"}],"author": {"author": {"url": chrt_url}},"thumbnail": {"url": full_img_url},"footer": {"text": symbol}}]}
    r = requests.post('https://discord.com/api/webhooks/934629182581907546/cGgGjwBzNT0ksETDyVfpVZsHJLyifDXhL1Da1tsaiHOt_bTVQ24T_p8FCe1uqjMozOxv',json=json1)
    print(r.json)
send_to_discord('ETH')'''



from email import header
from http import client
import requests
import discord
from discord.ext import commands
token = 'token here'
client = commands.Bot(command_prefix='!')
header = {
    "Authorization": f'Bot {token}'
}
api_key = 'your key here'
async def get_price(symbol):
    try:
        api_url = f'https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD&api_key={api_key}'
        r = requests.get(api_url).json()
        return r['USD']
    except:
        pass
async def get_data(symbol):
    try:
        base_url = 'https://www.cryptocompare.com'
        api_url = f'https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms={symbol}&tsyms=USD&api_key={api_key}'
        r = requests.get(api_url).json()
        full_name = r['Data'][symbol]['CoinInfo']['FullName']
        img_url = r['Data'][symbol]['CoinInfo']['ImageUrl']
        full_img_url = base_url+img_url
        url = r['Data'][symbol]['CoinInfo']['Url']
        chrt_url = base_url+url
        coines_Mined = r['Data'][symbol]['CoinInfo']['TotalCoinsMined']
        Launch_Date = r['Data'][symbol]['CoinInfo']['AssetLaunchDate']
        supply = r['Data'][symbol]['CoinInfo']['MaxSupply']   
        return full_name, full_img_url, chrt_url,coines_Mined,Launch_Date,supply
    except:
        pass
@client.command()
async def price(ctx,chan_id, symbol):
    price = await get_price(symbol)
    full_name, full_img_url, chrt_url,coines_Mined,Launch_Date,supply = await get_data(symbol)
    json1 = {"content": None,"tts": False,'avatar_url': "https://cdn.discordapp.com/attachments/929686954726031393/949732158195527700/gojo_1.png","embeds": [{"type": "rich","title": symbol,"description": "all info was scraped from cryptocompare api","url": chrt_url,"color": 0xdaa6f6,"fields": [{"name": 'info!',"value": f"full_name: {full_name}\nprice: {price}\ncoins Mined: {coines_Mined}\nLaunch Date: {Launch_Date}\n Max Supply: {supply}"}],"author": {"author": {"url": chrt_url}},"thumbnail": {"url": full_img_url},"footer": {"text": symbol}}]}
    r = requests.post(f'https://discord.com/api/v9/channels/{chan_id}/messages',json=json1, headers=header)
@commands.Cog.listener()
async def on_Command_error(ctx,error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member. Please try again.')
client.run(token)
