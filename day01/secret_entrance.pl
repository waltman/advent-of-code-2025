#!/usr/bin/env perl
use v5.40;

my ($part1, $part2);
my ($pos, $pos2) = (50, 50);

while (<<>>) {
    my $sign = substr($_, 0, 1) eq 'R' ? 1 : -1;
    my $cnt = substr($_, 1) * $sign;
    $pos = ($pos + $cnt) % 100;
    $part1++ unless $pos;

    my $on_zero = $pos2 == 0;
    $pos2 += $cnt;

    $part2++ if ($pos2 <= 0 && ! $on_zero);
    $part2 += int(abs($pos2) / 100);
    $pos2 %= 100;
}

say "Part 1: $part1";
say "Part 2: $part2";
