import urllib.request
import json

#Prosoxi!!!!
#To arxeio prepei na einai tis morfis-> BTH:20
#                                       ETH:2
#                                       LTC:4 


#Times ap to site
def get_coin_price(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d[coin]["EUR"]


#Pairnei times ap to arxeio
f=open("Random.txt", "r")
a={}
for c in f:
    (key,value)=c.split(":")
    a[key]=float(value)
f.close()


x=a["BTC"]*get_coin_price("BTC")
y=a["ETH"]*get_coin_price("ETH")
z=a["LTC"]*get_coin_price("LTC")

#Deixnei poso plousios einai kaneis!!
print("Your btc worth:",x,"€")
print("Your eth worth:",y,"€")
print("Your ltc worth:",z,"€")

#EZZZZZ








