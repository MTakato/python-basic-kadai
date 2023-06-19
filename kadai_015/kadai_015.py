class Human:
  def __int__(self):
    self.name = ""
    self.age = ""
  
  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age
  
  def printinfo(self):
    print(self.name)
    print(self.age)

Yamada = Human()
Yamada.set_name("Taro")
Yamada.set_age(21)
Yamada.printinfo()
