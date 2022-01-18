from rsa_signature import generate_keys, generate_signature, verify

option1 = "generate keys"
option2 = "generate signature for input message"
option3 = "generate signature for message from given file"
option4 = "verify signature from given file"
welcome_text = "Welcome to our simple RSA signature app. You can choose one of the below options: \n"
option_list = "1." + option1 + "\n" + "2." + option2 + "\n" + "3." + option3 + "\n" + "4." + option4 + "\n"

def user_generate_keys_to_file():
    public_key_path = input("Please provide path for public key file \n")
    private_key_path = input("Please provide path for private key file \n")

    ((n,e),d) = generate_keys()

    print("generated public key: \n", n, ",", e)
    with open(str(public_key_path),'w') as writer:
        writer.write(str(n) + ',' + str(e))

    print("generated private key: \n", d)
    with open(str(private_key_path),'w') as writer:
        writer.write(str(d)) 

    return ((n,e),d)

def user_generate_signature_to_file(m, n, e, d):
    signature_path = input("Please provide path for signature file \n")
    s = generate_signature(m,n,e,d)
    is_valid = verify(m,n,e,s)
    if(is_valid):
        #save signature to file
        print("generated signature: \n", s)
        with open(str(signature_path),'w') as writer:
            writer.write(str(s))
    else:
        #print not_valid message
        print("Failed to generate a valid signature. \n")
   
def user_input_switch(key: int):
    match key:
        case 1:
            #generate keys option
            print("You chose option: " + option1)  
            user_generate_keys_to_file() 
        case 2:
            #generate signature for input message
            print("You chose option: " + option2)
            #get message
            message = input("Please type the message to be signed \n")
            # generate keys
            ((n,e),d) = user_generate_keys_to_file()
            #generate signature and save to file
            user_generate_signature_to_file(message,n,e,d)
        case 3:
            #generate signature for message from given file
            print("You chose option: " + option3)  
            #get file with message path
            message_path = input("Please provide path to the file with the message, that you want to sign \n")
            #read message  
            with open(str(message_path),'r') as reader:
               message = reader.read()
            #generate keys and signature to files
            ((n,e),d) = user_generate_keys_to_file()
            user_generate_signature_to_file(message,n,e,d)
        case 4:
            #verify signature from given file
            print("You chose option: " + option4)
             #get file with message path
            signature_path = input("Please provide path to the file with the signature, that you want to verify \n")
            message_path = input("Please provide path to the file with message signed with your signature \n")
            public_key_path = input("Please provide path to your public key\n")
            #read message  
            with open(str(signature_path),'r') as reader:
               signature = reader.read()
            with open(str(message_path),'r') as reader:
               message = reader.read()
            with open(str(public_key_path),'r') as reader:
               file_contents = reader.read()
            (n,e) = file_contents.split(',')
            #verify signature and return result info
            is_valid = verify(message,int(n),int(e),int(signature))
            if(is_valid):
                print("Provided signature is valid. \n")
            else:
                print("Provided signature is invalid.\n")
                
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