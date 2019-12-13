#Problem 4
#Credit to Udacity for base Group and User object
#Checks if user is in group or any subgroups by looping through subgroups and recursively calling function so every subgroup is searched
#Time Complexity is O(n * m):
#Begins with searching list of users in provided group - number of users is n
#Searches all potential subgroups recursively - number of levels is m
#returns True if user is found at any point
#Space complexity is O(n * m)
#Top level group is added to memory stack - n
#Number of subsequent groups are added to memory stack as needed - m
#exits when user is found in any of these groups
