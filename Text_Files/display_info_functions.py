from email.policy import default
from os import system

num_sys_lines = open("Text_Files/number_systems.txt").read().splitlines()
types_sys_lines = open("Text_Files/types_systems.txt").read().splitlines()
decimal_sys_lines = open("Text_Files/decimal_system.txt").read().splitlines()
binary_sys_lines = open("Text_Files/binary_system.txt").read().splitlines()
hexadecimal_sys_lines = open("Text_Files/hexadecimal_system.txt").read().splitlines()
dec_to_other_base_lines = open("Text_Files/decimal_to_other_base.txt").read().splitlines()
other_base_to_dec_lines = open("Text_Files/other_base_to_decimal.txt").read().splitlines()



### FUNCTION TO PRINT TXT FILE
def print_txt_file(a_file):
	system('clear')
	
	for line in a_file:
		print(line)
	
	print('\n')
	return 0


### FUNCTION TO PRINT USER CHALLENGER SCORES
def display_user_stats(scores_dict):
	system('clear')
	
	for score in scores_dict.values():	
		num_correct = score['correct']
		num_answered = score['answered']
		base = score['base'] 
		percent = 0 if num_answered == 0 else float(num_correct/num_answered) * 100
		rounded_percent = round(percent, 2)
		
		if base == 101:
			print(f'Total: {num_correct} / {num_answered}   {rounded_percent}%')
		else:
			print(f"Base{base}: {num_correct} / {num_answered}   {rounded_percent}%")

	return 0


### FUNCTION FOR PRINTING A DETAILED EXPLANATION OF SINGLE CONVERSION
def detailed_breakdown(arr_place_val, num_as_string, base, num):
	# system('clear')
	i = 0
	j = 0

	print(f'Place values in Base {base}: \n', end = '')
	# print(arr_place_val)
	print(f"{', '.join(arr_place_val)}\n")
	print(f"{num_as_string} : Base{base}\n")
	
	for place_value in arr_place_val:
		digit = convert_alpha_to_num(num_as_string[i])
		if i < len(arr_place_val) - 1:
			print(f'({digit} x {place_value} = {int(digit) * int(place_value)})', end = ' + ')
			i += 1
		else:
			print(f'({digit} x {place_value} = {int(digit) * int(place_value)})', end = ' =\n\n')
	
	for place_value in arr_place_val:
		digit2 = int(convert_alpha_to_num(num_as_string[j]))
		if j < len(arr_place_val) - 1:
			print(f'{digit2 * int(place_value)}', end = ' + ')
			j += 1
		else:
			print(f'{digit2 * int(place_value)}', end = ' =')

	print(f" {num}\n")
	print(f"{num_as_string} : Base{base} = {num} : Base10")

	return 0


### FUNCTION TO CHANGE DIGITS GREATER THAN 9 INTO EQUIVALENT LETTER
def convert_alpha_to_num(character):
	match character:
		case 'A':
			return '10'
		case 'B':
			return '11'
		case 'C':
			return '12'
		case 'D':
			return '13'
		case 'E':
			return '14'
		case 'F':
			return '15'
		case _:
			return character