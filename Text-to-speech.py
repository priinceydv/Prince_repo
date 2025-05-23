# You can use the os module to run system commands in Python.
# This example uses the 'say' command on macOS to convert text to speech.
# This code will take user input and use the 'say' command to speak it out loud.
# Note: The 'say' command is specific to macOS. For other operating systems, you may need to use a different text-to-speech library or command.

import os # Importing the os module to use system commands
if __name__ == "__main__":
    
        print("Welcome to my first python project, Myself Prince yadav")
        print("Thank you for using my project")

        while True: # using while loop to continuously ask for input
            x = input("Enter a number (or 'exit' to quit): ")
            
            if x== 'exit':
                os.system("say 'Goodbye'")
                break #using the break statement to exit the loop
            
            command = f"say {x}"
            os.system(command) # This will run the command in the terminal