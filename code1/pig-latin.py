"""This translates English words into Pig Latin"""
# user input for the english word
orig_word = input("Enter word in English -->" )
# string to attach to the end of a word that begins with a vowel
suf_vowel = "yay"
# string to attach to the end of a word that begins with a consonant
suf_consonant = "ya"
#list of vowels
vowel_list = ["a","e","i","o","u", "A","E","I","O", "U"]
# Establish variable for pig latin word
pig_latin = 0
#punc_list =[".","?", "!", ",", ":", ";"]
#identifies first letter of inputed word
first_letter = orig_word[0]
punc_last = orig_word[-1]

# Identifies if input work contants an non alpha-numeric and removes it from the end
if orig_word.isalpha() == False:
    orig_word = orig_word[:len(orig_word)-1]

# Coverts the english word to pig latin
# Looks for first letter in the list of vowels to determine if the word starts with a vowel or consonant.
# Then determines whether the first letter is capitalized. Then arranges the word into pig latin, capitalizing
# the first letter if necessary bassed on original input.
if  first_letter in vowel_list:
    (first_letter == first_letter.upper())== True
    pig_latin = "".join(orig_word+ suf_vowel+ punc_last)
    print(orig_word + " in pig latin is " + pig_latin)
elif first_letter in vowel_list:
    pig_latin = orig_word+suf_vowel+ punc_last
    print(orig_word + " in pig latin is " + pig_latin)
elif first_letter == first_letter.upper():
     pig_latin = "".join(orig_word[1].upper() + orig_word[2:] + first_letter.lower() + suf_consonant+ punc_last)
     print(orig_word + " in pig latin is " + pig_latin)
else:
    pig_latin = "".join(orig_word[1:] + first_letter + suf_consonant+ punc_last)
    print(orig_word + " in pig latin is " + pig_latin)

