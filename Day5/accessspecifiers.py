class Parent:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"
    def access_from_same_class(self):
        print("Inside Parent class:")
        print("Public     :", self.public_var)
        print("Protected  :", self._protected_var)
        print("Private    :", self.__private_var)
class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child class (Subclass):")
        print("Public     :", self.public_var)
        print("Protected  :", self._protected_var)
        print("Private    :", self.__private_var)
c = Child()
c.access_from_same_class()
print()
c.access_from_subclass()
