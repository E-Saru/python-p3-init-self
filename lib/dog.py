#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name=name
        self.breed=breed
        # print(f"{name} is born!")

#     # def showing_self(self):
#     #     return self

    # def bark(self):
    #     print("Woof!")

    # def get_adopted(self, owner_name):
    #     self.owner=owner_name
        
#     def adopt(dog, owner_name):
#         dog.owner = owner_name

# adopt(fido, "Sophie")

fido=Dog("Fido")
fido.breed
# fido.name
# # fido.showing_self()
# # fido.bark("fido")
snoopy=Dog("Snoopy", "Terrier")
snoopy.breed

# fido.owner="Sophie"
# fido.get_adopted("Sophie")
# fido.owner