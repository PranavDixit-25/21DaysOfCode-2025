import sys


def find_sum(lst: list[int]) -> int:
    "Finds sum of elements of the list."

    # This is an alternative to the built in `sum` method

    result = 0
    for item in lst:
        result += item

    return result


def main() -> None:
    "The entry point of the program."

    try:
        n = int(input("Enter the size of the array: "))
    except ValueError:
        print("Invalid size!")
        sys.exit(-1)

    # Check if length is valid
    if n <= 0:
        print("Size must be greater 0.")
        sys.exit(-1)

    nums: list[int] = []

    print("+--Enter the values--+")
    for _ in range(n):
        try:
            num = int(input("> "))
        except ValueError:
            print("Invalid value!")
            sys.exit(-1)

        nums.append(num)

    result = find_sum(nums)

    print(f"Sum: {result}")


if __name__ == "__main__":
    main()
