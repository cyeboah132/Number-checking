#include <iostream>


int main(){
    int Adult;
    int Children;

    std::cout << "Enter The Number Of Adult: " <<std::endl;
    std::cin >> Adult;

    std::cout << " Enter The Number of Children: " << std::endl;
    std::cin >> Children;

    int Total_People = Adult + Children;

    double Adult_cost = 9.99 * Adult;
    double Child_cost = 6.99 * Children;

    double Total_cost = Adult_cost + Child_cost;

    if (Total_People > 6 ){
        double Discount = 0.15 * Total_cost;
    }

    std::cout << "The total Adult there is " << Adult << std:: endl;
    std::cout << "The total Children there is " << Children << std:: endl;
    std::cout << "The total Number of peope there is " << Total_People << std:: endl;
    std::cout << "The total cost there is " << Total_cost << std::endl;
 
    return 0;
}