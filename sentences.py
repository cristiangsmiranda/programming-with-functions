# as a point of creativity I chose to create a list of adjectives to add to the phrase

import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word.capitalize()

def get_adjective():
    adjectives = ["adorable", "bad", "bored", "calm", "careful", "creepy", "crazy", "dizzy", "faithful", "innocent", "lazy"]
    adjective = random.choice(adjectives)
    return adjective

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    verb = random.choice(verbs)
    return verb       

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
"beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out",
"over", "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    word = get_determiner (quantity)
    noun = get_noun (quantity)

    prepositional_phrase = f"{preposition} {word} {noun}"
    return prepositional_phrase

def make_sentence (quantity, tense):
    word = get_determiner (quantity)
    adjective = get_adjective()
    noun = get_noun (quantity)
    verb = get_verb (quantity, tense)
    preposition = get_preposition()

    sentence = f"{word} {adjective} {noun} {verb} {preposition} {word.lower()} {noun}."
    return sentence

def main():
    sentence1 = make_sentence (1, "past")
    print(sentence1)
    sentence2 = make_sentence (1, "present")
    print(sentence2)
    sentence3 = make_sentence (1, "future")
    print(sentence3)
    sentence4 = make_sentence (2, "past")
    print(sentence4)
    sentence5 = make_sentence (2, "present")
    print(sentence5)
    sentence6 = make_sentence (2, "future")
    print(sentence6)

main()



#words = ["boy", "girl", "cat", "dog", "bird", "house"]
#word = random.choice(words)
#print (word)

#word = "horse"
#cap_word = word.capitalize()
#print(cap_word)

#given = "Michelle"
#middle = "Aya"
#surname = "Takechi"
#full_name = f"{given} {middle} {surname}"
#print(full_name)