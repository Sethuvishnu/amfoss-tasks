x=int(input(""))
r=[]
for i in range(x):
    x,y,z=map(int,input("").split(" "))
    r.append([x,y,z])
s_x=0
s_y=0
s_z=0
for j in r:
    s_x+=j[0]
    s_y+=j[1]
    s_z+=j[2]
if s_x==0 and s_x==0 and s_x==0:
    print("YES")
else:
    print("NO")
    
