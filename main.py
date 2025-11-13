"""Module pour trouver et afficher les nombres premiers."""
from math import isqrt


def isprime(p):
    """Vérifie si un nombre est premier."""
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    # Vérifier seulement les nombres impairs jusqu'à sqrt(p)
    for i in range(3, isqrt(p) + 1, 2):
        if p % i == 0:
            return False
    return True


def main():
    """Affiche tous les nombres premiers jusqu'à 100."""
    primes = [n for n in range(2, 100) if isprime(n)]
    print(", ".join(map(str, primes)) + ", ")


if __name__ == "__main__":
    main()
