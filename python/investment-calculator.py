 # -*- coding: utf-8 -*-
"""
@author: github.com/byochim
"""
import sys
from classlist import investment_models
from classlist import lifetime_earnings_models

def main():
    '''
    Introductory message briefly explaining the program.
    '''
    print("Welcome to the Investment Calculator."
      "\nThis calculator contains basic models for ROI, NPV, PP, and DCF."
      "\nAdditionally, it contains a model to calculate lifetime earnings, or earnings over n years."
      "\nGiven a starting salary x, will provide you with an estimate of your total earnings over n years."
      "\nYear-to-year salary increases are estimated at 3%."
      "\nEnter the required data when prompted and you will receive a calculation for the chosen model."
      "\nType 'exit' at any main prompt to exit the program."
      )
    
    print("")
    choose()
    

def choose():
    '''
    Prompts user to choose between the two main calculators.
    '''
    choice = input("\nPress 1 for the investment models calculator or press 2 for the lifetime earnings calculator: ")
    
    if choice == "1":
        choice_investment_models()
        
    if choice == "2":
        choice_lifetime_earnings_model()
    
    choice = choice.upper()
    # Converts to uppercase to filter exit command
    
    if choice == 'EXIT':
    # Exits program
        print("Goodbye.")
        sys.exit()
        
    else:
    # Re-enters choose function if the user doesn't input a valid command
        print("Invalid input.")
        choose()
        

def choice_investment_models():
    '''
    Prompts user to choose an investment model for calculation.
    '''
    choice = input("\nWhat would you like to calculate first? (ROI, NPV, PP, or DCF): ")
    choice = choice.upper()
    # Converts to uppercase to filter input
    
    if choice == "ROI":
        ROI()
    
    if choice == "NPV":
        NPV()
            
    if choice == "PP":
        PP()
        
    if choice == "DCF":
        DCF()
    
    if choice == 'EXIT':
        print("Goodbye.")
        sys.exit()
        
    else:
    # Re-enters choice_investment_models function if the user doesn't input a valid command
        print("Invalid input.")
        choice_investment_models()
    
    
