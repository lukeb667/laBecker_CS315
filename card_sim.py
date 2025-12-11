# Luke Becker. Collaboarted with Spriha on the ideas!
# Code for comparing Huffman's/iteratively selecting to a Binary Search algorithm.
# The results: binary search performs better overall than eliminating the most probable answer with each guess. 
#  However, offsetting the starting guess of the binary search algorithm improves the answer, because we eliminate more of the improbable answers that way. 
#  Six 

import math
import random

def binary_search(selected_card, lower, upper, count=0, start=None):
    count += 1 # Keep track of how many recursive calls we've had
    
    # If we passed a start index, look at that first. Otherwise, go for the midpoint. 
    if start == None: 
        index = lower + (upper - lower) // 2
    else: index = start 

    # If we found the card, return how long it took
    if index == selected_card:
        return count

    # If the card was greater than the one we guessed
    elif index < selected_card:
        return binary_search(selected_card, index, upper, count)

    # If the card was less than the one we guessed
    elif index > selected_card:
        return binary_search(selected_card, lower, index, count)



def huffman(selected_card):
    # Count down from 9 to 1 for guesses. Return how many guesses it took to be correct
    for i in range(9, 0, -1):
        if i == selected_card: 
            return (9-i)+1

if __name__ == "__main__":
    # Create our deck. Based on the problem in class
    cards = []
    for i in range(1,10):
        [cards.append(i) for j in range(i)]

    h = [] # List of huffman times
    b = [] # List of binary search times

    # Calculate the average via repeated sampling. 
    for i in range(100000):
        # Get a random card based on the ones in the deck
        selection_index = random.randint(0, len(cards)-1)
        selected_card   = cards[selection_index]

        # Add the number of iterations each algorithm took to the lists
        h.append( huffman(selected_card) )
        b.append( binary_search(selected_card, 1, 10, start=6) )

    # Print the results 
    print("Average Guess Count (H):", sum(h)/len(h) )
    print("Average Guess Count (B):", sum(b)/len(b) )

