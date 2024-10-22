


class MagicalContact:
    def __init__(self , name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number


    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_phone_number(self):
        return self.__phone_number
    def set_email(self,email):
        self.__email = email
    def set_phone_number(self,phone_number):
        self.__phone_number = phone_number
    def describe(self):
        print(f"name: {self.__name}, {self.__email}, {self.__phone_number}")


class MagicalUser(MagicalContact):
    def __init__(self, name,email,phone_number,wand, house):
        super().__init__(name, email, phone_number)
        self.name = name
        self.__wand = dict(wand)
        self.__house = house
        houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if house not in houses:
            raise ValueError




    def get_wand(self):
        return f"{self.__wand["length"] , self.__wand["wood"] , self.__wand["core"]}"
    def get_house(self):
        return self.__house
    def describe(self):
        super().describe()
        print(f"length of wand: {self.__wand["length"]} , Wand wood: {self.__wand["wood"]} , Wand core material: {self.__wand["core"]}, House: {self.__wand}")


class MagicalCreature(MagicalContact):
    def __init__(self, name, email, phone_number, species, is_tame):
        super().__init__(name, email, phone_number)
        self.name = name
        self.__species = species
        self.__is_tame = bool(is_tame)
        if self.__is_tame:
            self.__is_tame = "this creature is tame"
        else:
            self.__is_tame = "this creature isn't tame"


    def get_species(self):
        return self.__species
    def is_tame(self):
        return self.__is_tame
    def describe(self):
        super().describe()
        print(f"species: {self.__species} , tameness: {self.__is_tame}")

class MagicalContactBook:
    def __init__(self, contacts):
        self.__contacts = list(contacts)

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def list_contacts(self):
        if len(self.__contacts) > 0:
            print("List:")
        for contact in self.__contacts:
            MagicalContact.describe(contact)

    def find_contact(self, name):
         for contact in self.__contacts:
            if name == contact.name :
                MagicalContact.describe(contact)
                return

         print("not found")

#start typing here:






