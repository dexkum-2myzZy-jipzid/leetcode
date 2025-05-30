#!/usr/bin/env python3


# Find all prime numbers up to n (inclusive) using the Sieve of Eratosthenes
def sieve(n):
    # Initialize the is_prime list
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Sieve process
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):  # Mark all multiples of i
                is_prime[j] = False

    # Extract primes
    return [i for i, val in enumerate(is_prime) if val]


if __name__ == "__main__":
    print(sieve(30))
