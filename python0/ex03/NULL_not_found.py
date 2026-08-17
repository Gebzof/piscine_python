import math

def NULL_not_found(object: any) -> int:
	typus = type(object)
	if object is None:
	        print(f"Nothing: {object} {typus}")
	        return 0
	elif typus is float and math.isnan(object):
	    print(f"Cheese: {object} {typus}")
	elif typus is int and object == 0:
	    print(f"Zero: {object} {typus}")
	    return 0
	elif typus is str and object == "":
	    print(f"Empty: {object} {typus}")
	    return 0
	elif typus is bool and object is False:
	    print(f"Fake: {object} {typus}")
	    return 0
	else:
	    print("Type not Found")
	    return 1