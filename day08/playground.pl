#!/usr/bin/env perl
use v5.42;
use autodie;
use Graph::Undirected;
use List::Util qw(sum);

sub dist($b1, $b2) {
    return sum( map { ($b1->[$_] - $b2->[$_]) ** 2 } 0..2);
}

my ($fname, $num_juncs) = @ARGV;
open my $fh, '<', $fname;
my @boxes;
while (<$fh>) {
    chomp;
    push @boxes, [split ','];
}

my $g = Graph::Undirected->new;
for my $box (@boxes) {
    $g->add_vertex("@$box");
}

my %dists;
for my $i (0..$#boxes-1) {
    my $b1 = $boxes[$i];
    for my $j ($i+1..$#boxes) {
        my $b2 = $boxes[$j];
        $dists{"@$b1,@$b2"} = dist($b1, $b2);
    }
}

my @sorted = sort {$dists{$a} <=> $dists{$b}} keys %dists;
for my $i (0..$num_juncs-1) {
    my ($b1, $b2) = split ',', $sorted[$i];
    $g->add_edge($b1, $b2);
}
my @cc = $g->connected_components;
my @sorted_cc = sort { @$b <=> @$a } @cc;
my $part1 = 1;
for my $i (0..2) {
    $part1 *= @{$sorted_cc[$i]};
}

say "Part 1: $part1";

my $i = $num_juncs;
my ($b1, $b2);
while (scalar $g->connected_components > 1) {
    ($b1, $b2) = split ',', $sorted[$i];
    $g->add_edge($b1, $b2);
    $i++;
}

my @b1 = split ' ', $b1;
my @b2 = split ' ', $b2;
say "Part 2: ", $b1[0] * $b2[0];
