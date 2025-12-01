#!/usr/bin/env perl
use v5.40;

my ($part1, $part2);
my ($pos, $pos2) = (50, 50);

while (<<>>) {
    my $dir = substr($_, 0, 1) eq 'R' ? 1 : -1;
    my $cnt = substr($_, 1);
    $pos = ($pos + ($cnt * $dir)) % 100;
    $part1++ unless $pos;

    for my $i (1..$cnt) {
        $pos2 = ($pos2 + $dir) % 100;
        $part2++ unless $pos2;
    }
}

say "Part 1: $part1";
say "Part 2: $part2";
