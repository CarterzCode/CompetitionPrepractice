"""
The solution for Amerískur vinnustaður in Kattis.
Jon C. - October 2023
"""

def main() -> None:
    # input
    KM_IN_FOOTBALL_FIELD: float = 0.09144
    n: float = float(input())

    # processing and output
    print(n * KM_IN_FOOTBALL_FIELD)


if __name__ == "__main__":
    main()