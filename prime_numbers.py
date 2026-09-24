"""Display prime numbers in an inclusive range."""

from math import isqrt


def is_prime(number: int) -> bool:
    """Return True when *number* is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def primes_between(first: int, second: int) -> list[int]:
    """Return all prime numbers between two inclusive bounds."""
    start, end = sorted((first, second))
    return [number for number in range(start, end + 1) if is_prime(number)]


def read_integer(prompt: str) -> int:
    """Read an integer from the user, repeating until input is valid."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")


def main() -> None:
    """Read two bounds and display the prime numbers between them."""
    first = read_integer("Enter the first number: ")
    second = read_integer("Enter the second number: ")
    primes = primes_between(first, second)

    if primes:
        print(f"Prime numbers between {first} and {second}: {primes}")
    else:
        print(f"There are no prime numbers between {first} and {second}.")


if __name__ == "__main__":
    main()