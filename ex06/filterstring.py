from ft_filter import ft_filter
import sys

def main():
    """
    Function: Filterstring

    A program that accepts two arguments, a string S and an integer N.
    The program outputs a list of word from S that have a length greater than N.
    """

    length = int(len(sys.argv))

    assert length == 3, "the arguments are bad"
    assert sys.argv[2].isdigit() == True, "the arguments are bad"

    list1 = sys.argv[1].split()

    funky = lambda a: a > N

    N = int(sys.argv[2])
    S = [item for item in list1 if funky(len(item))]

    print(f"{S}")


if __name__ == "__main__":
    main()
    print(main.__doc__)