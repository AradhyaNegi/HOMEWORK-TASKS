# -*- coding: utf-8 -*-
"""
CLASS HOEWORK - 2
"""
#TASK 1
a = float(input(" Enter the weight in Pounds : "))
d = a /2.205
print("The weight in kg of" + str(a) + "pounds is" + str(d) + "kg")

#TASK 2
b = input(" Please Enter your NAME : ")
print("HALO !! " + b + "WELCOME TO THE WORLD OF GOD!!!!!!!")
c = input(" Which school do u go to ? : ")
print("WOW " + c + "is a renowned school in your city Dude!!")
g = input(" Whats your age ? :")
print(" You seem preety smart at your age dude..")
w = input(" What are your hobbies : ")
print(" You are just to good at your age dude..")

#TASK 3
a = float(input(" Enter the First number : "))
b = float(input(" Enter the Second number : "))
if a<b:
    print(str(b)+" is smaller than " + str(a))
else: print(str(a) + " is smaller than " + str(b))

#TASK 4
a = float(input(" Enter the height of the First triangle : "))
b = float(input(" Enter the base of the First triangle : "  ))
q = 1/2 * a * b
print(" This triangle is triangle ABC and has a area of : " + str(q) + "unit sq.")
c = float(input(" Enter the height Second triangle : "))
d = float(input(" Enter the base Second triangle : "))
f = 1/2 * c * d
print(" This triangle is triangle XYZ and has a area of : " + str(f) + "unit sq.")
if q < f:
    print("Triangle XYZ has GREATER area than triangle ABC")
else :
    print("Triangle ABC has GREATER area than triangle XYZ")
 
#TASK 5
a = input("Please Enter a name of Grain from the following - dal|wheat|rice|moong| : " ).lower()
if a == "dal":
    print("DAL")
    print("It is loaded with protein, fibre, magnesium, calcium, B vitamins and folate that boost overall health. Rich in essential nutrients masoor dal promotes skin health and prevents acne.")
elif a == "wheat" :
    print("WHEAT")
    print("Wheat is a member of the grass family that produces a dry, one-seeded fruit commonly called a kernel. More than 17,000 years ago, humans gathered the seeds of plants and ate them. ... Wheat is the primary grain used in U.S. grain products — approximately three-quarters of all U.S. grain products are made from wheat flour.")
elif a == ("rice") :
    print("RICE")
    print("As a cereal grain, domesticated rice is the most widely consumed staple food for over half of the world's human population, especially in Asia and Africa.")
elif a == ("moong"):
    print("Moong")
    print("Packed with protein and low on carbs, moong dal (also known as green gram) is one of the most recommended vegetarian superfoods.")
    print("One of the best weight loss friendly snacks is moong dal ")
else : 
    print("This grain is not in the LIST   :|")

#TASK 6
print("Here is an EQUATION : 2x + 3y = 18 ")
print("Enter the value suitable to satisfy the condition:")
a = int(input("Enter the Value of 'x' "))
b = int(input("Enter the Value of 'y' "))
d = 2*a + 3*b
if d == 18:
    print("WOW!!! correct answer ")
else : 
    print("Nope! try again..")

#TASK 7
a = input("Enter the symbol of an chemical element").lower()
if a == "h" :
    print("Hydrogen")
elif a == "he":
    print("Helium")
elif a == "o":
    print("Oxygen")
else :
    print("I am still learning them!!")
    
#TASK 8
alpha = input("Enter a alphabet").lower()
if alpha == "a":
    print("Apple,Adam,Always,Ask,Aman")
elif alpha == "b":
    print("Ball,Bat,Battle,BOOM,Bad")
elif alpha == "c":
    print("Call,Catch,Cluster,Clue,Call")
elif alpha == "d":
    print("Delta,Demon,Distilled,Demolisher,Delay")
elif alpha == "e":
    print("English,Emily,Ender,Emash,Email")
elif alpha == "f":
    print("Fish,Full,Flash,fed,Fast")
else :
    print("DUDE!! This is a long work wait for the rest to come \nEven u do some work bro..!!")

#TASK 10
print("WELCOME to the GOD quiz")
print("Enter the correct answer to win!")
print("Q1.What is the capital of Russia :")
a = input(("Enter the answer:")).lower()
if a == "moscow":
    print("Wow ! is the right Answer " )
else :
    print("Wrong answer!try again once u give the answer for the rest 2 questions>>")

d = input("Q2.Which is the most trending video game of all times ?").lower()
if a == "minecraft" : 
    print("Correct answer!!")
else : 
    print("Wrong answer..but that is also a trending game !!")
e = input("What is the highest peak in the world..come on thats a piece of cake..").lower()
if e == "mount everest":
    print("Thats the Right ANSWER ..")
else : 
    print("Thats wrong..")




