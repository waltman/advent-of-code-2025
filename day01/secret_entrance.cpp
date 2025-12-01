#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int mod(const int a, const int b) {
    return (a % b + b) % b;
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];
    int part1 = 0;
    int part2 = 0;
    int pos1 = 50;
    int pos2 = 50;

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    string line;
    while (!infile.eof()) {
        getline(infile, line);
        if (line.size() < 2)
            continue;
        const int dir = line[0] == 'R' ? 1 : -1;
        const int cnt = stoi(line.substr(1)) * dir;
        pos1 = (pos1 + cnt) % 100;
        if (pos1 == 0)
            part1++;

        const bool on_zero = (pos2 == 0);
        pos2 += cnt;

        if (pos2 <= 0 && !on_zero)
            part2++;

        part2 += abs(pos2) / 100;
        pos2 = mod(pos2, 100);
    }

    cout << "Part 1: " << part1 << endl;
    cout << "Part 2: " << part2 << endl;
}
