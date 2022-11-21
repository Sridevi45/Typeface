s1=input()
s2=input()
c=0
x=s2[len(s2)-1]
for i in s1:
  if i==x:
    c+=1    
print(c)
