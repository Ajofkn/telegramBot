import requests
import json
import os
token = os.environ.get("IEXAPI")
def ticker(ticker):
    
    res = requests.get('https://cloud.iexapis.com/stable/stock/{}/quote?token={}'.format(ticker, token))
    data = res.json()

    name = data["companyName"]
    price = data["iexRealtimePrice"]
    high = data["week52High"]
    low = data["week52Low"]
    change = data["change"]
    percentChange = data["changePercent"]
    peratio = data["peRatio"]

    text = "Name: {} \nPrice: {}\nPrice Change: {}\nPercent Change: {}\nP/E Ratio: {}\n52 Week High: {}\n52 Week Low: {} ".format(name, price, change, percentChange, peratio, high, low)
    
    return text