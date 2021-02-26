import urllib.request
import json
import datetime

#Prospa8isa na min to paro me 2 kliseis tou site alla mono me mia gia na ginei kalitero 
#diladi den pira id
#alla den 3ero an auto telika itan i kaliteri lisi :(  --->  #WhatAmIdoing?

x=datetime.datetime.now()
y=x.strftime("%Y-%m-%d")
u=x.strftime("%d")
c=x.strftime("%m")
v=x.strftime("%Y")
b=[]

#Pairnei mono tin proti klirosi to exo tsekarei!
for i in range(0,int(u)):
    z=datetime.date(int(v), int(c), int(u)-i)
    g=str(z)
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/"+g+"/"+g
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    for draw in data ["content"]:
        b.append(draw["winningNumbers"]["list"])   
        break    
    

#Poses fores emfanizetai o ka8e ari8mos (apo ton 0 eos ton 99) se ka8e proti klirosi tis ka8e imeras!
h=[]
for d in b:
    for j in range(100):
        r=d.count(j)
        if r>0 :
            h.append(j)
        
        
for k in range(100):
    l=h.count(k)
    print("O ari8mos",k,"emfanizetai:",l,"fores")

#A little Hard


