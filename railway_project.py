#----------------------Project:Railway  Ticket booking------------------------ 
import random
class Train():
    def __init__(self,train_num,source,destination,seats):
        self.train_num=train_num
        self.source=source
        self.destination=destination
        self.seats=seats
        
    def display(self):
        print(f"Train Number:{self.train_num}")
        print(f"Source:{self.source}")
        print(f"Destination:{self.destination}")
        print(f"Seats:{self.seats}")
        print()
    
    def book_tickets(self,num_tickets):
        if num_tickets>self.seats:
            None
        else:
            pnr_list=[]
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000,999999))
            self.seats=num_tickets
            return pnr_list

class Passenger:
    def __init__(self,name,age,gender,phoneno):
        self.name=name
        self.age=age
        self.gender=gender
        self.phoneno=phoneno
    
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Phoneno:{self.phoneno}")
        print()

class Tickets:
    def __init__(self,train,source,destination,passengers,pnr):
        self.train=train
        self.source=source
        self.destination=destination
        self.passengers=passengers
        self.pnr=pnr
    
    def display(self):
        print(f"Train:{self.train.train_num}")
        print(f"Source:{self.source}")
        print(f"Destination:{self.destination}")
        print(f"PNR:{self.pnr}")
        for passenger in self.passengers:
            passenger.display()
        print()

class Account:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def check_password(self,password):
        return self.password==password
    
accounts=[
    Account("username1","password1"),
    Account("username2","password2")
]
logged_in_account=None
while True:
    print("\n1.Create Account\n2.Login\n")
    choice=input("Enter Number:")
    if choice=='1':
        username=input("Enter Username:")
        password=input("Enter Password:")
        accounts.append(Account(username,password))
        print("Account Created Successfully")
    elif choice=='2':
        username=input("Enter Username:")
        password=input("Enter Password:")
        for account in accounts:
            if account.username==username and account.check_password(password):
                logged_in_account=account
                break
        if logged_in_account is None:
            print("Invalid Usernaame and Password")
        else:
            print(f"\nlogged in as {logged_in_account.username}\n\n-----Available Train details-----")
            break
    else:
        print("Invalid Choice")   

if logged_in_account  is not None:
    Trains=[
        Train('178748','kadapa','vizag',30),
        Train('178747','vizag','kadapa',26),
        Train('12742','chennai','vijayawada',10),
    ]
    
for train in Trains:
    train.display()
    
while True:
    try:
        train_num=input("Enter Train Number:")
        num_tickets=int(input("Enter No.of Tickets:"))
        if num_tickets<=0:
            raise ValueError("No.of Tickets should be greater than 0")
        for train in Trains:
            if train.train_num==train_num:
                if num_tickets>train.seats:
                  raise ValueError("Selected more tickets than available tickets")
                break
        else:
            raise ValueError("Invalid Train Number")
        break
    except ValueError as e:
        print(f"Invalid Input:{e}")
        
train=None
for t in Trains:
     if t.train_num == train_num:
         train=t
         break       
     
if train is None:
    print("Invalid Train Number")
else:
    passengers=[]
    for i in range(num_tickets):
        print(f"Entered no.of passengers {i+1}:")
        while True:
            try:
                name=input("Enter name:")
                if not name:
                    raise ValueError("Invalid Input")
                age=int(input("Enter Age:"))
                if age<=0 or age>=120:
                    raise ValueError("Invalid Age")
                gender=input("Enter Gender:")
                phone=input("Enter Phone Number:")
                if not phone or len(phone)!=10 or not phone.isdigit():
                    raise ValueError("Invalid Phone Number")
                passenger=Passenger(name,age,gender,phone)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input:{e}")
    
    pnr_list=train.book_tickets(num_tickets)   
    if pnr_list is  None:
        raise ValueError("Ticket not booking")
    else:
        print("---------------Booking Successful!--------------\n\nYour Train Details:\n")
        for i in range(num_tickets):
            ticket=Tickets(train,train.source,train.destination,[passengers[i]],pnr_list[i])
            ticket.display()
            print("\n------Thank You-------\n------Safe Journey------")
            
                 

                
                
        
        
            
    
    
    
        
    
    
    
        
    
        
        
                
            