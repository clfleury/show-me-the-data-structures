#Problem 2
#Recursively finds filenames in each subfolder to ensure all folders are checked
#n input refers to how many files are in the provided directory path
#recursion terminates when the last file in the last searched subfolder has been added to the array
#Time Complexity is O(n * m)):
#searchs through list in provided directory; for each directory, adds n files to list
#For each subdirectory - runs m times for each level
#list array grows in for loop depending on size of input and depth of directories
#Space Complexity is O(n * m):
#Starts with base provided directory; for each directory, adds n files to list
#For each subdirectory, stores m levels in memory
#list array grows in for loop depending on size of input and depth of directories
#n is the number of root directories
#m is the depth level of the directories
