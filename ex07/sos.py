import sys
NESTED_MORSE = {"": "/",
				"A": ".-",
				"B": "-..",
				"C": "-.-.",
				"D": "-..",
				"E": ".",
				"F": "..-..",
				"G": "--.",
				"H": "....",
				"I": "..",
				"J": ".---",
				"K": "-.-",
				"L": ".-..",
				"M": "--",
				"N": "-.",
				"O": "---",
				"P": ".--.",
				"Q": "--.-",
				"R": ".-.",
				"S": "...",
				"T": "-",
				"U": "..-",
				"V": "...-",
				"W": ".--",
				"X": "-..-",
				"Y": "-.--",
				"Z": "--..",
				"0": "-----",
				"1": ".----",
				"2": "..---",
				"3": "...--",
				"4": "....-",
				"5": ".....",
				"6": "-....",
				"7": "--...",
				"8": "---..",
				"9": "----."
				}

def main():
	"""
	function main :
	This functions prints tests and does the error handling before starting the code
	"""
	transform()
	print(main.__doc__)

def transform():
	string = sys.argv[1].lower()
	for i, c in enumerate(string):
		if i == len(string) - 1:
			end = ""
		else:
			end = " "
		for cle, code in NESTED_MORSE.items():
			if c == cle.lower():
				print(code, end = end)


if __name__ == "__main__":
	main()