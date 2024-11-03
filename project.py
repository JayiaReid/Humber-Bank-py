#1: opening acount
def securityCheck():
    correctPin = 3752
    tries = 1
    while True:
        pin = input("Enter 4-digit pin to access account: ")
        
        if(len(pin)!= 4 or not pin.isdigit()):
            print('Invalid Input')
        else:
            if(int(pin)==correctPin):
                break
            else:
                #2
                if(tries<3):
                    print(f'incorrect pin. Try agin... {3-tries} tries left')
                    print('---'*8)
                    tries+=1
                else:
                    print('access denied. Try again in a year')
                    exit()
  
def displayBal():
    global balance
    print(f"Current Balance: ${balance:.2f}")
    

def withdraw():
    global balance
    
    print('---Withdrawal Service Active---')
    print('-20')
    print('-40')
    print('-60')
    print('-80')
    print('-100')
    print('-custom amount')
    print('---' * 5)
    
    try:
        amount = float(input('Select an option above by entering the amount or Enter a custom amount: '))
        
        if amount >0:
            if balance >= amount:
                balance -= amount 
                print(f'New Balance: ${balance:.2f}')
            else:
                print('Insufficient funds')
        else:
            print('Enter a valid amount. thanks')
            withdraw()
    except ValueError:
        print("Invalid input. Please enter a valid amount.\n")
        withdraw()
        
        
  
def deposit():
    global balance
    print("---Deposit Service Active---")
    #11
    try:
        amount = float(input('Enter amount you would like to deposit: '))
        if amount>0:
            balance += amount 
            print(f'New Balance: ${balance:.2f}')
        else:
            print('Enter valid amount')
            deposit()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        deposit() 
    
    
#3    
def mainMenu():
    while True:
        print('----Main Menu----')
        print('(1) Display Balance')
        print('(2) Make a withdrawal')
        print('(3) Make a Deposit')
        print('(4) Exit')
        
        try:
            task = int(input('Select an option above by entering the respective number: '))
            
            if(task == 1):
                displayBal() #4
            elif(task ==2):
                withdraw() #5
            elif(task==3):
                deposit() #6
            elif(task==4):
                print('Thank you for banking with us!Exiting......')
                exit() #7
            else:
                print('Invalid Input: Enter a number between 1 and 4.')
                continue
        except ValueError:
            print('Invalid Input: Enter a number between 1 and 4.')
            continue
        
        #8
        
        state=input('would you like to perform another action? (y)yes (n)no: ')
        if(state=='n' or state=='no'):
            print('Thank you for banking with us!Exiting......')
            exit()

balance = 10000.00
print('---'*8)
print('Hello! Welcome to Humber Banking') #1
print('---'*8)
securityCheck()
mainMenu()

