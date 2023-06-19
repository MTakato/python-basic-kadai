Human_List=[]

class Human:
  def __int__(self):
    self.name = ""
    self.age = ""
  
  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age
  
  def check_adult(self):
    if self.age >= 20:
      print("Adult")
    else:
      print("No Adult")


Yamada = Human()
Yamada.set_name("Taro")
Yamada.set_age(21)
  
Human_List.append(Yamada)

Suzuki = Human()
Suzuki.set_name("Hanako")
Suzuki.set_age(18)

Human_List.append(Suzuki)


for i in range(0,len(Human_List)):
  Human_List[i].check_adult()
