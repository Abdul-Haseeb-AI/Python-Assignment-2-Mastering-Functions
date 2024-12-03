def freq_chk(string): # function to cheak frequency
    freq_dict = {}      # empty dictionary
    for i in string:
        if i in freq_dict:  # cheak if character is in dictionary(freq_dict)
            freq_dict[i] += 1   # if True add value or update to freq_dict
        else:
            freq_dict[i] = 1    # if False only add value to freq_dict
    return freq_dict
user_input = input("Enter String : ")
user_input = user_input.lower()
print("frequency : ",freq_chk(user_input))