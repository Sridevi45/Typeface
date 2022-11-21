def converttoternary(N):
if(N==0):
  return;
x=N%3;
N//=3;
if(x<0):
  N+=1;
converttoternary(N):
if(x<0):
  print(x+(3*-1),end="");
else:
 print(x,end="");
def convert(decimal):
  print("ternary number of",decimal,"is:",end="");
  if(decimal!=0):
     converttoternary(decimal);
  else:
     print("0",end="");
