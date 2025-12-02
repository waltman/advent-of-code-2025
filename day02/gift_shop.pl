#!/usr/bin/env perl
use v5.42;

my @ranges;
while (<<>>) {
    chomp;
    for my $pair (split ',') {
        push @ranges, [split '-', $pair];
    }
}

my ($part1, $part2);
for my $range (@ranges) {
    for my $i ($range->[0]..$range->[1]) {
	$part1 += $i if $i =~ /^(\d+)\1$/;
	$part2 += $i if $i =~ /^(\d+)\1+$/;
    }
}

say "Part 1: $part1";
say "Part 2: $part2";
