#!/usr/bin/env python3

def classify(number):
    list_of_factors = [i for i in range(1, number) if number % i == 0]

    if number < 1:
      raise ValueError(f'An error occurred due to the value. Make sure number is greater than 0 (input was {number}).')

    if sum(list_of_factors) == number:
      return "perfect"
    elif sum(list_of_factors) > number:
      return "abundant"
    elif sum(list_of_factors) < number:
      return "deficient"
    elif number <= 0:
        raise Exception("ValueError")


