/*
@author: github.com/byochim
*/

#include <iostream>
#include <algorithm> 
#include <string>  
#include <stdlib.h>
#include <cmath>
#include "header.h"
using namespace std;

investment_models model;
lifetime_earnings_models earnings_model;

int ROI() {
    /*
     Input: user data required for the ROI model
     Output: ROI calculation
    */
    double cost;
    double gain;
    int x = 0; 
    
    cout << "Enter the initial investment cost: " << endl; 
    while(!(cin >> cost)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter the gain or loss from the investment: " << endl;
    while(!(cin >> gain)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }

    cout << "Your ROI is " << model.calc_ROI(gain, cost) << "%." << endl;
    return 0;
}

int NPV() {
    /*
    Input: user data required for the NPV model
    Output: NPV calculation
    */
    double time;
    double discount;
    double cost; 
    
    cout << "Enter the length of the project or investment in years (decimals will be rounded to the nearest whole number): " << endl;
    while(!(cin >> time)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter the discount rate (please enter in decimal form): " << endl;
    while(!(cin >> discount)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter the initial investment cost: " << endl;
    while(!(cin >> cost)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    round(time);
    cout << "Your NPV is " << "$" << model.calc_NPV(time, discount, cost) << endl;
    return 0;
}

int PP() {
    /*
    Input: user data required for the PP model
    Output: PP calculation
    */
    double cost;
    double annual_gain;

    cout << "Enter the initial investment cost: " << endl;
    while(!(cin >> cost)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }

    cout << "Enter the annual net cash flow gained from the investment: " << endl;
    while(!(cin >> annual_gain)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }

    cout << "Your PP is " << model.calc_PP(cost, annual_gain) << " years." << endl;
    return 0;
}

int DCF() {
    /*
    Input: user data required for the DCF model
    Output: DCF calculation
    */
    double time;
    double discount;

    cout << "Enter the length of the project or investment in years (decimals will be rounded to the nearest whole number): " << endl;
    while(!(cin >> time)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter the discount rate (please enter in decimal form): " << endl;
    while(!(cin >> discount)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    round(time);
    cout << "Your DCF is " << "$" << model.calc_DCF(time, discount) << endl;
    return 0;
}

int earnings() {
    /*
    Input: user data required for earnings calculation (no degree/cert)
    Output: earnings calculation without degree/cert
    */
    double starting_salary;
    double years;

    cout << "Enter starting salary: " << endl;
    while(!(cin >> starting_salary)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter  the number of years you'd like to calculate (decimals will be rounded to the nearest whole number): " << endl;
    while(!(cin >> years)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
   
   round(years);
   cout << "Your earnings over a " << years << " period, given a starting salary of " << "$" << starting_salary << ", total " << "$" << earnings_model.calc_earnings(starting_salary, years) << endl;
   return 0;
}

int earnings_degree() {
    /*
    Input: user data required for earnings calculation 
    Output: earnings calculation with degree/cert
    */
    double cost;
    double time;
    double temp_salary;
    double starting_salary; 
    double years;
    
    cout << "Enter the total cost of the degree or certification: " << endl;
    while(!(cin >> cost)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    

    cout << "Enter the number of years it will take you to complete your degree or certification (decimals will be rounded to the nearest whole number): " << endl;
    while(!(cin >> time)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter your yearly salary be while you complete this degree or certification: " << endl;
    while(!(cin >> temp_salary)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
   
    cout << "Enter starting salary: " << endl;
    while(!(cin >> starting_salary)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    cout << "Enter the number of years you'd like to calculate (decimals will be rounded to the nearest whole number): " << endl;
    while(!(cin >> years)) {
        cin.clear();
        cin.ignore();
        cout << "Invalid input. Please enter a valid number." << endl;
    }
    
    round(time);
    round(years);
    cout << "Your post-completion earnings over a " << years << " period, given a starting salary of " << "$" << starting_salary << ", total " << "$" << earnings_model.calc_earnings_degree(temp_salary, cost, time, starting_salary, years) << endl;
    return 0;
}

int choice_lifetime_earnings_model() {
    /*
    Gives user option to include the cost of a degree or certification with the calculation.
    */
    string choice;
    cout << "Would you like to calculate the earnings of a degree or certification? (Y/N): " << endl;
    cin >> choice;
    std::transform(choice.begin(), choice.end(),choice.begin(), ::toupper);

    if(choice == "Y" || choice == "YES") {
        earnings_degree();
        return 0;
    }
    if(choice == "N" || choice == "NO") {
        earnings();
        return 0;
    }
    if(choice == "EXIT") {
        cout << "Goodbye.";
        return 0;
    }
    else {
        cout << "Invalid input." << endl;
        choice_lifetime_earnings_model();
        return 0;
    }
}

int choice_investment_models() {
    /*
    Prompts user to choose an investment model for calculation.
    */
    string choice;
    cout << "What would you like to calculate first? (ROI, NPV, PP, or DCF): " << endl;
    cin >> choice;
    std::transform(choice.begin(), choice.end(), choice.begin(), ::toupper);

    if (choice == "ROI") {
        ROI();
        return 0;
    }
    if (choice == "NPV") {
        NPV();
        return 0;
    }
    if (choice == "PP") {
        PP();
        return 0;
    }
    if (choice == "DCF") {
        DCF();
        return 0;
    }
    if (choice == "EXIT") {
        cout << "Goodbye.";
        return 0;
    }
    else {
    // Re-enters the choice_investment_models function if user doesn't input a valid command
        cout << "Invalid input." << endl;
        choice_investment_models();
        return 0;
    }
}

int choose() {
    /*
    Prompts user to choose between the two main calculators.
    */
    string choice;
    cout << "Press 1 for the investment models calculator or press 2 for the lifetime earnings calculator: " << endl;
    cin >> choice;

    if (choice == "1") {
       choice_investment_models();
       return 0;
    }
    if (choice == "2") {
       choice_lifetime_earnings_model();
       return 0;
    }
    
    std::transform(choice.begin(), choice.end(), choice.begin(), ::toupper);
    
    if (choice == "EXIT") {
    //Exits program
        cout << "Goodbye.";
        return 0;
    }

    else {
        cout << "Invalid Input." << endl;
        choose();
        return 0;
    }
}

int end() {
    /*
    Gives the user the option to calculate something else or exit the program.
    */
    string choice;
    cout << "Press 1 to calculate something else or press 2 (or type 'exit') to exit the program: " << endl;
    cin >> choice;
    std::transform(choice.begin(), choice.end(),choice.begin(), ::toupper);

    if(choice == "1") {
        choose();
        return 0;
    }
    if(choice == "2" || choice == "EXIT") {
        cout << "Goodbye.";
        return 0;
    }
    else {
        cout << "Invalid input." << endl;
        return 0;
    }
}

int main() {
    /*
    Introductory message briefly explaining the program. 
    */

    cout << R"(Welcome to the Investment Calculator.
    This calculator contains basic models for ROI, NPV, PP, and DCF.
    Additionally, it contains a model to calculate lifetime earnings, or earnings over n years.
    Given a starting salary x, will provide you with an estimate of your total earnings over n years.
    Year-to-year salary increases are estimated at 3%.
    Enter the required data when prompted and you will receive a calculation for the chosen model.
    Type 'exit' at any main prompt to exit the program.)" << endl << "" << endl; 
    choose();
    end();
    
    return 0;
}

