# magical_witch_book

This project contains 4 main classes:

1. MagicalContact: it contains the attributes of a contact (name, email, phone number)
   and it has its methods:
   get_name(): gets the name of a contact
   get_email(): gets the email of a contact
   get_phone_number(): gets the phone number of a contact
   set_email(email): sets the contact's current email to another one typed by the user (email)
   set_phone_number(phone_number): sets the contact's current phone number to another one typed by the user(phone_number)
   describe(): describes the contact as in it prints its name, email and phone number

2. MagicalUser: it contains the same attributes as MagicalContact in addition to a description of the user's wand(core material, wood type, length) and the house of the user (either Gryffindor, Hufflepuff, 
   Ravenclaw or Slytherin otherwise it's an error) and it has the same methods in addition to:
   get_wand(): gets the description of the wand (its core material, wood type and length)
   get_house(): gets the user's house
   describe(): acts the same as the describe() method in MagicalContact in addition to a description of the wand and the user's house

3. MagicalCreature: it contains the same attributes as MagicalContact in addition to the creature's species and if it's tameable or not and it has the same methods in addition to:
   get_species(): gets the creature's species
   is_tame(): prints whether the creature is tameable or not
   describe(): acts the same as the describe() method in MagicalContact in addition to printing its species and if it's tameable or not

4. MagicalContactBook: it contains a list of contacs from the MagicalContact class with their name, email and phone number and it has its methods:
   add_contact(contact): adds a contact from the MagicalContact class written by the user (contact) onto the list with its name, email and phone number
   list_contacts(): prints all of the contacts in the list with their name, phone number and email
   find_contact(name): searches for a certain contact by its name and if it finds it, the name, email and phone number are printed as the contact was found. otherwise, it will print not found

   You are free to use the methods and create contacts, users and creatures with their description and add them to the contact book 
   
