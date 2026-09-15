"""
The solution for the Gluttinous George problem in Kattis.
Jon C. - October 2025
"""

def main() -> None:
    # input
    left, question, right = input().split(" ") # could also split on " ? "

    # proceessing
    left = int(left)
    right = int(right)

    # processing and output
    if left < right:
        print("<")
    elif left > right:
        print(">")
    else:
        print("Goggi svangur!")

if __name__ == "__main__":
    main()
