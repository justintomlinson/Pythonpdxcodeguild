"""This translates English words into Pig Latin"""
# user input for the english word
orig_word = input("Enter word in English -->" )
# string to attach to the end of a word that begins with a vowel
suf_vowel = "yay"
# string to attach to the end of a word that begins with a consonant
suf_consonant = "ya"
#list of vowels
vowel_list = ["a","e","i","o","u"]
# Establish variable for pig latin word
pig_latin = 0

#identifies first letter of inputed word
first_letter = orig_word[0]

# Coverts the english word to pig latin
# Looks for first letter in the list of vowels. If true adds the "yay" to input word,
# if false moves the first letter to end of the orginal string and adds "ya"
if  first_letter in vowel_list:
    (first_letter == first_letter.upper())== True
    pig_latin = "".join(first_letter +orig_word[1:]+ suf_vowel)
    print(orig_word + " in pig latin is " + pig_latin)
elif first_letter in vowel_list:
    pig_latin = orig_word+suf_vowel
    print(orig_word + " in pig latin is " + pig_latin)
elif first_letter == first_letter.upper():
     pig_latin = "".join(orig_word[1].upper() + orig_word[1:] + first_letter.lower() + suf_consonant)
     print(orig_word + " in pig latin is " + pig_latin)
else:
    pig_latin = "".join(orig_word[1:] + first_letter + suf_consonant)
    print(orig_word + " in pig latin is " + pig_latin)

