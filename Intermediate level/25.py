# Q25: A spell checker can be a helpful tool for people who struggle to spell words correctly. In this exercise, you will write a program that reads a file and displays all of the words in it that are misspelled. Misspelled words will be identified by checking each word in the file against a list of known words.
def remove_punctuation_and_lower(text):
    clean_text = ""
    i = 0
    while i < len(text):
        char = text[i]
        
        is_punc = 0
        if char == ',' or char == '.' or char == '!' or char == '?' or char == ':':
            is_punc = 1
        
        if is_punc == 1:
            clean_text = clean_text + ' '
        else:
            if 'A' <= char <= 'Z':
                clean_text = clean_text + chr(ord(char) + 32)
            else:
                clean_text = clean_text + char
        i = i + 1
    return clean_text

file_to_check = "check.txt"
known_words_file = "known.txt"

f_known = open(known_words_file, 'w')
f_known.write("apple banana orange")
f_known.close()

f_check = open(file_to_check, 'w')
f_check.write("I like applez, banana and orange.")
f_check.close()

try:
    f_known = open(known_words_file, 'r')
    known_words = {}
    
    known_content = f_known.read()
    known_words_list = known_content.split()
    for word in known_words_list:
        known_words[word] = True
    f_known.close()

    f_check = open(file_to_check, 'r')
    check_content = f_check.read()
    f_check.close()

    clean_content = remove_punctuation_and_lower(check_content)
    
    check_words = clean_content.split()
    misspelled = {}
    
    for word in check_words:
        if len(word) > 0:
            if word not in known_words:
                misspelled[word] = True

    print("Misspelled words found:")
    for word in misspelled:
        print(word)

except:
    print("Error: Could not perform file operations.")