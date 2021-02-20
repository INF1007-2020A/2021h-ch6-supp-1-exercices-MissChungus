#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):

	return [max(element) for element in numbers]

def join_integers(numbers):
	entier = ''
	for number in numbers:
		entier += str(number)
	entier = int(entier)

	return entier

def generate_prime_numbers(limit):
	return [0]

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	result = []
	for num in range(1, num_combinations + 1):
		if excluded_multiples == None:
			for letter in strings:
				result.append(letter + str(num))
		else:
			if num % excluded_multiples != 0:
				for letter in strings:
					result.append(letter + str(num))

	return result

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
