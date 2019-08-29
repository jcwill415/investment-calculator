# -*- coding: utf-8 -*-
"""
@author: github.com/byochim
"""
class investment_models():
    def __init__(self, gain, cost, time, annual_gain, cash, discount):
        '''
        All variables are numbers entered by the user.
        '''
        self.gain = gain
        self.cost = cost
        self.time = time
        self.annual_gain = annual_gain
        self.cash = cash
        self.discount = discount
    
    def calc_ROI(gain, cost):
        '''
        ROI = Gain/Cost
        '''
        roi = (gain/cost) * 100
        return(roi)
    
    def calc_NPV(time, discount, cost):
        '''
        NPV = Cash/(1+r)^t - Cost 
        '''
        i = 0
        npv = 0
        for n in range(time):
            i += 1
            cash = float(input("Enter the cash flow or return for year " + str(i) + ": "))
            npv += (cash/(1+discount) ** i)
    
        npv = round((npv-cost),2)
        # Rounding to nearest tenth
        return(npv)
            
    def calc_PP(cost, annual_gain):
        '''
        PP = Cost/Gain
        '''
        pp = (cost/annual_gain)
        return(pp)
        
    def calc_DCF(time, discount):
        '''
        DCF = Cash/(1+r)^t
        '''
        i = 0
        dcf = 0
        for n in range(time):
            i += 1
            cash = float(input("Enter the cash flow or return for year " + str(i) + ": "))
            dcf += (cash / (1+discount)**i)
        
        dcf = round((dcf),2)
        # Rounding to nearest tenth
        return(dcf)


class lifetime_earnings_models():
    def __init__(self, starting_salary, temp_salary, cost, time, years):
        '''
        All variables are numbers entered by the user.
        '''
        self.starting_salary = starting_salary
        self.temp_salary = temp_salary
        self.cost = cost
        self.time = time
        self.years = years

    def calc_earnings(starting_salary, years):
        '''
        Earnings = Salary + 3% over n iterations
        '''
        salary = starting_salary
        earnings = 0.0
        for n in range(years):
            salary = salary + (salary*.03)
            earnings = salary + earnings
        
        earnings = round(earnings,2)
        return(earnings)
        
    def calc_earnings_degree(temp_salary, cost, time, starting_salary, years):
        '''
        Earnings = Salary + 3% over n iterations - Cost of degree/cert + Salary while completing degree/cert
        '''
        salary = temp_salary
        earnings = 0 - cost
        for n in range(time):
            salary = salary + (salary*.03)
            earnings = salary + earnings
        
        salary = starting_salary
        for n in range(years):
            salary = salary + (salary*.03)
            earnings = salary + earnings
        
        # Rounding to nearest tenth
        earnings = round(earnings,2)
        return(earnings)