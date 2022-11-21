def check(p):
  while(p>0):
    c=p%10
    if(c==3 or c==4 or c==7):
      return false
   p//=10
 return True
p=int(input())
c,count=1,1
while(count<p):
  c+=1
  if(check(c)):
    count+=1
print(c)
