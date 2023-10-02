import spacy
nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))  # Similarity between "cat" and "monkey"
print(word3.similarity(word2))  # Similarity between "banana" and "monkey"
print(word3.similarity(word1))  # Similarity between "banana" and "cat"

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define three words as tokens
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Calculate and print similarity scores
print(word1.similarity(word2))  # Similarity between "cat" and "monkey"
print(word3.similarity(word2))  # Similarity between "banana" and "monkey"
print(word3.similarity(word1))  # Similarity between "banana" and "cat"

# Regarding the similarities between cat, monkey, and banana, what I find interesting is how they can be related through their properties and attributes. 
# For instance, all three are living organisms, they have specific physical features such as fur, and they can be categorized as mammals.
# On the other hand, they also differ in various ways such as the type of food they consume, their behavior, and their natural habitats.

#an example of my own

nlp = spacy.load("en_core_web_md")

word1 = nlp("car")
word2 = nlp("bicycle")
word3 = nlp("skateboard")

print(word1.similarity(word2))  # Similarity between "car" and "bicycle"
print(word3.similarity(word2))  # Similarity between "skateboard" and "bicycle"
print(word3.similarity(word1))  # Similarity between "skateboard" and "car"

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define three words as tokens
word1 = nlp("car")
word2 = nlp("bicycle")
word3 = nlp("skateboard")

# Calculate and print similarity scores
print(word1.similarity(word2))  # Similarity between "car" and "bicycle"
print(word3.similarity(word2))  # Similarity between "skateboard" and "bicycle"
print(word3.similarity(word1))  # Similarity between "skateboard" and "car"

# As for an example of my own, let's consider the similarities between a car, a bicycle, and a skateboard. 
# While all three are modes of transportation, they differ in their size, speed, and the way they are operated. 
# A car is typically large, fast, and requires fuel, while a bicycle is smaller, slower, and can be powered by human effort. 
# A skateboard is even smaller and slower than a bicycle and is typically used for recreational purposes.


# Regarding the differences between the 'en_core_web_sm' and 'en_core_web_md' language models, 
# the main distinction is the size of their vocabulary and the number of training examples. 
# 'en_core_web_md' is a larger model that includes more features and is trained on a larger dataset.
# It makes it more accurate and robust in understanding complex sentences and nuanced language.
