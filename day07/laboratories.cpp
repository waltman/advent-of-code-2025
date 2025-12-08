#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <errno.h>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>

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
    int *beams = new int[ncols];
    fill(beams, beams+ncols, 0);
    for (size_t col = 0; col < ncols; col++)
        if (grid[0][col] == 'S') {
            beams[col] = 1;
            start_col = col;
            break;
        }

    // track the beam as if goes down
    for (size_t row = 1; row < nrows; row++) {
        unique_ptr<int[]> new_beams(new int[ncols]);
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

        for (size_t i = 0; i < ncols; i++)
            beams[i] = new_beams[i];
    }
    cout << "Part 1: " << part1 << endl;
        
    unsigned long long *counts = new unsigned long long[ncols];
    unsigned long long *new_counts = new unsigned long long[ncols];
    fill(counts, counts+ncols, 0);
    counts[start_col] = 1;
    for (size_t row = 1; row < nrows; row++) {
        fill(new_counts, new_counts+ncols, 0);
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
        copy(new_counts, new_counts+ncols, counts);
    }

    for (size_t i = 0; i < ncols; i++)
        part2 += counts[i];
    
    cout << "Part 2: " << part2 << endl;
    
}
