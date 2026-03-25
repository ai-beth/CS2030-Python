#Description: Appending/ updating data to a Json file

#Import JSON and OS
import json, os

#Function to append data to a JSON file without overwriting the
#existing data
def append_to_json(filename,new_data):
    #Check if the file exist
    if os.path.exists(filename):
        #Open the JSON file for reading
        with open(filename,'r') as f:
            try:
                #Load existing data from the file
                data = json.load(f)

            except json.JSONDecodeError:
                #Handle empty or invalid JSON Data
                data = {}

    else:
        #If the file doesn't exist, start with an empty dictionary
        data = {}

    #Append or Update new data to the existing data structure
    if isinstance(data,list): #If the existing data is a list
        data.append(new_data)
    elif isinstance(data,dict): #If the existing data is a dictionary
        data.update(new_data)

    #Write the updated data back to the file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=3)

#Example of appending data
#new_entry = {"user1":{"name":"Timmy","age":23}}
new_entry = {"user2":{"name":"Rocky","age":43}}
append_to_json('Student.json',new_entry)












    








        



