#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <errno.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct Range {
    unsigned long long start;
    unsigned long long end;
} Range;

const Range parse_range(string range_str) {
    Range range = {.start = 0, .end = 0};
    int state = 1;
    for (char c : range_str)
        if (c == '-')
            state = 2;
        else if (state == 1)
            range.start = range.start * 10 + c - '0';
        else
            range.end = range.end * 10 + c - '0';

    return range;
}

void merge_ranges(vector<Range> &ranges, vector<Range> &merged) {
    sort(ranges.begin(), ranges.end(), [](Range a, Range b) {return a.start < b.start;});
    merged.push_back(ranges[0]);

    for (size_t i = 1; i < ranges.size(); i++) {
        Range curr = ranges[i];
        size_t j = merged.size() - 1;
        Range last = merged[j];

        if (curr.start <= last.end)
            merged[j].end = (curr.end > last.end) ? curr.end : last.end;
        else
            merged.push_back(curr);
    }
}

void parse_input(string fname, vector<Range> &ranges, vector<unsigned long long> &ids) {
    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(errno);
    }

    string line;
    int state = 1;
    while (!infile.eof()) {
        getline(infile, line);
        if (line.size() == 0)
            state = 2;
        else if (state == 1)
            ranges.push_back(parse_range(line));
        else
            ids.push_back(stoll(line));
    }
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];
    vector<Range> ranges;
    vector<unsigned long long> ids;

    parse_input(fname, ranges, ids);

    unsigned long long part1 = 0;
    for (auto val : ids)
        for (auto range : ranges)
            if (range.start <= val && val <= range.end) {
                part1++;
                break;
            }
    cout << "Part 1: " << part1 << endl;

    vector<Range> merged;
    merge_ranges(ranges, merged);
    unsigned long long part2 = 0;
    for (auto range : merged) {
        part2 += range.end - range.start + 1;
    }
    cout << "Part 2: " << part2 << endl;
}
