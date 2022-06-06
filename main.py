# Problem 73:
#     Counting Fractions in a Range
#
# Description:
#     Consider the fraction, n/d, where n and d are positive integers.
#     If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
#
#     If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#         1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, [ 3/8, 2/5, 3/7 ], 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#     It can be seen that there are 3 fractions between 1/3 and 1/2.
#
#     How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

from math import ceil, floor, gcd


def main(d_max):
    """
    Returns the number of distinct proper reduced fractions having denominator at most `d_max`, which are
      fractions `n/d` (where n,d are natural numbers), such that n < d, and n,d are relatively prime,
      where 1/3 < n/d < 1/2.

    Args:
        d_max (int): Natural number, greater than 1

    Returns:
        (int): Count of distinct proper reduced fractions n/d between 1/3 and 1/2 (exclusive), where d ≤ `d_max`.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(d_max) == int and d_max > 1

    count = 0
    for d in range(2, d_max+1):
        for n in range(floor(d/3)+1, ceil(d/2)):  # Stay between 1/3 and 1/2
            count += (gcd(n, d) == 1)  # Only count reduced fractions
    return count


if __name__ == '__main__':
    max_denominator = int(input('Enter a natural number (greater than 1): '))
    fraction_count = main(max_denominator)
    print('Number of distinct reduced proper fractions between 1/3 and 1/2, for d ≤ {}:'.format(max_denominator))
    print('  {}'.format(fraction_count))
