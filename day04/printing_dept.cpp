#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <errno.h>
#include <string>
#include <vector>

using namespace std;

typedef struct Point {
    const int row;
    const int col;
} Point;

const unsigned int num_adjacent(const vector<string> &grid, const unsigned int row, const unsigned int col) {
    const Point deltas[] = {
        {.row = -1, .col = -1},
        {.row = -1, .col =  0},
        {.row = -1, .col =  1},
        {.row =  0, .col = -1},
        {.row =  0, .col =  1},
        {.row =  1, .col = -1},
        {.row =  1, .col =  0},
        {.row =  1, .col =  1}
    };
    const size_t num_deltas = sizeof(deltas) / sizeof(Point);
    const int nrows = grid.size();
    const int ncols = grid[0].size();
    unsigned int cnt = 0;
    for (unsigned int i = 0; i < num_deltas; i++) {
        const int r = row + deltas[i].row;
        const int c = col + deltas[i].col;
        if (r >= 0 && r < nrows && c >= 0 && c < ncols && grid[r][c] == '@')
            cnt++;
    }
    
    return cnt;
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];
    unsigned int part1 = 0;
    unsigned int part2 = 0;

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
    for (unsigned int r = 0; r < nrows; r++)
        for (unsigned int c = 0; c < ncols; c++) {
            if (grid[r][c] == '@' && num_adjacent(grid, r, c) < 4)
                part1++;
        }

    cout << "Part 1: " << part1 << endl;

    bool done = false;
    while (!done) {
        vector<Point> rolls;
        for (int r = 0; r < (int) nrows; r++)
            for (int c = 0; c < (int) ncols; c++)
            if (grid[r][c] == '@' && num_adjacent(grid, r, c) < 4) {
                part2++;
                rolls.push_back({.row = r, .col = c});
            }
    if (rolls.size() > 0)
        for (auto roll : rolls)
            grid[roll.row][roll.col] = '.';
    else
        done = true;
    }

    cout << "Part 2: " << part2 << endl;
}

