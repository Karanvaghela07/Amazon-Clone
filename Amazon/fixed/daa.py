def is_prime(n):
  if (n<=0):
    return 0
  else:
    for i in range(2,n):
      count = 0
      if(n%i == 0):
        count += 1
        print("not prime")
        break
  if(count == 0):
      print("prime")
      
n = int(input())

is_prime(n)