#Problem 3
#Credit to Udacity for base Node, Tree, Stack, and State Structures
#Time Complexity - create_tree loops through input in O(n^2) time - min function adds additional O(n)
#Time Complexity - huffman_encoding loops through tree in O(n) time
#pre_order/traverse appends value to list in o(1) time
#encode_string loops through string characters in 0(n) time
#Time Complexity - huffman_decoding loops O(n^2)
#Creates dictionary with huffman encoded values, deletes numbers
#Decodes array of provided binary values and decodes them with provided dictionary
#Space Complexity of huffman_encoding is O(n) - visit_order, keys_to_delete grows based on size of linked list
#Space Complexity of huffman_decoding/encode_string - O(n) - string grows based on size of input
#Space Complexity of create_tree is O(n) - nodes_to_add grows with input
