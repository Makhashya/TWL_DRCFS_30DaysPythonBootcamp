# line 10 wala function
#readlines()
'''
username = "UjwalMakhashya"
with open('Week 2\personal\practise\contact.txt','r') as file:
    contents = file.read()
    contents = [i.split(',') for i in contents.split('\n')][:-1]
    res = []
    for name,email,phone in contents:
        if name.lower() == username.lower():
            res.append((name,email,phone))
        print(res)
    #return res   
'''
print('PRINTING ALL CONTACTS')
try:
    contacts = open('Week 2\personal\practise\contact.txt','r').readline()
    for i, contact in enumerate(contacts):
        contact = contact.split(',')
        print(f'Contact No. {i}')
        print(f'Name: {contact[0]}')
        print(f'Email: {contact[1]}')
        print(f'Phone: {contact[2]} \n')
except Exception as e:
    print('No Contacts found.. INVALID FILE PATH. Please change the Relative path of the file in code to run it in windows properly')

