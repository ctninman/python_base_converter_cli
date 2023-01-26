import json
 
 
# the file to be converted to
# json format
filename = 'Text_Files/user_data.txt'
 
# dictionary where the lines from
# text will be stored
user_dict = {}
 
# creating dictionary
with open(filename) as fh:
 
	for line in fh:

			# reads each line and trims of extra the spaces
			# and gives only the valid words
		command, description = line.strip().split(None, 1)

		user_dict[command] = description.strip()

		print(user_dict)
 
# creating json file
# the JSON file is named as test1
out_file = open("user_scores.json", "w")
json.dump(user_dict, out_file, indent = 4, sort_keys = False)

print(out_file)
out_file.close()