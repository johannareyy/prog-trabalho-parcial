#include <iostream>
#include <string>
using namespace std;

class Date{
public:
    int day{1};
    int month = 1;
    int year = 0;

    Date() {
    }

    Date(int pday, int pmonth, int pyear) : day(pday), month(pmonth), year(pyear){
        day = pday;
        month = pmonth;
        year = pyear;
    }

    Date(int pday, int pmonth, int pyear){
        day = pday;
        month = pmonth;
        year = pyear;
    }
};

class Pessoa{
public:
    string nome = " ";
    int idade = 0;
    bool comendo = false;
    bool falando = false;

    Pessoa (string pnome, int pidade, bool pcomendo = false, bool pfalando = false){
        nome = pnome;
        idade = pidade;
        comendo = pcomendo;
        falando = pfalando;
};

int main() {
    Date d1;
    // d1.day = 1;
    // d1.month = 1;
    // d1.year = 2022;     //mudar somente um parametro

    cout << d1.day << "/" << d1.month << "/" << d1.year;
    return 0;
}