def ROI():
    '''
    Input: user data required for the ROI model
    Output: ROI calculation
    '''
    # Controls in place in case user does not enter a number
    while True:
        try:
            # Converts from str to float for decimals and the calculation
            # Abs is to control for negative inputs
            cost = abs(float(input("Enter the initial investment cost: ")))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
            
    while True:
        try:
            # Converts from str to float for decimals and the calculation
            gain = float(input("\nEnter the gain or loss from the investment: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    
    # Calls the calc_ROI function from the classlist file in order to calculate the ROI
    print("\nYour ROI is " + str(investment_models.calc_ROI(cost, gain)) + "%.")
    end()
    

def NPV():
    '''
    Input: user data required for the NPV model
    Output: NPV calculation
    '''
    # Controls in place in case user does not enter a number
    while True:
        try:
            # Converts from str to float for decimals and the calculation
            # Rounds to the nearest whole number for calculation
            # Abs is to control for negative inputs
            time = abs(round(float(input("Enter the length of the project or investment in years (decimals will be rounded to the nearest whole number): "))))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    
    while True:
        try:
            # Converts from str to float for decimals and the calculation
            # Abs is to control for negative inputs
            discount = abs(float(input("Enter the discount rate (please enter in decimal form): ")))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    
    while True:
        try:
            # Converts from str to float for decimals and the calculation
            # Abs is to control for negative inputs
            cost = abs(float(input("Enter the initial investment cost: ")))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break

    # Calls the calc_NPV function from the classlist file in order to calculate the NPV
    # Prints in dollar format
    print("\nYour NPV is " + "${:,.2f}".format(investment_models.calc_NPV(time, discount, cost)))
    end()

 
def PP():
    '''
    Input: user data required for the PP model
    Output: PP calculation
    '''
    # Controls in place in case user does not enter a number
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            cost = abs(float(input("Enter the initial investment cost: ")))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            annual_gain = abs(float(input("Enter the annual net cash flow gained from the investment: ")))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
        
    # Calls the calc_PP function from the classlist file in order to calculate the PP
    print("\nYour PP is " + str(investment_models.calc_PP(cost, annual_gain)) + " years.")
    end()
    

def DCF():
    '''
    Input: user data required for the DCF model
    Output: DCF calculation
    '''
    # Controls in place in case user does not enter a number
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Rounds to the nearest whole number for calculation
        # Abs is to control for negative inputs
            time = abs(round(float(input("Enter the length of the project or investment in years (decimals will be rounded to the nearest whole number): "))))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            discount = abs(float(input("Enter the discount rate (please enter in decimal form): ")))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        break

    # Calls the calc_DCF function from the classlist file in order to calculate the DCF
    # Prints in dollar format
    print("\nYour DCF is " + "${:,.2f}".format(investment_models.calc_DCF(time, discount)))
    end()
    
def choice_lifetime_earnings_model():
    '''
    Gives user option to include the cost of a degree or certification with the calculation.
    '''
    choice = (input("Would you like to calculate the earnings of a degree or certification? (Y/N): "))
    choice = choice.upper()
    # Converts to uppercase to filter exit command
 
    if choice == "Y" or choice == "YES":
        earnings_degree()
        
    if choice == "N" or choice == "NO":
        earnings()
        
    if choice == "EXIT":
    # Exits program
        print("\nGoodbye.")
        sys.exit()
        
    else:
    # Re-enters choice_lifetime_earningsModel function if the user doesn't input a valid command
        print("\nInvalid input.")
        choice_lifetime_earnings_model()

    
def earnings():
    '''
    Input: user data required for earnings calculation (no degree/cert)
    Output: earnings calculation without degree/cert
    '''
    # Controls in place in case user does not enter a number
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            starting_salary = abs(float(input("Enter starting salary: ")))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Rounds to the nearest whole number for calculation
        # Abs is to control for negative inputs
            years = abs(round(float(input("Enter the number of years you'd like to calculate (decimals will be rounded to the nearest whole number): "))))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        break
    
    # Calls the calc_earnings function from the class-list file in order to calculate the earnings
    # Prints in dollar format
    print("\nYour earnings over a " + str(years) + " period, given a starting salary of " + "${:,.2f}".format(starting_salary) + ", total " + "${:,.2f}".format(lifetime_earnings_models.calc_earnings(starting_salary, years)))
    end()
    
        
def earnings_degree():
    '''
    Input: user data required for earnings calculation
    Output: earnings calculation with degree/cert
    '''
    # Controls in place in case user does not enter a number
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            cost = abs(float(input("Enter the total cost of the degree or certification: ")))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Rounds to the nearest whole number for calculation
        # Abs is to control for negative inputs
            time = abs(round(float(input("Enter the number of years it will take you to complete your degree or certification (decimals will be rounded to the nearest whole number): "))))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            temp_salary = abs(float(input("Enter your yearly salary be while you complete this degree or certification: ")))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Abs is to control for negative inputs
            starting_salary = abs(float(input("Enter starting salary: ")))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
    
    while True:
        try:
        # Converts from str to float for decimals and the calculation
        # Rounds to the nearest whole number for calculation
        # Abs is to control for negative inputs
            years = abs(round(float(input("Enter the number of years you'd like to calculate (decimals will be rounded to the nearest whole number): "))))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
    
    # Calls the calc_earnings_degree function from the classList file in order to calculate the earnings with degree/cert
    # Prints in dollar format
    print("\nYour post-completion earnings over a " + str(years) + " period, given a starting salary of " + "${:,.2f}".format(starting_salary) + ", total " + "${:,.2f}".format(lifetime_earnings_models.calc_earnings_degree(temp_salary, cost, time, starting_salary, years)))        
    end()

def end():
    '''
    Gives the user the option to calculate something else or exit the program.
    '''
    choice = input("\nPress 1 to calculate something else or press 2 (or type 'exit') to exit the program: ")
    choice = choice.upper()
    # Converts to uppercase to filter exit command

    if choice == "1":
        choose()
        
    if choice == "2" or choice == "EXIT":
    # Exits program
        print("Goodbye.")
        sys.exit()
        
    else:
    # Re-enters end function if the user doesn't input a valid command
        print("Invalid input.")
        end()

main()

