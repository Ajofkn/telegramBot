from bs4 import BeautifulSoup
import requests
import string

# Function that takes in one single ticker, finds it on the yahoo finance website, and returns the specified attributes
# in an object and returns it.
def findPrice(ticker):
    data = {}      
    url = "https://finance.yahoo.com/quote/{}".format(ticker)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    data["name"] = soup.find('h1', attrs={"data-reactid": "7"}).text
    data["price"] = soup.find('span', attrs={"data-reactid": "50"}).text
    data["shift"] = soup.find('span', attrs={"data-reactid": "51"}).text
    data["close"] = soup.find('td', attrs={"data-test": "PREV_CLOSE-value"}).text
    data["openPrice"] = soup.find('td', attrs={"data-test": "OPEN-value"}).text

    attributes = "Name: "+data["name"]+ "\n" +"Current Price: $" +  data["price"] +"\n"+  "Price Change: "+data["shift"]+"\n"+ "Previous Close: $"+data["close"]+"\n"+ "Open Price: $"+ data["openPrice"]

    return attributes
# Function that removes any duplicate tickers within the list of tickers
def removeDupes(tickerList):
    returnList = []
    [returnList.append(i) for i in tickerList if i not in returnList]
    return returnList

# Takes in the split message, and uses it to find any tickers within it to insert into a seperate list. Returns list of tickers sans puncuation
def findTicker(msg):
    tickList = []
    for i in msg:
        if "$" in i:
            if i =="$":
                pass        
            else:
                i = i.translate(str.maketrans('', '', string.punctuation))
                tickList.append(i)
    tickList = removeDupes(tickList)
    return tickList

