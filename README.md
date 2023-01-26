# Python CLI Number Base Converter

<!-- INTRO SECTION -->
Python CLI Number Base Converter is a program that aims to help curious users learn about other number systems, and in turn gain a deeper understanding of our decimal (Base 10) number system. 

<img alt='terminal program walkthrough' src=./Images/BaseConverterGif.gif style='max-height: 200px'>

<!-- MAIN FEATURES -->

<details>

<summary>What are the main features of Python CLI Number Base Converter?</summary><br>

Users can choose from three main features of the program:

<img alt='terminal tutorial walkthrough' src=./Images/BaseExplanationGif.gif style='max-height: 200px'><br>
<text>
  Select and view various tuturials about numbers systems and the most common ones
</text><br><hr>
<img alt='terminal program walkthrough' src=./Images/BaseConverterGif.gif style='max-height: 200px'><br>
<text>
  Choose a number base and the program calculates any number into that base, with a detailed breakdown of the conversion
</text><br><hr>
<img alt='terminal program walkthrough' src=./Images/BaseChallengeGif.gif style='max-height: 200px'><br>
<text>
  Take a challenge where they select a number base, receive a random number in that base, and then attempt to convert it into decimal
</text><br>

</details>
<hr>

<!-- FLOWCHART -->

<details>
  
<summary>Flowchart</summary><br>
<img alt="App Flowchart" src =./Images/Base_Conversion_Flowchart.png >
  </details>
<hr>

<!-- PROGRAM FLOW -->

<details>
<summary>Program Flow</summary><br>
After running main.py, a user enters into the main program loop. The beginning of the loop will present them with four options:

<!-- PROGRAM FLOW OPTION 1 -->
<details style="padding-left: 20px">
<summary>1. View number base system text tutorials</summary>
User enters a loop with the option to select from a list of tutorials or return to the main menu. If a user selects one of the tutorials, that tutorial will be printed to the screen. The user is prompted to press 'enter' to return to the tutorial option menu. A user may continue to select and view from the list of tutorials until they choose the last option to return to the main menu.
<hr>
</details>

<!-- PROGRAM FLOW OPTION 2 -->
<details style="padding-left: 20px">
<summary>2. Program converts a chosen number from decimal to another system</summary>
User is given 2 options at the conversion menu:
<ul>
  <li>Select a number base in which to convert a number</li>
  <li>Return to main menu</li>
</ul>
If the user selects the first option, they are prompted to enter a number from 2 - 16 which will be the base to convert to. Users are then prompted to enter a number they wish to convert. The program will print incrementing numbers with equal value in both decimal and the chosen base number systems. Depending on the value of the number, these printed numbers will increment in greater intervals, so the program does not take more than five seconds to print the ascending values. The program will pause once the selected number is reached.

Here users have three options:
<ul>
  <li>Return to the main menu</li>
  <li>Return to the conversion menu and select another base and number</li>
  <li>Print a detailed breakdown of the digits and place values in the converted number. At this point, users can choose to return to either the conversion menu or the main menu
</ul>
<hr>
</details>

<!-- PROGRAM FLOW OPTION 3 -->
<details style="padding-left: 20px">
  <summary>3.User attempt to convert a random number from one base to decimal</summary>
  User enters the challenge loop. Here they have three options:
  <ul>
    <li>Return to main menu</li>
    <li>
      View their scores. This will print the number of correct responses, total responses, and percentage correct for each of the bases from 2 through 16, along with the number of total responses.
    </li>
    <li>
      Select a base to convert from. A random number is then printed and the program awaits the users response to convert that number from the selected base to decimal. The random number is selected from a higher range of numbers if the user has taken many challenges and responded correctly. After the user enter the response, they will be informed whether or not the answered correctly and receive a detailed breakdown of the number in the base that was selected. User scores are then updated and the user has the option to reenter the challenge loop or return to the main screen. 
    </li>
  </ul>
	<hr>
</details>

<!-- PROGRAM FLOW OPTION 4 -->
<details style="padding-left: 20px">
  <summary>4.Exit the loop and close the program</summary>
  Exit the program
</details>
</details>
<hr>

<!-- HOW TO RUN THE PROGRAM -->

<details>
<summary>How to Run the Program</summary><br>
In order to use Python CLI Number Base Converter, you will need to fork and clone this repository. Once you have done so, navigate to the root folder of the cloned directory and run the command 'python main.py'. This will start the program and enter the user into the main program loop.

As an alternative, you may also open the following Python Sandbox to run and edit the code.

<a href='https://pythonsandbox.dev/mbfgxoewl0ez'>Python CLI Number Base Converter sandbox</a>
</details>
<hr>

<!-- FILE SETUP -->
<details>
<summary>File Setup</summary>
<br>

<text>[1] main.py</text><br>
<em>-contains the main program loop</em><br>

<text>[2] calculation_functions.py</text><br>
<em>-contains functions that calculate number conversions and place values in number systems contains functions that calculate user scores and difficulty levels</em><br>

