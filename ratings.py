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

user_restaurant = input("Enter restaurant name: ")
user_rating = input("Enter restaurant score: ")
ratings_dicts[user_restaurant] = user_rating

sorting_rating_dict(ratings_dicts)