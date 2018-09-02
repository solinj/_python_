from datetime import datetime
print("%02d/%02d/%04d" % (datetime.now().day, datetime.now().month, datetime.now().year))

# Ask the user to input a word in English.
# Make sure the user entered a valid word.
# Convert the word from English to Pig Latin.
# Display the translation result.



word = raw_input("which word to translate ?")
# ATTENTION VERIFIER QU'IL S'AGIT D'UN MOT :
if len(word) > 0 and word.isalpha() == True:
    new_word = word[1:] + word[0] + "ay"
    print(new_word.lower())
else:
    print("empty content")



# process string elements in the list and make them integers
input_list = [str(a) for a in word]
