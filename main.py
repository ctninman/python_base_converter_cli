from os import system
from random import randint
import json
import prompts
import user_input_functions
import calculation_functions
from display_info_functions import print_txt_file, display_user_stats, detailed_breakdown

### TXT FILES TUTORIALS
num_sys_lines = open("Text_Files/number_systems.txt").read().splitlines()
types_sys_lines = open("Text_Files/types_systems.txt").read().splitlines()
decimal_sys_lines = open("Text_Files/decimal_system.txt").read().splitlines()
binary_sys_lines = open("Text_Files/binary_system.txt").read().splitlines()
hexadecimal_sys_lines = open("Text_Files/hexadecimal_system.txt").read().splitlines()
dec_to_other_base_lines = open("Text_Files/decimal_to_other_base.txt").read().splitlines()
other_base_to_dec_lines = open("Text_Files/other_base_to_decimal.txt").read().splitlines()

### VARIABLES
main_menu_options = ['1','2','3','4']
tutorial_menu_options = ['1','2','3','4','5','6','7','8']
challenge_menu_options = ['1','2','3']

### ENTER PROGRAM
run_program = False
if __name__ == "__main__":
	run_program = True

while run_program:

	system('clear')
	menu_selection = user_input_functions.menu_selection(prompts.main_menu_prompt, main_menu_options)
	
### EXIT PROGRAM (MAIN MENU - CHOICE 4)
	if menu_selection == 4:
		system('clear')
		run_program = False
		print(prompts.exit_prompt)


### SHOW TUTORIALS (MAIN MENU - CHOICE 1)
	while menu_selection == 1:
		system('clear') 
		sub_selection = user_input_functions.menu_selection(prompts.tutorial_prompt, tutorial_menu_options)


#'BEN'*** PYTHON PREFERRED IF ELSE VS MATCH 
		### PRINT TUTORIAL BASED ON USER INPUT
		match sub_selection:
			case 1:
				print_txt_file(num_sys_lines)
				user_input_functions.go_back()
			case 2:
				print_txt_file(types_sys_lines)
				user_input_functions.go_back()
			case 3:
				print_txt_file(decimal_sys_lines)
				user_input_functions.go_back()
			case 4:
				print_txt_file(binary_sys_lines)
				user_input_functions.go_back()
			case 5:
				print_txt_file(hexadecimal_sys_lines)
				user_input_functions.go_back()
			case 6:
				print_txt_file(dec_to_other_base_lines)
				user_input_functions.go_back()
			case 7:
				print_txt_file(other_base_to_dec_lines)
				user_input_functions.go_back()
			case 8:
				menu_selection = 0
				break


