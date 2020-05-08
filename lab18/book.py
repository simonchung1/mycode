#!/usr/bin/env python3
#A program that prompts the user for a value (1 through n), then returns a quick synopsis of a book or movie in that series.
#1 - Harry Potter
#2 - Hobbit & Lord of the Rings
#3 - Chronicles of Narnia
#4 - Indiana Jones

name = " " #define name variable

while name != "1" and name != "2" and name != "3" and name != "4": #setup infinite loop with conditions
    name = input("Please enter a number between 1 and 4: ") #Prompts user for a number and stores into name
    if name == "1": #Checks if user inputted 1. If they did, outputs synposis of Harry potter
        print("You've selected Harry Potter. Here is a brief synposis:"+"\n")
        print("Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.")
    elif name == "2": #Checks if user inputted 2. If they did, outputs synposis of Lord of the rings
        print("You've selected Hobbit & Lord of the Rings. Here is a brief synposis:" + "\n")
        print("The Lord of the Rings: The Fellowship of the Ring is a 2001 fantasy adventure film, directed by Peter Jackson. It is the first part of the Lord of the Rings trilogy of films, based on the best-selling novel by J.R.R. Tolkien. The film tells the story of young hobbit Frodo Baggins who, accompanied by eight companions, embarks on a journey to destroy the One Ring in the fires of Mount Doom.")
    elif name == "3": #Checks if user inputted 3. If they did, outputs synposis of Chronicles of Narnia
        print("You've selected Chronicles of Narnia. Here is a brief synposis:" + "\n")
        print("During the World War II bombings of London, four English siblings are sent to a country house where they will be safe. One day Lucy (Georgie Henley) finds a wardrobe that transports her to a magical world called Narnia. After coming back, she soon returns to Narnia with her brothers, Peter (William Moseley) and Edmund (Skandar Keynes), and her sister, Susan (Anna Popplewell). There they join the magical lion, Aslan (Liam Neeson), in the fight against the evil White Witch, Jadis (Tilda Swinton).")
    elif name == "4": #Checks if user inputted 4. If they did, outputs synposis of Indian jones
        print("You've selected India Jones. Here is a breif synposis:" + "\n")
        print("The first film is set in 1936. Indiana Jones (Harrison Ford) is hired by government agents to locate the Ark of the Covenant before the Nazis. The Nazis have teams searching for religious artefacts, including the Ark, which is rumored to make an army that carries the Ark before it invincible.[24] The Nazis are being helped by Indiana's nemesis René Belloq (Paul Freeman). With the help of his old flame Marion Ravenwood (Karen Allen) and Sallah (John Rhys-Davies), Indiana manages to recover the Ark in Egypt. The Nazis steal the Ark and capture Indiana and Marion. Belloq and the Nazis perform a ceremony to open the Ark, but when they do so, they are all killed gruesomely by the Ark's wrath. Indiana and Marion, who survived by closing their eyes, manage to get the Ark to the United States, where it is stored in a secret government warehouse.")
    else: #if user did not input 1,2,3 or 4, will output it's invalid and prompt user to enter a number until valid number is entered
        print("Invalid input")

