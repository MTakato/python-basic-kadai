#商品の金額aを１00から10000の範囲で考えています
import math
import random

a = random.randint(100, 10000)
b = 10
def c_tax(a: int ,b):
  total =a + a * b / 100
  total = math.floor(total)
  return total

c_tax(a,b)