### RUN NUMBER CONVERTER (MAIN MENU - CHOICE 2)
	while menu_selection == 2:
		
		### SERIES OF FUNCTIONS TO SET NUMBER, CONVERTED NUMBER, AND LIST OF PLACE VALUES
		base_entered = user_input_functions.select_base(prompts.which_base_prompt)
		num_entered = user_input_functions.accept_number(prompts.number_to_convert_prompt)
		calculated_place_values = calculation_functions.determine_place_values(num_entered, base_entered)
		converted_num = calculation_functions.num_to_new_base(num_entered, calculated_place_values) if base_entered < 10 else calculation_functions.num_to_new_base_greater_than_ten(num_entered, calculated_place_values)
		interval_calculate = 1 if num_entered < 500 else int(num_entered * 0.003) + 1

		### BRIEFLY DISPLAY EACH NUMBER CONVERTED UP TO THE INPUT NUMBER
		for num in range(1 , num_entered, interval_calculate):
			
			temp_place_values = calculation_functions.determine_place_values(num, base_entered)
			
			if base_entered < 10:
				converted_num_to_print = str(calculation_functions.num_to_new_base(num, temp_place_values))
			else:
				converted_num_to_print = str(calculation_functions.num_to_new_base_greater_than_ten(num, temp_place_values))

			converted_length_difference = len(str(converted_num)) - len(str(converted_num_to_print))
			base_ten_length_difference = len(str(num_entered)) - len(str(num))

			print(f"*** BASE 10 ***")
			print(f"{' ' * base_ten_length_difference}{num}")
			print(f"\n*** BASE {base_entered} ***")
			print(f"{' ' * converted_length_difference}{converted_num_to_print}")
			
			user_input_functions.clear_terminal()

		### DISPLAY INPUT NUMBER CONVERTED INTO NEW BASE
		print(f"*** BASE 10 ***")
		print(f"{num_entered}\n")
		print(f"*** BASE {base_entered} ***")
		print(f"{converted_num}\n")
		
		### DISPLAY OPTION MENU
		print("Enter 'm' to return to the main menu")
		print("Enter '?' for a detailed breakdown")
		user_selction = input("Enter any other key to continue:\n")
		
		### RE_ENTER CONVERSION LOOP
		if user_selction.lower() == 'm':
			menu_selection = 0
		### VIEW BREAKDOWN OF CONVERTED NUMBER
		elif user_selction == '?':
			system('clear')
			detailed_breakdown([str(x) for x in calculated_place_values], converted_num, base_entered, num_entered)
			#'Ben' {x : str(x) for x in calculated_place_values if x < 7}
			# map = {}
			# for x in calculated_place_values:
			# 	if x < 7:
			# 		map[x] = str(x)

			print("\nEnter 'm' to return to main menu")
			user_selction = input('Enter any other key to convert another number\n')
		
			if user_selction.lower() == 'm':
				menu_selection = 0
				continue
		### RETURN TO MAIN MENU	
		else:
			pass


### CONVERSION CHALLENGE MODE (MAIN MENU - CHOICE 3)
	while menu_selection == 3:
		### LOAD AND SAVE USER SCORE DATA FROM JSON FILE 
		with open('user_scores.json') as json_file:
			scores = json.load(json_file)

		challenge_selection = user_input_functions.menu_selection(prompts.challenge_prompt, challenge_menu_options)

		if challenge_selection == 1:
			
			### SELECT A BASE AND NUMBER FOR USER TO ATTEPMT TO CONVERT INTO DECIMAL
			base_chosen = user_input_functions.select_base(prompts.which_base_prompt)
			challenge_min, challenge_max = calculation_functions.difficulty_level(scores['total']['correct'], scores['total']['answered'])
			num_to_convert = randint(challenge_min, challenge_max)
			calc_place_values = calculation_functions.determine_place_values(num_to_convert, base_chosen)
			
			if base_chosen < 10:
				converted_num = calculation_functions.num_to_new_base(num_to_convert, calc_place_values) 
			else:
				converted_num = calculation_functions.num_to_new_base_greater_than_ten(num_to_convert, calc_place_values) 

			system('clear')
			user_response = input(f"The number {converted_num} in base{base_chosen} is equal to what number in base10 (decimal)?\n\n")
			system('clear')
			
			### USER ENTERS CORRECT RESPONSE
			if user_response == str(num_to_convert):
				updated_scores = calculation_functions.update_scores(scores, base_chosen, True)
				#'Ben' dictionaries point to same object in memory
				#  print(f"{scores == updated_scores}")

				print("CORRECT!!! Nice job!")
			### USER ENTERS INCORRECT RESPONSE
			else:
				updated_scores = calculation_functions.update_scores(scores, base_chosen, False)
				print("Sorry, that is incorrect.\n")
			print(f"{converted_num} in base{base_chosen} equals {num_to_convert} in our decimal system.\n")
			detailed_breakdown([str(x) for x in calc_place_values], converted_num, base_chosen, num_to_convert)
			
			### REWRITE SCORES IN JSON FILE
			out_file = open("user_scores.json", "w")
			json.dump(updated_scores, out_file, indent = 4, sort_keys = False)
			out_file.close()

			input("Press ENTER to continue")

		### SELECT FROM MENU - VIEW ALL USER SCORES
		elif challenge_selection == 2:
			display_user_stats(scores)

			input("\nPress ENTER to continue")

		### RETURN TO MAIN MENU
		elif challenge_selection == 3:
			menu_selection = 0



