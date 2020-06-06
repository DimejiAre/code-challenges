// Project Eulers
/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
*/

function specialPythagoreanTriplet(n) {
    for (let i = 1; i < n; i++) {
        for (let j = 2; j < n; j++) {
            let k = n - (i + j)
            if (k ** 2 === i ** 2 + j ** 2) {
                return i * j * k
            }
        }
    }
}

specialPythagoreanTriplet(1000);