<text>[3] display_info_functions.py</text><br>
<em>-contains functions that interpolate values and files to be printed</em><br>

<text>[4] user_input_functions.py</text><br>
<em>-contains functions that handle user inputs and verify that they are valid</em><br>

<text>[5] prompts.py</text><br>
<em>-contains strings, often multiline, that will printed during the program, such as a list of menu options</em><br>

<text>[6] user_scores.json</text><br>
<em>-JSON file that contains all of the user's scores on the challenge section
potential for reconfiguration to store multiple users in the future</em><br>

<text>[7] Text_Files</text><br>
<em>-contains .txt files that are tutorials explaining number systems</em><br>

</details>
<hr>

<!-- CALCULATION FUNCTIONS -->

<details>
<summary>calculation_functions.py</summary><br>
<b>determine_place_values(num, num_system)</b><br>
<em>num = </em><text>Integer : number to convert</text><br>
<em>num_system = </em><text>Integer : number system base selected</text><br>
<em>returns - </em><text>Array of Integers : List of place values not greater than the number to convert, sorted from greatest to least</text><br>

<br>

<b>num_to_new_base(num, list_place_val)</b><br>
<em>num = </em><text>Integer : number to convert</text><br>
<em>list_place_val = </em><text>Array of Integers : number system base selected</text><br>
<em>returns - </em><text>String : Representation of number converted to new base less than ten</text><br>
<br>
<b>digit_greater_than_nine(num)</b><br>
<em>num = </em><text>Integer : number in range of 10 and 15</text><br>
<em>returns - </em><text>String : letter in range of 'A' and 'F'</text><br>

<br>

<b>num_to_new_base_greater_than_ten(num, list_place_val)</b><br>
<em>num = </em><text>Integer : number to convert</text><br>
<em>list_place_val = </em><text>Array of Integers : number system base selected</text><br>
<em>returns - </em><text>String : Representation of number converted to new base less than is greater than ten serves same purpose as num_to_new_base, but using number bases that including alpha characters</text><br>

<br>

<b>update_scores(scores, num_of_base, correct_bool)</b><br>
<em>scores = </em><text>Dictionary : user's scores for each base</text><br>
<em>num_of_base = </em><text>Integer : number of base being converted</text><br>
<em>correct_bool = </em><text>Boolean : True if challenge answered correctly, otherwise False</text><br>
<em>returns - </em><text>Dictionary: updated user score dictionary</text><br>

<br>

<b>difficulty_level(num_correct, num_answered)</b><br>
<em>num_correct = </em><text>Integer : number of correct scores in total</text><br>
<em>num_answered = </em><text>Integer : number of responses in total</text><br>
<em>returns - </em><text>2 Integers : Low and high limits of challenge random numbers</text><br>
</details>

<hr>

<!-- DISPLAY INFO FUNCTIONS -->

<details>
<summary>display_info_functions.py</summary><br>
<b>print_txt_file(a_file)</b><br>
<em>a_file = </em><text>String : txt file open and read</text><br>
<em>returns - </em><text> 0 (not used) : prints txt file</text><br>

<br>

<b>detailed_breakdown(arr_place_val, num_as_string, base, num)</b><br>
<em>arr_place_val = </em><text>Array of  Strings: descending array of place values in given base, with each element as a string</text><br>
<em>num_as_string = </em><text>String : Representation of number in a base other than Base10</text><br>
<em>base = </em><text>Integer : selected base other than 10</text><br>
<em>num = </em><text>Integer : number in base 10</text><br>
<em>returns - </em><text>0 (not used) : prints count of digits by place count and breakdown of conversion</text><br>

<br>

<b>display_user_stats(scores_dict)</b><br>
<em>scores_dict = </em><text>Dictionary : user scores</text><br>
<em>returns - </em><text>Nothing : prints all user scores by base</text><br>
</details>

<hr>

<!-- USER INPUT FUNCTIONS -->

<details>
<summary>user_input_functions.py</summary><br>
<b>menu_selection(prompt, arr_of_nums_as_strings)</b><br>
<em>prompt = </em><text>String : txt file open and read</text><br>
<em>arr_of_nums_as_strings = </em><text>Array of Strings : list of acceptable menu option</text><br>
<em>returns - </em><text> Integer : runs user through loop until a valid number is input, then returns that number as integer</text><br>

<br>
<b>accept_number(prompt)</b><br>
<em>prompt = </em><text>String : txt file open and read</text><br>
<em>arr_of_nums_as_strings = </em><text>Array of Strings : list of acceptable menu choice numbers</text><br>
<em>returns - </em><text> Integer : runs user through loop until valid menu option is selected, then returns choice as integer</text><br>

<br>

<b>accept_base(prompt)</b><br>
<em>prompt = </em><text>String : txt file open and read</text><br>
<em>returns - </em><text> Integer : runs user through loop until a number between 2 and 16 (base) is input, then returns that number as integer</text><br>
</details>

<hr>

<!-- TESTING SETUP -->

<details>
<summary>Testing Setup</summary>
Unit tests are run in the 'test_calculations.py' file through unittest.
</details>
