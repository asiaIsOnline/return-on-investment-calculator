from ROI_class import ROI

def runROI():
    # Starts by asking the user for an input for property price.
    property_price = input("Welcome to the ROI Calculator.\nPlease input the property's price: ")
    while property_price.isdigit() == False:
        property_price = input("Sorry, property price needs to be entered as a whole number. Try Again: ")
    property_price_num = int(property_price)
    
    # Also collects the user's input for unit amount. 
    unit_amount = input("Thank you. Please input the property's unit amount: ")
    while unit_amount.isdigit() == False:
        unit_amount = input("Sorry, unit amount needs to be entered as a whole number. Try Again: ")
    unit_amount = int(unit_amount)
    
    # Enters the user's input into the class instance arguments
    ROI_calc = ROI(property_price, unit_amount)

    # Starts running the calculator's property income collection function.
    # Return value is equal to the total monthly income.
    print("If you don't have a monthly rental charge per unit already chosen this program will show different amounts based on percentage. ")
    use_two_percent_test = input("Would you like to use the Percent Test to see possible rental charges? If so, enter Yes otherwise enter No. ")
    while True:
        if use_two_percent_test.lower() == "yes":
            percent_test_function = ROI_calc.percent_test()
            income_function = ROI_calc.income()
            break
        if use_two_percent_test.lower() == "no":
            income_function = ROI_calc.income()
            break
        else: 
            use_two_percent_test = input("Sorry, you need to enter Yes or No. Would you like to see possible monthly unit charges based on percentage? ")

    # Starts running the calcultor's property expense collection function.
    # Return value is equal to the total monthly expenses. 
    expense_function = ROI_calc.expenses()

    # Starts running the calculator's cash flow function.
    # Return value is equal to the cash flow. 
    cash_flow_function = ROI_calc.cashFlow()

    #Starts running the calculator's final ROI function.
    # Princes the Cash on Cash Return on Investment
    print("Finally, almost to the end!")
    return_on_investment_function = ROI_calc.cocROI()
runROI()