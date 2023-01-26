from os import system
from prompts import not_valid_prompt, main_menu_prompt

### FUNCTION TO CREATE BLANK TERMINAL SCREEN
def clear_terminal():
	system('clear')


### FUNCTION TO VALIDATE USER SELECTION IN LIST OF OPTIONS AND RETURN SELECTION AS INTEGER
def menu_selection(prompt, arr_of_nums_as_strings):

	valid_selection = False

	while not valid_selection:
		system('clear')
		print(prompt)
		user_input = input()
		
		if not user_input in arr_of_nums_as_strings:
			print("Please make a valid selection.")
		else:
			valid_selection = True

	return int(user_input)


### FUNCTION TO PAUSE EXECUTION AND THEN CLEAR SCREEN
def go_back():
	input("Press ENTER to go back")
	clear_terminal()


### FUNCTION TO ENSURE USER ENTERS A NUMBER
def accept_number(prompt):
	clear_terminal()
	number_to_convert = input(prompt)

	while not number_to_convert.isnumeric():
		print(not_valid_prompt)
		number_to_convert = input()

	clear_terminal()
	return int(number_to_convert)


### FUNCTION TO ENSURE USER SELECTS VALID BASE NUMBER
def select_base(prompt1):
	clear_terminal()
	print(prompt1)

	acceptable_bases = ['2','3','4','5','6','7','8','9','11','12','13','14','15','16']
	option_selected = input()

	while not option_selected in acceptable_bases:
		print('Please enter valid selection:\n')
		option_selected = input()
	
	base = int(option_selected)

	return base