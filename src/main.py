

option1 = "generate keys"
option2 = "generate signature for input message"
option3 = "generate signature for message from given file"
option4 = "verify signature from given file"

def user_generate_keys():
    pass

def user_generate_signature_for_input_message():
    pass

def user_generate_signature_for_file_message():
    pass

def user_verify_signature_from_file():
    pass

def user_input_switch(key: int):
    match key:
        case 1:
            # #generate keys option
            print("You chose option: " + option1)  
        case 2:
            #generate signature for input message
            print("You chose option: " + option2)
        case 3:
            #generate signature for message from given file
            print("You chose option: " + option3)    
        case 4:
            #verify signature from given file
            print("You chose option: " + option4)       
        case _:
            print("Please choose a valid option 1-4")

user_option_input = int(input("Please choose one of the below options. Type 1-4 to choose an option."))
print("the user input is:" + str(user_option_input))

user_input_switch(user_option_input)