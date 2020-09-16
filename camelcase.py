import re

# This program uses the .title(), .split(), and .join() functions to convert a sentence into camel case.

def display_instructions():
    print('Enter a sentence to convert to camelCase. ')

def display_banner():
    """ Display program name in banner """
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

def camel_case(sentence):
    try:
        no_newline = re.sub('\n', ' ', sentence) #replace newlines with a space
        no_special = re.sub('[^a-zA-Z1-9 ]', '', no_newline) #remove characters that aren't alphanumeric
        split_sentence = no_special.strip().split(" ")
        for s in range(len(split_sentence)):
            split_sentence[s] = split_sentence[s].title() #uppercase first letter, lowercase the rest for each word
        split_sentence[0] = split_sentence[0].lower()   # First word must be all lowercase
        join_sentence = "".join(split_sentence)

        return join_sentence
    except (TypeError):
        print('Sentences must include only letters, no digits.')
        return '' #return empty string instead of None

def main():
    display_banner()
    display_instructions()
    sentence = input("Enter a sentence: ")
    output = camel_case(sentence)
    print(output)

if __name__ == '__main__':
    main()