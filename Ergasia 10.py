#Nai 3ero auto den itan kai oti pio e3ipno (iperbolika polles metablites)
#Alla den mporo na skefto kati allo distixos :(
#Kai nomizo leitourgei me oles tis periptoseis (enoo kai me alles ektos apo ta pradeigmata) giati to ti test tou ekana den perigrafetai! 
#Opote 8a elega oti den einai beta alla teleiomeno

a={}
c=0


b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
b7=0
b8=0
b9=0
b10=0
b11=0


i1="{"
i2=":["
i3="{["
i4=":{"
i5="["
i6="[["
i7="{{"
i8="[{"
i9="}"
i10="]"
i11=":"


d1=0
d2=0
d3=0
d4=0
d5=0
d6=0
d7=0
d8=0
d9=0
d10=0
d11=0
d12=0
d13=0
d14=0
d15=0
d16=0


j1="}},{{"
j2="}},[["
j3="}},[{"
j4="}},{["
j5="]],{{"
j6="]],[["
j7="]],[{"
j8="]],{["
j9="]},{{"
j10="]},[["
j11="]},[{"
j12="]},{["
j13="}],{{"
j14="}],[["
j15="}],[{"
j16="}],{["


f=open("Text.txt", "r")
a=f.read()
f.close()

#Bgazo ta kena giati dialioun to programma mou (me tin parakato sinartisi)
def HateSpaces(string): 
    return string.replace(" ", "") 
      
a=HateSpaces(str(a))
 

b1=a.count(i1)
b2=a.count(i2)  
b3=a.count(i3)
b4=a.count(i4)
b5=a.count(i5)
b6=a.count(i6)
b7=a.count(i7)
b8=a.count(i8)
b9=a.count(i9)
b10=a.count(i10)
b11=a.count(i11)


d1=a.count(j1)
d2=a.count(j2)
d3=a.count(j3)
d4=a.count(j4)
d5=a.count(j5)
d6=a.count(j6)
d7=a.count(j7)
d8=a.count(j8)
d9=a.count(j9)
d10=a.count(j10)
d11=a.count(j11)
d12=a.count(j12)
d13=a.count(j13)
d14=a.count(j14)
d15=a.count(j15)
d16=a.count(j16)


#Random thoughts!!
#But they work??
#Basika pros8eto oles tis periptoseis pou mou dinoun +1 ba8os (kai kapoies pou den xreiazontai alla tis afairo sti seinexeia)

if b1==1 and b2==0 and b3==0 and b4==0 and b5==0 and b6==0 and b7==0 and b8==0:
    c=1

if b5==1 and b2==0 and b3==0 and b4==0 and b1==0 and b6==0 and b7==0 and b8==0:
    c=1

if b1>0 and (b2!=0 or b3!=0 or b4!=0 or b5!=0 or b6!=0 or b7!=0 or b8!=0):
    c=1+b2+b3+b4+b6+b7+b8

if b5>0 and (b2!=0 or b3!=0 or b4!=0 or b1!=0 or b6!=0 or b7!=0 or b8!=0):
    c=1+b2+b3+b4+b6+b7+b8

if str(a)=="{}":
    c=0

if str(a)=="[]":
    c=0

if b1==1 and b9==1 and b11==0 and b5==0 and b10==0:
    c=0

if b5==1 and b10==1 and b11==0 and b1==0 and b9==0:
    c=0

#Kai edo afairo oles tis periptoseis pou mou au3anoun to ba8os otan den xreiazetai (diladi autes pou den einai mesa se alles gia na au3isoun to ba8os!) 
#Cringe   to 3ero!

c=c-d1-d2-d3-d4-d5-d6-d7-d8-d9-d10-d11-d12-d13-d14-d15-d16

print("O ba8mos tou ",a," einai ",c)

#PAINNN

