x=0
Meeting=[]
team=[]
human=[]
tems=["Web"," GD","3D","AI","IS","QA","M"]
John=["AI","QA","M"]
Bryce=["Web","3D","IS"]
Kailee=["GD","3D","AI"]
Mike=["3D","QA","M"]
David =["Web","GD","IS"]
Harry=["AI","M"]
Megan=["GD","3D","QA"]
Carly=["Web","IS","M"]
Robert=["Web","GD","AI","IS"]
Rudy=["Web","3D","QA"]
speaker=[John,Bryce,Kailee,Mike,David,Harry,Megan,Carly,Robert,Rudy]
speakers=["John","Bryce","Kailee","Mike","David","Harry","Megan","Carly","Robert","Rudy"]
#120
for q in range(len(speakers)-2):
w=speaker[q]
f=speakers[q]
for e in range(len(speaker)-1):
if e<=q:
continue
r=speaker[e]
g=speakers[e]
for t in range(len(speaker)-0):
if t<=e:
continue
y=speaker[t]
h=speakers[t]
d=0
for u in w:
human.append(u)
for i in r:
human.append(i)
for o in y:
human.append(o)
for a in tems:
s=human.count(a)
if s == 2:
d=d+2
elif s==3:
d=d+3
team.append([f,g,h,d])
human=[]
#8214570
for q in range(len(team)-3):
w=team[q]
for e in range(len(team)-2):
if e<=q:
continue
r=team[e]
for t in range(len(team)-1):
if t<=e:
continue
k=team[t]
for j in range(len(team)):
if j<=t:
continue
y=team[j]
z=w[3]+r[3]+k[3]+y[3]
human=[w[0],w[1],w[2],r[0],r[1],r[2],k[0],k[1],k[2],y[0],y[1],y[2],z]
n=0
for a in speakers:
s=human.count(a)
if s >3 or s == 0:
n=1
break
if n==0:
if z==x:
Meeting.append(human)
elif z>x:
x=z
Meeting=[]
Meeting.append(human)

print(Meeting)
