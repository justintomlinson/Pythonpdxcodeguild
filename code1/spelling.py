""" Program checks to see if word follows I before E except after C"""

orig_word = input ("Word?  ")
ie_combo = "ie"
ei_combo = "ei"

c_find = orig_word.find("c")
ie_find = orig_word.find("ie")
ei_find = orig_word.find("ei")



if c_find >= 0:
    if "ie" in orig_word:
        if c_find > ie_find:
            print(orig_word + " does follow the rule")
        elif c_find < ie_find:
            print (orig_word + " doesnt follow the rule")
    elif "ei" in orig_word:
        if c_find < ei_find:
            print(orig_word +" does follow the rule")
        elif c_find > ei_find:
            print(orig_word + " does not follow the rule")
elif "ie" in orig_word:
        print(orig_word + " does follow the rule.")
elif "ei" in orig_word:
        print(orig_word + " does not follow the rule")


