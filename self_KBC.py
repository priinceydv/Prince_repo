print("Welcome to the KBC game!")
print("You have 5 questions to answer.")
print("You can quit the game at any time by typing 'quit'.")
print("Let's start!\n") 

# using list and dictionary to store questiins.
question = [
    {"question" : "what is the capital of india?",
     "options" : ["a) indore", "b) bhopal", "c) delhi", "d) banglore"],
     "answer" : "c"},
     {"question" : "what is the capital of mp?",
      "options" : ["a) indore", "b) bhopal", "c) delhi", "d) banglore"],
      "answer" : "b"},
     {"question" : "what is the capital of maharashtra?",
      "options" : ["a) indore", "b) bhopal", "c) delhi", "d) mumbai"],
      "answer" : "d"},
     {"question" : "what is the capital of up?",
      "options" : ["a) indore", "b) bhopal", "c) delhi", "d) lucknow"],
      "answer" : "d"},
     {"question" : "what is the capital of rajasthan?",
      "options" : ["a) indore", "b) bhopal", "c) delhi", "d) jaipur"],
      "answer" : "d"}
]

count = 0 #total number of correct questions
Total_prize= 0 #total prize money
prize = [1000, 10000, 100000, 1000000, 10000000] #prize money for each question
# using for loop to iterate through the questions
for i in range(len(question)):

    print(f"Prize money of this question {i+1} is : ", prize[i],"\n")
    
    print("Question ", i+1, ":\n")
    print(question[i]["question"], "\n")

# using for loop to iterate through the options
    for j in range(len(question[i]["options"])):
        print(question[i]["options"][j])
    answer = input("Enter your answer: ")
    while answer not in ["a", "b", "c", "d", "quit",]:
        print("Invalid option! Please enter a, b, c, or d.")
        answer = input("Enter your answer: ")

    # using if else statement to check the answer
    if answer == question[i]["answer"]:
        print("\nYour answer is correct!\n")
        print("You have won Rs ", prize[i], "\n")
        Total_prize = prize[i]
        count += 1
        
            
        
    elif answer == "quit":
        print("\nYou have quit the game.")
        break
    else:
        print("Wrong answer!")
        break
    
print("Game Over!")
print("Your correct answer is: ", count, " out of 5")
print("You won: Rs ", Total_prize) 
print("Thank you for playing!")

