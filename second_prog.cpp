#include <iostream>

enum class Day {
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
};

void printDay(Day day) {
    switch (day) {
        case Day::Sunday: std::cout << "Sunday" << std::endl; break;
        case Day::Monday: std::cout << "Monday" << std::endl; break;
        case Day::Tuesday: std::cout << "Tuesday" << std::endl; break;
        case Day::Wednesday: std::cout << "Wednesday" << std::endl; break;
        case Day::Thursday: std::cout << "Thursday" << std::endl; break;
        case Day::Friday: std::cout << "Friday" << std::endl; break;
        case Day::Saturday: std::cout << "Saturday" << std::endl; break;
    }
}

int main() {
    Day today = Day::Friday;
    printDay(today); // Outputs "Friday"
    return 0;
}
