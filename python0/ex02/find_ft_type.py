def all_thing_is_obj(object: any) -> int:
    typus = type(object)
    if (typus is list):
        print(f"List : {typus}")
    elif (typus is tuple):
        print(f"Tuple : {typus}" )
    elif (typus is set):
        print(f"Set : {typus}" )
    elif (typus is dict):
        print(f"Dict : {typus}" )
    elif (typus is str):
        print(f"{object} is in the kitchen : {typus}")
    else:
        print("Type not found")
    return 42