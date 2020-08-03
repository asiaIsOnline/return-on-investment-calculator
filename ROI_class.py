class ROI():
    def __init__(self, pprice, units):
        self.pprice = pprice
        self.units = units
    
    """
        RentIncCalc will require 2 positional arguments:
        Positional arguments will be replaced by two input prompts.
        Both prompts will expect an integer.
    """
     # PERCENTAGE TEST 
    def percent_test(self):
        # Gathers the 3 Possible Rent Prices for 1%, 1.5% and 2%
        self.possible_rent_per_unit_one = float(self.pprice) * 0.01
        self.possible_rent_per_unit_onehalf = float(self.pprice) * 0.015
        self.possible_rent_per_unit_two = float(self.pprice) * 0.02

        print(f"Property Price: ${self.pprice}\n Monthly Rental Charge at 1%: ${int(self.possible_rent_per_unit_one)} | Monthly Rental Charge at 1.5%: ${int(self.possible_rent_per_unit_onehalf)} | Monthly Rental Charge at 2% ${int(self.possible_rent_per_unit_two)}")

    # INCOME COLLECTION
    def income(self):
        # Collects the Monthly Rental Income per Unit Manually
        rent_per_unit = input("\nHow much are you charging (or are planning to charge) each unit a month for rent?: ")
        while rent_per_unit.isdigit() == False:
            rent_per_unit = input("Sorry, rent per unit needs to be entered as a whole number. Try again: ")
        rent_per_unit = int(rent_per_unit)
        
        # Collects the Monthly Laundry Income
        laundry_income = input("How much monthly laundry income is your property expected to bring in?: ")
        while laundry_income.isdigit() == False:
            laundry_income = input("Sorry, laundry income needs to be entered as a whole number. Try again: ")
        laundry_income = int(laundry_income)
        
        # Collects the Monthly Storage Income
        storage_income = input("How much monthly on-site storage income is your property expected to bring in?: ")
        while storage_income.isdigit() == False:
            storage_income = input("Sorry, storage income needs to be entered as a whole number. Try again: ")
        storage_income = int(storage_income)

        # Collects the Monthly Carport Income
        carport_income = input("How much monthly garage storage income is your property expected to bring in?: ")
        while carport_income.isdigit() == False:
            carport_income = input("Sorry, monthly carport needs to be entered as a whole number. Try again: ")
        carport_income = int(carport_income)
                
        # Collects any remaining Miscellaneous Income
        misc_income = input("Enter the amount of any other miscellaneous property income you would like to include: ")
        while misc_income.isdigit() == False:
            misc_income = input("Sorry, miscellaneous income needs to be entered as a whole number. Try again: ")
        misc_income = int(misc_income)
                
        self.total_monthly_income = (rent_per_unit * self.units) + laundry_income + storage_income + carport_income + misc_income
        print(f"The amount of your total monthly income equates to: ${self.total_monthly_income}\n")
        return self.total_monthly_income

    # EXPENSE COLLECTION
    def expenses(self):
        # Collects the Monthly Tax Expenses
        tax_expense = input("Enter the amount of your monthly tax expense for the property: ")
        while tax_expense.isdigit() == False:
            tax_expense = input("Sorry, tax expenses need to be entered as a whole number. Try again: ")
        tax_expense = int(tax_expense)

        # Collects the Monthly Insurance Expenses 
        insurance_expense = input("Enter the amount of your monthly insurance expense for the property: ")
        while insurance_expense.isdigit() == False:
            insurance_expense = input("Sorry, insurance expenses need to be entered as a whole number. Try again: ")
        insurance_expense = int(insurance_expense)

        # Collects the Monthly Utilities Expenses
        utilities_expense = input("Enter the amount of total monthly utilities expenses you would like to include: ") 
        while utilities_expense.isdigit() == False:
            utilities_expense = input("Sorry, utilities expenses need to be entered as a whole number. Try again: ")
        utilities_expense = int(utilities_expense)

        # Collects the Monthly HOA Expenses
        hoa_expense = input("Enter the amount of your monthly HOA (Home Owners Association) expense: ")
        while hoa_expense.isdigit() == False:
            hoa_expense = input("Sorry, HOA expenses need to be entered as a whole number. Try again: ")
        hoa_expense = int(hoa_expense)

        # Collects Monthly Visual Upkeep Expense
        visual_upkeep_expense = input("Enter the amount for your monthly visual upkeep expenses: ")
        while visual_upkeep_expense.isdigit() == False:
            visual_upkeep_expense = input("Sorry, visual upkeep needs to be entered as a whole number. Try again: ")
        visual_upkeep_expense = int(visual_upkeep_expense)

        # Collects Monthly Vacancy Cost Expense
        vacancy_cost_expense = input("Enter the amount for your monthly vancancy cost expenses: ")
        while vacancy_cost_expense.isdigit() == False:
            vacancy_cost_expense = input("Sorry, vacancy cost needs to be entered as a whole number. Try again: ")
        vacancy_cost_expense = int(vacancy_cost_expense)

        # Collects Repair Expenses
        repair_cost_expense = input("Enter the amount of your expected monthly repair costs for the property: ")
        while repair_cost_expense.isdigit() == False:
            repair_cost_expense = input("Sorry, repair costs need to be entered as a whole number. Try again: ")
        repair_cost_expense = int(repair_cost_expense)

        # Collects CapEx Expenses
        capEx_expense = input("Enter the amount of your monthly capital expenditures: ")
        while capEx_expense.isdigit() == False:
            capEx_expense = input("Sorry, CapEx expenses need to be entered as a whole number. Try again: ")
        capEx_expense = int(capEx_expense)

        # Collects Property Management Expenses
        property_manage_expense = input("Enter the amount of your monthly property management expenses: ")
        while property_manage_expense.isdigit() == False:
            property_manage_expense = input("Sorry, the cost of monthly property management needs to be entered as a whole number. Try again: ")
        property_manage_expense = int(property_manage_expense)

        # Collects Mortgage Expenses
        mortgage_expense = input("Enter the amount of your monthly mortgage or loan expenses: ")
        while mortgage_expense.isdigit() == False:
            mortgage_expense = input("Sorry, monthly mortgage expenses need to be entered as a whole number. Try again: ")
        mortgage_expense = int(mortgage_expense)

        self.total_monthly_expenses = tax_expense + insurance_expense + utilities_expense + hoa_expense + visual_upkeep_expense + vacancy_cost_expense + repair_cost_expense + capEx_expense + property_manage_expense + mortgage_expense
        print(f"The amount of your total monthly expenses equates to {self.total_monthly_expenses}.\n")
        return self.total_monthly_expenses

    # CASH FLOW 
    def cashFlow(self):
        self.cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f"The cash flow for this property equates to: ${self.cash_flow}\n")
        return self.cash_flow

    # CASH ON CASH RETURN ON INVESTMENT
    def cocROI(self):
        # Collects the Initial Down Payment for the Property
        # Presents the option to use an automated down payment that's created from 20% of the property price. 
        print("If you've yet to purchase this property and don't have a given down payment, we offer an automated down payment. ")
        print("This automated down payment would be 20% of the Total Property Price.")
        auto_down_payment = input("Would you like to use the automated down payment amount. Enter Yes or No: ")
        while True:
            if auto_down_payment.lower() == "yes":
                down_payment = float(self.pprice) * 0.20
                print(f"The automated down payment was set as: ${int(down_payment)}")
                break
            if auto_down_payment.lower() == "no": 
                down_payment = input("Please manually enter down payment for the property: ")
                while down_payment.isdigit() == False:
                    down_payment = input("Sorry, the down payment needs to be entered as a whole number. Try again: ")
                break
            else:
                auto_down_payment = input("Sorry, you need to enter yes or no. Would you like to use an automated down payment amount? ")
        down_payment = int(down_payment)

        # Collects the Closing Costs for the Property
        closing_costs = input("Enter the amount paid in closing costs for the property: ")
        while closing_costs.isdigit() == False:
            closing_costs = input("Sorry, closing costs need to be entered as a whole number. Try again: ")
        closing_costs = int(closing_costs)

        # Collects the Repair Money for the Property
        repair_money = input("Enter the amount paid in repair money (or the rehab budget): ")
        while repair_money.isdigit() == False:
            repair_money = input("Sorry, repair budget needs to be entered as a whole number. Try again: ")
        repair_money = int(repair_money)

        # Collects the Miscellaneous Cost for the Property
        misc_prop_money = input("Enter any other additional cost that came with the purchase of this property: ")
        while misc_prop_money.isdigit() == False:
            misc_prop_money = input("Sorry, miscellaneous costs should be entered as a whole number. Try again: ")
        misc_prop_money = int(misc_prop_money)

        total_investment_cost = down_payment + closing_costs + repair_money + misc_prop_money
        annual_cash_flow = self.cash_flow * 12
        cash_on_cash_ROI = round((annual_cash_flow / total_investment_cost * 100), 2)
        print(f"\nThe cash on cash return-on-investment for this property is {cash_on_cash_ROI}%.") 
        print(f"The stock market averages around 6% to 7% annual return on investment.")
        if cash_on_cash_ROI < 6.00:
            print(f"Since this ROI falls below 6% you may want to really consider this investment.") 
        elif cash_on_cash_ROI >= 6.00 and cash_on_cash_ROI < 8.00:
            print(f"Since this ROI falls between 6% and 8% this is a decent investment.")
        elif cash_on_cash_ROI >= 8.00 and cash_on_cash_ROI < 20.00:
            print(f"Since this ROI falls between 8% and 20% this is a good investment.")
        elif cash_on_cash_ROI >= 20.00:
            print(f"Since this ROI falls at or above 20% this a ideal investment!")
        return cash_on_cash_ROI
