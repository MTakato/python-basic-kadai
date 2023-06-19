#正の整数varを１から100の範囲で考えています。
import random
var = random.randint(1, 100)

if var%3 == 0:
  if var%5 ==0:
    print("FizzBuzz")
  else:
    print("Fizz")
elif var%5 == 0:
  print("Buzz")
else:
  print(var)
