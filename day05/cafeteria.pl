#!/usr/bin/env perl
use v5.42;
use List::Util qw(max sum);

sub merge_ranges(@ranges) {
    my @r = sort {$a->[0] <=> $b->[0]} @ranges;
    my @result = ($r[0]);

    for my $curr (@r[1..$#r]) {
        my $last = $result[-1];
        if ($curr->[0] <= $last->[-1]) {
            $last->[1] = max($last->[1], $curr->[1]);
        } else {
            push @result, $curr;
        }
    }
    return @result;
}

my (@ranges, @ids);
my $state = 1;

while (<<>>) {
    chomp;
    if (/^$/) {
        $state = 2;
    } elsif ($state == 1) {
        push @ranges, [split '-'];
    } else {
        push @ids, $_;
    }
}

my $part1;
for my $id (@ids) {
    for my $range (@ranges) {
        if ($range->[0] <= $id <= $range->[1]) {
            $part1++;
            last;
        }
    }
}

say "Part 1: $part1";

my @merged = merge_ranges(@ranges);
my $part2 = sum(map {$_->[1] - $_->[0] + 1} @merged);
say "Part 2: $part2";
