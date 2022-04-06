#include <iostream>
#include <fstream>
#include <chrono>


using namespace std;

int main() {
    //start timer
    auto start = chrono::high_resolution_clock::now();
    //read from file
    ifstream file("../rounds.txt");
    string str((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
    int rounds = stoi(str);
    int primes, composites;

    for(int num = 0; num <= rounds; num++){
        int ctr = 0;

        for(int i = 2; i <= num / 2; i++){
            if(num % i == 0){
                ctr++;
                composites++;
                break;
            }
        }

        if(ctr == 0 && num != 1){
            primes++;
        }
    }
    //end timer
    auto end = chrono::high_resolution_clock::now();
    auto milliseconds = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    

    cout << __VERSION__ << " " << (float)milliseconds / 1000;

    return 0;
}