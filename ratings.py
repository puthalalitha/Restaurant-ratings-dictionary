"""Restaurant rating lister."""

def sorting_rating_dict(dictionary):
    for key in sorted(dictionary):
        print(f'{key} is rated at {dictionary[key]}.')   

# put your code here
ratings_dicts = {}
file = open("scores.txt")
for line in file:
    name, rating = line.rstrip().split(":")
    ratings_dicts[name] = rating

sorting_rating_dict(ratings_dicts)

user_restaurant = input("Enter restaurant name: ").title()

while True:
    
    user_rating = int(input("Enter restaurant score: "))
    if user_rating >= 1 and user_rating <= 5:
        ratings_dicts[user_restaurant] = user_rating
        break
    print("Invalid score. Score should be between 1 and 5.")

sorting_rating_dict(ratings_dicts)