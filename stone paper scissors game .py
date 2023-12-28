#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

 

options = ["Rock", "Paper", "Scissors"]

 

user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)

 

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)

 

if user_choice == computer_choice:

    print("Tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("user wins !!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("user wins !!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("user wins!!")

else:

    print("Computer wins!!")


# In[ ]:




