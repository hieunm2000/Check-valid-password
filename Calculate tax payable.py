# input
income = int(input("Your income is: "))
tax_payable = 0

def calculate_tax(income, tax_payable):
    
    # write if statement to check if income <= 10000
    if income <= 10000:
        tax_payable = 0
    
    # write if statement to check if income <= 20000
    elif income <= 20000:
        tax_payable = (income - 10000) * 0.1
    
    # write if statement to check if income > 20000
    else:
        tax_payable = (income - 20000) * 0.2
   
    print("Total tax to pay is:", tax_payable)
calculate_tax(income, tax_payable)