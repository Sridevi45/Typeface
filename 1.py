t=int(input())
k="
while(t):
  k+=str(t%3)
  t=int(t//3)
print(k[::-1])
