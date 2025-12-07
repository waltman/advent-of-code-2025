#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <errno.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    const string fname = argv[1];
    unsigned int part1 = 0;
    unsigned long long part2 = 0;

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(errno);
    }

    string line;
    vector<string> grid;
    while (!infile.eof()) {
        getline(infile, line);
        if (line.size() > 0)
            grid.push_back(line);
    }
    const size_t nrows = grid.size();
    const size_t ncols = grid[0].size();

    // find the initial column of the beam
    int start_col = 0;
    int beams[ncols];
    memset(beams, 0, sizeof(beams));
    for (size_t col = 0; col < ncols; col++)
        if (grid[0][col] == 'S') {
            beams[col] = 1;
            start_col = col;
            break;
        }

    // track the beam as if goes down
    for (size_t row = 1; row < nrows; row++) {
        int new_beams[ncols];
        memset(new_beams, 0, sizeof(new_beams));
        for (size_t col = 0; col < ncols; col++) {
            if (beams[col]) {
                if (grid[row][col] == '^') {
                    new_beams[col-1] = 1;
                    new_beams[col+1] = 1;
                    part1++;
                } else
                    new_beams[col] = 1;
            }
        }
        memcpy(beams, new_beams, sizeof(beams));
    }
    cout << "Part 1: " << part1 << endl;
        
    unsigned long long counts[ncols];
    unsigned long long new_counts[ncols];
    memset(counts, 0, sizeof(counts));
    counts[start_col] = 1;
    for (size_t row = 1; row < nrows; row++) {
        memset(new_counts, 0, sizeof(new_counts));
        new_counts[0] = counts[0];
        new_counts[ncols-1] = counts[ncols-1];
        for (size_t col = 1; col < ncols-1; col++) {
            if (grid[row][col] == '.')
                new_counts[col] += counts[col];
            else {
                new_counts[col-1] += counts[col];
                new_counts[col+1] += counts[col];
            }
        }
        memcpy(counts, new_counts, sizeof(counts));
    }

    for (size_t i = 0; i < ncols; i++)
        part2 += counts[i];
    
    cout << "Part 2: " << part2 << endl;
    
}
