def character_frequency(string):
    frequency_dict = {}
    for char in string:
        if char.isalpha(): 
            char = char.lower()
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict

if __name__ == "__main__":
    print(character_frequency("Hello World!")) 
    print(character_frequency("123 ABC abc!")) 
    print(character_frequency(""))  
    print(character_frequency("AaBbCc"))

