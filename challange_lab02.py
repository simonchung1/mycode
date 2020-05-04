#!/usr/bin/env python3
col_list= ["blue", "Columbus"]

col_list.append(1492)

#print(col_list)

user_input= input("What is your name?: ")

#print (user_input)

print("In ", col_list[2], ", Columbus sailed the ocean ", col_list[0], ". ", user_input, " fell off the boat.", sep="")
print(f"In {col_list[2]}, {col_list[1]} sailed the ocean {col_list[0]}. {user_input} fell off the boat.")
#print(col_list[0])
