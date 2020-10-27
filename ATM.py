# Import Math Module As MT
import math as mt

print("Hello This is An ATM")


# Ask For Money
Ask_Money = int(input("How Much Money Do you want: "))


# Currency

Currency = input("Enter Your Currency : ")


stock_Of_Money = 2523434526435654732

if Ask_Money >  stock_Of_Money:
    
    print("Our Bank is out of stock ")
    
    Ask_Negotiation = mt.sqrt(Ask_Money)
    
    print(Ask_Negotiation)
    
    Ask1  = input("Would You Like This Negotiation")

    
    if Ask1 == "Yes" or "yes":
        print("Ok It Is Going Into Your Virtual Bank Account")
        
        quit()
        
    else:
        print("Ok The Money Transaction is cancelled")
        
        quit()

else:
    print("Here Is Your Money ", Ask_Money, "  In ", Currency)
    
    print(Currency, Ask_Money)

    print("We Are Sending This to your Virtual Bank Account")

    quit()
