# Ask the user for a list of three friends
#for each friend tell the user whether they are nearby
# for each friend, we save their name to nearby friends
people_file = open('people.txt', 'r')
nearby_people = people_file.read().splitlines()
people_file.close()
nearby_set = set(nearby_people)
user_friends = []
print(nearby_set)
for x in range(0,3):
    friend = input("Who's your friend?")
    if friend in nearby_set:
        print(f"{friend} is nearby!")
        user_friends.append(friend)
    else:
        print(f"{friend} is not nearby!")
nearby_friends = open('nearby_friends.txt', 'w')
for friend in user_friends:
    nearby_friends.write(f"{friend}\n")
nearby_friends.close()

