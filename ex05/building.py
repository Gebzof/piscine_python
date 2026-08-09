import string, sys

def main():
	"""
	function main :
    This functions prints tests and does the error handling before starting the code
	"""
	string = get_string()
	cal(string)
	print(main.__doc__)

def get_string():
	"""
	function get_string:
    This function looks for a string, if no string is given as argv[1] it uses a default one
    This function returns the string in main
	"""
	if len(sys.argv) > 1:
		string = str(sys.argv[1])
	else:
		string = str("Hello World! ")
		print(f"What is the text to count?")
		print(string)
	print(get_string.__doc__)
	return string


def cal(my_str):
	"""
	function cal :
    This function calculates and prints the number of char in a string that are either uppercase, lowercase, a whitespace, a digits and or a form of punctuation
    It uses the function sum to add up to index any type of char, and uses a loop to increment every char in the string
	"""
	nbr_len = len(my_str)
	nb_upper = sum(1 for c in my_str if c.isupper())
	nb_lower = sum(1 for c in my_str if c.islower())
	nb_ponct = sum(1 for c in my_str if c in string.punctuation)
	nb_spaces = sum(1 for c in my_str if c.isspace())
	nb_digits = sum(1 for c in my_str if c.isdigit())

	print(f"the text contains {nbr_len} characters")
	print(f"{nb_upper} upper letters")
	print(f"{nb_lower} lower letters")
	print(f"{nb_ponct} lower punctuation marks")
	print(f"{nb_spaces} lower spaces")
	print(f"{nb_digits} lower digits")

	print(cal.__doc__)

if __name__ == "__main__":
	main()