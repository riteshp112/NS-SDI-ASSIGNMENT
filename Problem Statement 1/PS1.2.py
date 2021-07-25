def rec0tox(x,num):
  if num>x:
    return
  print(num,end=" ")
  rec0tox(x,num+2)
    
x=int(input("Input the value of X "))
rec0tox(x,0)