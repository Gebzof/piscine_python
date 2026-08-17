import sys

length = int(len(sys.argv))

assert length <= 2, "more than one argument is provided"
assert length != 1, "no argument is provided"
assert type(sys.argv[1]) == int, "argument is not an integer"

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
elif int(sys.argv[1]) % 2 == 1:
    print("I'm Odd.")