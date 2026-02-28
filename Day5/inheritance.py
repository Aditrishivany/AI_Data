class Grandfather:
    def wisdom(self):
        print("Grandfather shares wisdom")
class father(Grandfather):
    def drive(self):
        print("Father can drive")
class mother(Grandfather):
    def cook(self):
        print("Mother cooks")
class son(father):
    def play(self):
        print("Son is playing")
class daughter(father):
    def dance(self):
        print("Daughter is dancing")
class child(mother,father):
    def play(self):
        print("Child plays")
# s=son()
# s.wisdom()
# s.drive()
# s.play()
# d=daughter()
# d.wisdom()
# d.drive()
# d.dance()
c=child()
c.drive()
c.cook()
c.play()
c.wisdom()