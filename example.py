#function definition
def test():
    print("Hello")
#function definition
def addition(a,b):
    print("Addition of two numbers",a+b)
#function definition for credit function
balance_amount=100000 #global variable
def credit(amount): #amount is formal parameter
    global balance_amount
    balance_amount+=amount
    print("Current account balance is",balance_amount)