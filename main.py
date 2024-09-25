# def word_frequency():
#     # Read input from the user
#     input_text = input("Enter text: ")

#     # Split the input into words
#     words = input_text.split()

#     # Create a dictionary to count the frequency of each word
#     word_count = {}
#     for word in words:
#         # Use the word as a key and increment its count
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     # Sort the dictionary keys alphanumerically
#     sorted_words = sorted(word_count.keys())

#     # Print the results
#     for word in sorted_words:
#         print(f"{word}:{word_count[word]}")

# # Call the function
# word_frequency()



dict = {
    "Deep":23,
    "Het": 123

}

if 'Deep' in dict:
    print("Yesh")