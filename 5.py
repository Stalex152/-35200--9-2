vafly=['Admin','Vlad','Roma','Kolya','Katya']
if vafly==[]:
    print('We need to find some users!')
else:
    for x in vafly:
        if x =='Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello '+x+', thank you for logging in again')
input=raw_input()
            
