#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <errno.h>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

typedef map<string, vector<string> > Node;

unsigned long long path_count(Node &nodes, string source, string dest) {
    static map<string, unsigned long long> cache;
    string key = source + "-" + dest;
    unsigned long long result = 0;

    if (source == dest)
        result = 1;
    else if (cache.contains(key))
        return cache[key];
    else {
        for (auto new_source : nodes[source]) {
            result += path_count(nodes, new_source, dest);
        }
    }
    return cache[key] = result;
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];
    Node outputs;
    string line;

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(errno);
    }

    // build the list of nodes
    while (!infile.eof()) {
        getline(infile, line);
        if (line.size() < 1)
            break;
        istringstream iss(line);
        string key, value;
        vector<string> v;
        getline(iss, key, ':');
        getline(iss, value, ' ');
        while (getline(iss, value, ' '))
            v.push_back(value);
        outputs[key] = v;
    }

    unsigned long long part2 =
        path_count(outputs, "svr", "fft") *
        path_count(outputs, "fft", "dac") *
        path_count(outputs, "dac", "out");
    cout << "Part 2: " << part2 << endl;
}
