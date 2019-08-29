# investment-calculator

This program contains models for ROI, NPV, PP, and DCF. It also contains a model to calculate lifetime earnings, earnings over n years. 

I chose the sys module in order to allow the user to exit the program when the given specifications are met. I also imported classes from my own module, 'classList'. The Investment Calculator file handles the user inputs and program outputs while the classes handle the calculations. 

This was primarily an exercise in using classes and handling user inputs properly (invalid inputs, exiting the program, case insensitivity, etc.). 

## Usage

Providing calculations for the given models based on user input. The ROI, NPV, PP, and DCF are the standard models that a cursory google search will provide you with. 

The lifetime earnings model calculates earnings over *n* years, given a starting salary *x*, and assuming year-to-year salary increases of 3%. This model also provides an option to include the cost of a degree, both in terms of time and monetary cost. 
