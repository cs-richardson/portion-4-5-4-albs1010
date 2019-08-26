# Amount of food and number of people
tons_of_food = 0.07
num_people = 25

# Determine how much food each person gets
tons_of_food_per_person = rtons_of_food / num_people
#rounds to 5 decmial places
tons_of_food_per_person = round(tons_of_food_per_person, 5)
print tons_of_food_per_person

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))
#rounds to 5 decmial places
tons_taken = round(tons_taken, 5)
if tons_taken == tons_of_food_per_person:
    print "Good job, you took the right amount of food!"
else:
    print "You took the wrong amount of food!"
