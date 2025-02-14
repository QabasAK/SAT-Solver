#include <iostream>
#include <chrono>
using namespace std; 
using namespace std::chrono;

int main() {

    //you can use high resolution clock or steady clock 
    auto start = steady_clock::now();
        //algorithm 
    auto end = steady_clock::now();

    chrono::duration<double> algo_time = end - start;
    cout << "Time: " << algo_time.count() << "s\n";

    return 0;
}
