################################
# Tenzin Wangchuk
#BE ELECTRICAL ENGG. 1YEAR
# 02230086
################################
# REFERENCES
# @CHAT_GPT
################################
# SOLUTION
# Your Solution Score:50223
# Put your number here
# CSF-101-CAP/input_6_cap1.txt
################################

# Read the input.txt file
def read_input(Input_your_file_name): #Defining read_input function
    messi = [] #Creating an empty list
    with open(Input_your_file_name, 'r') as files:#
        for neymer in files:
            opponent_choice, outcome = neymer.split()
            messi.append((opponent_choice, outcome))
    return messi #Returning list messi

# To Calculate the score for each round
def calculate_score(Total_Number_of_rounds):
    Goal = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # It is Defeat
            if opponent_choice == 'A':
                Goal += 3  #  if Paper blocks Rock
            elif opponent_choice == 'B':
                Goal += 1  # if Scissors cuts Paper
            elif opponent_choice == 'C':
                Goal += 2  # Rock crushes sicssor
        elif outcome == 'Y':  # Draw
            if opponent_choice == 'A':
                Goal += 4  # Both showed rock so it's a draw
            elif opponent_choice == 'B':
                Goal += 5  # Both showed paper so it's a draw
            elif opponent_choice == 'C':
                Goal += 6  # Both showed scissor so it's a draw
        elif outcome == 'Z':  # Victory
            if opponent_choice == 'A':
                Goal += 8  # Paper beats rock
            elif opponent_choice == 'B':
                Goal += 9  # Scissor cuts paper
            elif opponent_choice == 'C':
                Goal += 7  # Rock crushes scissor
    print(f"The total score is:{Goal}") #outcome : your total score is score

# To run a program
Input_your_file_name = "CSF-101-CAP/input_6_cap1.txt" #Specifying  file
calculate_score(read_input(Input_your_file_name))