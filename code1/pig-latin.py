"""This translates English words into Pig Latin"""

# Identifies if input work contants an non alpha-numeric and removes it from the end
#if orig_word.isalpha() == False:
 #   orig_word = orig_word[:len(orig_word)-1]

# Coverts the english word to pig latin
# Looks for first letter in the list of vowels to determine if the word starts with a vowel or consonant.
# Then determines whether the first letter is capitalized. Then arranges the word into pig latin, capitalizing
# the first letter if necessary bassed on original input.


def consonant_convert(orig_word):
    first_letter = orig_word[0]
    suf_consonant = "ya"
    punc_last = orig_word[-1]
    if orig_word.isalpha() == False:
        orig_word = orig_word[:len(orig_word)-1]

    if first_letter == first_letter.upper():
        pig_latin = "".join(orig_word[1].upper()+orig_word[2:]+first_letter.lower()+suf_consonant+punc_last)
    else:
        pig_latin = "".join(orig_word[1:]+first_letter+suf_consonant+punc_last)
    return(pig_latin)

def vowel_convert(orig_word):
    first_letter = orig_word[0]
    suf_vowel = "yay"
    punc_last = orig_word[-1]

    if orig_word.isalpha() == False:
        orig_word = orig_word[:len(orig_word)-1]
        if first_letter == first_letter.upper:
            pig_latin = "".join(orig_word+suf_vowel+punc_last)
        else:
            pig_latin = "".join(orig_word+suf_vowel+punc_last)
    else:
        pig_latin = "".join(orig_word+suf_vowel)
    return(pig_latin)

# if first_letter not in vowel_list:
#    pig_latin = consonant_convert(orig_word, ):
#     #identifies first letter of inputed word
#     first_letter = orig_word[0]
#     punc_last = orig_word[-1]
#     if first_letter not in vowel_list and first_letter == first_letter.upper():
#         pig_latin = "".join(orig_word[1:]+first_letter.lower()+suf_consonant+punc_last)
#         elif pig_latin= "".
def main ():
    # user input for the english word
    orig_word = input("Enter word in English -->" )
    # string to attach to the end of a word that begins with a vowel
    #suf_vowel = "yay"
    # string to attach to the end of a word that begins with a consonant
    #suf_consonant = "ya"
    #list of vowels
    vowel_list = ["a","e","i","o","u", "A","E","I","O", "U"]
    # Establish variable for pig latin word
    pig_latin = 0
    first_letter = orig_word[0]
    #punc_last = orig_word[-1]

    if first_letter in vowel_list:
        pig_latin = vowel_convert(orig_word)
    else:
        pig_latin = consonant_convert(orig_word)
    print(orig_word + " in pig latin is " + pig_latin)
if __name__ == '__main__':
    main()
