/*
@author: github.com/byochim
*/

#include <iostream>
#include <cmath>
#include <string>  
using namespace std;
#include "header.h"

investment_models::investment_models() {}

double investment_models::calc_ROI(double gain, double cost) {
    /*
    ROI = Gain/Cost
    */
    double roi = gain/cost * 100;
    
    return(roi);
}

double investment_Models::calc_NPV(double time, double discount, double cost) {
    /*
    NPV = Cash/(1+r)^t - Cost
    */   
    double npv = 0;
    double cash;

    for(int i=0; i<time; i++) {
        cout << "Enter the cash flow or return for year " << i << ": " << endl;
        cin >> cash;
        npv += pow((cash/(1+discount)),i);
    }

    return(npv);
}

double investment_models::calc_PP(double cost, double annual_gain) {
    /*
    PP = Cost/Gain
    */
    double pp = (cost/annual_gain);
    return(pp);
}

double investment_models::calc_DCF(double time, double discount) {
    /*
    DCF = Cast/(1+r)^t
    */
    double dcf = 0;
    double cash;
    
    for(int i=0; i<time; i++) {
        cout << "Enter the cash flow or return for year " << i << ": " << endl;
        cin >> cash;
        dcf += pow((cash/(1+discount)),i);
    }

    return(dcf);
}

lifetime_earnings_models::lifetime_earnings_models() {}

double lifetime_earnings_models::calc_earnings(double starting_salary, double years) {
    /*
    Earnings = Salary + 3% over n interations
    */
    double salary = starting_salary;
    double earnings = 0.0;
    
    for(int i=0; i<years; i++) {
        salary = salary + (salary*.03);
        earnings = salary + earnings;
    }

    return(earnings);
}

double lifetime_earnings_models::calc_earnings_degree(double temp_salary, double cost, double time, double starting_salary, double years) {
    /* 
    Earnings = Salary + 3% over n iterations - Cost of degree/cert + Salary while completing degree
    */
    double salary = temp_salary;
    double earnings = 0 - cost;

    for(int i=0; i<time; i++) {
        salary = salary + (salary*.03);
        earnings = salary + earnings;
    }

    salary = starting_salary;

    for(int i=0; i<years; i++) {
        salary = salary + (salary*.03);
        earnings = salary + earnings;
    }

    return(earnings);
}
