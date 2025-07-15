#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[]) {
    int income = atoi(argv[1]);
    int expenses = atoi(argv[2]);
    int savings = income - expenses;

    if (savings > 0)
        cout << "Great! You're saving ₹" << savings << " per month.";
    else
        cout << "Alert! You're overspending by ₹" << -savings << " per month.";
    return 0;
}

