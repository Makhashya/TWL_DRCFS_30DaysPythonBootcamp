from typing import Any

#def add_contact(name: str, email: str, phone: int) -> bool:
 #   with open('Week 2\personal\contact\contact.txt','a') as file:
  #      file.write(name +","+ email + ","+str(phone))
   #     file.write('\n')
    #    return 1
    #return 0
#def find_contact(username: str) -> str:
#with open('Week 2\personal\contact\contact.txt','r') as file:
    #contents=file.read()
    #print(contents)
    #contents = [i.split(",") for i in contents.split('\n')][:-1]
    #print(contents)

#def import_contacts(filename) -> bool:
##file1 = open('Week 2\personal\contact\precontact.txt', 'r')
#file2 = open('Week 2\personal\contact\contact.txt','a')
#file1 = file1.readlines()
#print(file1)
#for item in file1:
  #  contact_details = item.split(",")
   # file2.write(','.join(contact_details))

print("Printing all the contacts")
file = open("Week 2\personal\contact\contact.txt",'r')
contacts = file.readlines()
for contact in contacts:
    name,email,phone = contact.split(",")
    print("name:"+ name+ "email:"+ email+"phone:"+phone )







