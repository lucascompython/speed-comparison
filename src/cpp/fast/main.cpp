
#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
#include <math.h>
using namespace std;

int main() {
    //start timer
    auto start = chrono::high_resolution_clock::now();
    //read from file
    ifstream file("../../rounds.txt");
    int rounds = 0;
    file >> rounds;
    file.close();

    vector<bool> total(rounds + 1, true);



    for (int i = 2; i <= sqrt(rounds); i++) {
        if (total[i] == true) {
            for (int j = i * i; j < rounds; j += i) {
                total[j] = false;
            }
        }
    }

    int primes = 0;
    for (int k = 2; k < rounds; k++) {
        if (total[k] == true) {
            primes++;
        }
    }
    //end timer
    auto end = chrono::high_resolution_clock::now();
    auto milliseconds = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    
    cout << __VERSION__ << " " << (float)milliseconds / 1000;

    return 0;
}
