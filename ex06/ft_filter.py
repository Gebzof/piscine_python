def main():
    ages = [5, 12, 18, 24, 35]
    adults = ft_filter(myFunc, ages)
    for x in adults:
        print(x)

def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which
function(item) is true.  If function is None, return the items that
are true. """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
    print(ft_filter.__doc__)