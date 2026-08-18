import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
        assert any(ele > 0 for ele in height), "Height cannot be null or negative"
        assert len(height) == len(weight), "Height and Weight must have the same length."

        height_squared = list(np.multiply(height, height))
        bmi_list = list(np.divide(weight, height_squared))
        return [float (bmi) for bmi in bmi_list]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
        limit_list = []
        for i in bmi:
                if i > limit:
                        limit_list.append(True)
                else:
                        limit_list.append(False)
        return limit_list