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

my $dups = Set::Scalar->new(map {$_ x 2} 1..99_999);
my $pairs = $dups->clone;

$dups->insert(map {$_ x 3} 1..999);

for my $copies (4..5) {
    $dups->insert(map {$_ x $copies} 1..99);
}

for my $copies (6..10) {
    $dups->insert(map {$_ x $copies} 1..9);
}

my $part1 = sum map {(Set::Scalar->new($_->[0]..$_->[1]) * $pairs)->members} @ranges;
my $part2 = sum map {(Set::Scalar->new($_->[0]..$_->[1]) * $dups)->members} @ranges;

say "Part 1: $part1";
say "Part 2: $part2";
