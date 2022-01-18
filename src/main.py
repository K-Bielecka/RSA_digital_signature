

from rsa_signature import generate_keys


option1 = "generate keys"
option2 = "generate signature for input message"
option3 = "generate signature for message from given file"
option4 = "verify signature from given file"
welcome_text = "Welcome to our simple RSA signature app. You can choose one of the below options: \n"
option_list = str("1.", option1, "\n", "2.", option2, "\n","3.", option3, "\n","4.", option4, "\n")

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
            #generate keys option
            print("You chose option: " + option1)  
            public_key_path = input("Please provide path for public key file \n")
            private_key_path = input("Please provide path for private key file \n")

            ((n,e),d) = generate_keys()

            print("generated public key: \n", n, ",", e)
            with open(str(public_key_path),'w') as writer:
                writer.write(str(n) + ',' + str(e))

            print("generated private key: \n", d)
            with open(str(private_key_path),'w') as writer:
                writer.write(str(d))    
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


print(welcome_text, option_list)
user_option_input = int(input("Type 1, 2, 3 or 4 to choose the option and press 'Enter'. \n"))

user_input_switch(user_option_input)


#Think about implementing the option to "escape" the certain option if for example somoene made a mistake. Should be done possibly with event listener, catch the 
#  key press event and exit if it is the 'Escape' key

#Below is code that might help with this

# from pynput import keyboard

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()