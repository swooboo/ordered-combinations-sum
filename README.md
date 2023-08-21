# Counting ordered combinations of numbers that sum up to a target number

## Problem statement
Given a set of positive integers, and a non-negative target sum, find all the
combinations of the numbers from the set that sum up to the target sum, order
is significant. For example, for {1,2}, 5, there is 8 combinations.

## Solution using polynomials
Using polynomes to represent different sums and lengths of combinations. Each
polynome represents the numbers of ways to sum up to all possible sums, depending
on the length of the combination. For each length, there is one polynome that
will contain all the counts for each sum that's accessible through a combination.
For example, the polynome P(x)=(x^2+x)(x^2+x) represents a combination of two
numbers from the set {1,2}. When expanded, we get P(x)=x^4+2*x^3+x^2. In this
form, the coefficients are the number of combinations, and the matching monome
power is the sum for which the number of combination is counted. From the above
example, there's 1 way to sum to 4, 2 ways to sum to 3 and 1 way to sum to 2,
using a combination of 2 numbers from the set {1,2}.

### Example run:
```
In [1]: poly_sum_ordered_reps([1,2,3],1000)
Out[1]: 
2758842807766486252615892411656158645133100149652696210351601845036392978912293462801016485671033253921841350537004356434253826361707295202024537559785200706502368152965047761644352316799391470273906561574500883480570560512982435681502330814068718832813973880527601

In [2]: 
```
