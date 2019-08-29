#ifndef HEADER_H
#define HEADER_H

class investment_models {
    public:
        investment_models();
        
        double calc_ROI(double gain, double cost);
        double calc_NPV(double time, double discount, double cost);
        double calc_PP(double cost, double annual_gain);
        double calc_DCF(double time, double discount);
};

class lifetime_earnings_models {
    public:
        lifetime_earnings_models();

        double calc_earnings(double starting_salary, double years);
        double calc_earnings_degree(double temp_salry, double cost, double time, double starting_salary, double years);
};

#endif
