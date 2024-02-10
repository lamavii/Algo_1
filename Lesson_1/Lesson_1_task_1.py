#Вам даны три числа 𝑎, 𝑏, и 𝑐. Определите, является 
#ли одно суммой двух других.

t=0
while t<1 or t> 9261:
  t=int(input())   
count=0
while count<t:
  a, b, c =map(int,input().split())
  if a == b+c or b==a+c or c==a+b:
       print('YES')
  else:
   print('NO') 
  count+=1



   