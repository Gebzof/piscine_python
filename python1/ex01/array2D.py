import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
        original_array = np.array(family)
        print(f"My shape is: {original_array.shape}")
        new_array = original_array[start:end]
        print(f"My new shape is: {new_array.shape}")
        return (new_array.tolist())