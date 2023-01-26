from os import system

### FUNCTION TO CREATE LIST OF PLACE VALUES IN SELECTED BASE
def determine_place_values(num, num_system):

	list_of_place_values = []
	next_place_value = 1

	while next_place_value <= num:
		list_of_place_values.append(next_place_value)
		next_place_value = next_place_value * num_system

	return list_of_place_values


### FUNCTION TO CONVERT DECIMAL NUMBER TO ANOTHER BASE (BASE NUMBER LESS THAN 10)
def num_to_new_base(num, list_place_val):

	if num == 0:
		return '0'
	if num == 1:
		return '1'
	
	list_place_val.reverse()
	remaining_balance = num
	list_new_system_values = []

	for place_value in list_place_val:
		if remaining_balance < place_value:
			digit = 0
		else:
			digit = int(remaining_balance / place_value)
		
		list_new_system_values.append(digit)
		remaining_balance -= digit * place_value

	list_as_strings = [str(i) for i in list_new_system_values]
	
	return ''.join(list_as_strings)


### FUNCTION TO CHANGE A DIGIT 10 OR GREATER INTO LETTER
def digit_greater_than_nine(num): # TODO: consider if/elif/else vs match
	match num:
		case 10:
			return "A"
		case 11:
			return "B"
		case 12:
			return "C"
		case 13:
			return "D"
		case 14:
			return "E"
		case 15:
			return "F"
		case _:
			return num


### FUNCTION TO CONVERT DECIMAL NUMBER TO ANOTHER BASE (BASE NUMBER 10 OR GREATER)
def num_to_new_base_greater_than_ten(num, list_place_val):

	if num == 0:
		return '0'
	if num == 1:
		return '1'
	
	list_place_val.reverse()
	remaining_balance = num
	list_new_system_values = []

	for place_value in list_place_val:
		if remaining_balance < place_value:
			digit = '0'
			list_new_system_values.append(digit)
		else:
			unmodified_digit = int(remaining_balance / place_value) # // for integer division
			
			if unmodified_digit < 10: 
				digit = str(unmodified_digit)
				list_new_system_values.append(digit)
			else:
				digit = digit_greater_than_nine(unmodified_digit)
				list_new_system_values.append(digit)
			
			remaining_balance -= unmodified_digit * place_value
	
	return ''.join(list_new_system_values)


### FUNCTION TO UPDATE USER_SCORES DICTIONARY
def update_scores(scores, num_of_base, correct_bool):
	scores[f'base{num_of_base}']['answered'] += 1
	scores['total']['answered'] += 1
	if correct_bool:
		scores[f'base{num_of_base}']['correct'] += 1
		scores['total']['correct'] += 1
	return scores


def difficulty_level(num_correct, num_answered):
	if num_answered < 10 or num_correct / num_answered < 0.5:
		return 10, 100
	elif num_answered < 25 and num_correct / num_answered > 0.5:
		return 50, 500
	else:
		return 100, 1000

