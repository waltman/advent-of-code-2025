#!/usr/bin/env perl
use v5.42;
use Set::Scalar;
use List::Util qw(sum);

my @ranges;
while (<<>>) {
    chomp;
    for my $pair (split ',') {
        push @ranges, [split '-', $pair];
    }
}

my %pairs = map {$_ x 2 => 1} 1..99_999;
my %dups = map {$_ x 2 => 1} 1..99_999;

$dups{$_ x 3} = 1 for 1..999;
for my $copies (4..5) {
    $dups{$_ x $copies} = 1 for 1..99;
}

for my $copies (6..10) {
    $dups{$_ x $copies} = 1 for 1..9;
}

my ($part1, $part2);
for my $range (@ranges) {
    for my $i ($range->[0]..$range->[1]) {
        $part1 += $i if defined $pairs{$i};
        $part2 += $i if defined $dups{$i};
    }
}

say "Part 1: $part1";
say "Part 2: $part2";
