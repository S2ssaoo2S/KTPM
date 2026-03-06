import math
import sys

def isprime(n: int) -> bool:
    if n < 2:
        raise ValueError("n must be greater than 2")

    for i in range(3, math.isqrt(n)+1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(isprime(4))