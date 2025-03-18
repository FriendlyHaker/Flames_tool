#getting two names
print("NOTE: this is only for time pass!")
str1=input("Enter first name:")
str2=input("Enter second name:")
#covert into lower case
name1=str1.lower()
name2=str2.lower()
#storing str1 into separate charecters
a1=name1.count('a')
b1=name1.count('b')
c1=name1.count('c')
d1=name1.count('d')
e1=name1.count('e')
f1=name1.count('f')
g1=name1.count('g')
h1=name1.count('h')
i1=name1.count('i')
j1=name1.count('j')
k1=name1.count('k')
l1=name1.count('l')
m1=name1.count('m')
n1=name1.count('n')
o1=name1.count('o')
p1=name1.count('p')
q1=name1.count('q')
r1=name1.count('r')
s1=name1.count('s')
t1=name1.count('t')
u1=name1.count('u')
v1=name1.count('v')
w1=name1.count('w')
x1=name1.count('x')
y1=name1.count('y')
z1=name1.count('z')
#storing str2 into separate charecters
a2=name2.count('a')
b2=name2.count('b')
c2=name2.count('c')
d2=name2.count('d')
e2=name2.count('e')
f2=name2.count('f')
g2=name2.count('g')
h2=name2.count('h')
i2=name2.count('i')
j2=name2.count('j')
k2=name2.count('k')
l2=name2.count('l')
m2=name2.count('m')
n2=name2.count('n')
o2=name2.count('o')
p2=name2.count('p')
q2=name2.count('q')
r2=name2.count('r')
s2=name2.count('s')
t2=name2.count('t')
u2=name2.count('u')
v2=name2.count('v')
w2=name2.count('w')
x2=name2.count('x')
y2=name2.count('y')
z2=name2.count('z')
#subracting  number of repeted characters 
a=a1-a2
b=b1-b2
c=c1-c2
d=d1-d2
e=e1-e2
f=f1-f2
g=g1-g2
h=h1-h2
i=i1-i2
j=j1-j2
k=k1-k2
l=l1-l2
m=m1-m2
n=n1-n2
o=o1-o2
p=p1-p2
q=q1-q2
r=r1-r2
s=s1-s2
t=t1-t2
u=u1-u2
v=v1-v2
w=w1-w2
x=x1-x2
y=y1-y2
z=z1-z2
#adding number of uncommon charecters
lenth=abs(a)+abs(b)+abs(c)+abs(d)+abs(e)+abs(f)+abs(g)+abs(h)+abs(i)+abs(j)+abs(k)+abs(l)+abs(m)+abs(n)+abs(o)+abs(p)+abs(q)+abs(r)+abs(s)+abs(t)+abs(u)+abs(v)+abs(w)+abs(x)+abs(y)+abs(z)
#giving result using added charecters
if(lenth==3 or lenth==5 or lenth==14 or lenth==16 or lenth==18):
	print("They Are Friends!")
elif(lenth==10 or lenth==19):
	print("They Are Lovers!")
elif(lenth==8 or lenth==12 or lenth==13 or lenth==17):
	print("Affection Bitween Them!")
elif(lenth==6 or lenth==11 or lenth==15):
	print("They Will Marriage!")
elif(lenth==2 or lenth==4 or lenth ==7 or lenth==9 or lenth==20):
	print("They Are Enimies!")
elif(lenth==1):
	print("They Are Siblings!")
else:
	print(" check the names!")	