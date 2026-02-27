import numpy as np

import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    result = np.array(nums, dtype=object)
    mask_fizz = (nums % 3 == 0)
    mask_buzz = (nums % 5 == 0)
    mask_fizzbuzz = mask_fizz & mask_buzz
    result[mask_fizzbuzz] = "fizzbuzz"
    result[mask_fizz & ~mask_buzz] = "fizz"
    result[mask_buzz & ~mask_fizz] = "buzz"
    return result
