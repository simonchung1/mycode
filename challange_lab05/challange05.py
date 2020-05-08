#!/usr/bin/env python3

char_name = ""
char_stat = ""
char_dict = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

# char_name = input("Which character do you want to know about (Flash, Batman, Superman)")
#    if char_name.lower() == "
# 
# char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)")
#  print(char_name + "'s " + char_stat + " is: " + char_dict[char_name.lower()][char_stat.lower()])

while True:
    char_name = input("Which character do you want to know about (Flash, Batman, Superman): ")
    if char_name.lower() == "batman" or char_name.lower() == "flash" or char_name.lower() == "superman":
        break
    else:
        print("Invalid character")
while True:
    char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence): ")
    if char_stat.lower() == "strength" or char_stat.lower() == "speed" or char_stat.lower() == "intelligence":
        break
    else:
        print("Invalid statistic")

print(char_name + "'s " + char_stat + " is: " + char_dict[char_name.lower()][char_stat.lower()])


