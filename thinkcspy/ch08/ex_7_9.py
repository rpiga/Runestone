def is_prime(n):
  # your code here
  idx = 2
  
  while idx < n:
    if n % idx == 0:
      return False
    idx += 1
  
  return True
