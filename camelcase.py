# This program uses the .title(), .split(), and .join() functions to convert a sentence into camel case.

def display_instructions():
    print('Enter a sentence to convert to camelCase. ')

def display_banner():
    """ Display program name in banner """
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

def camel_case(sentence):
    cap_sentence = sentence.title()
    split_sentence = cap_sentence.split(" ")

    split_sentence[0] = split_sentence[0].lower()   # First word must be lowercase

    join_sentence = "".join(split_sentence)
    return join_sentence

def main():
    display_banner()
    display_instructions()
    sentence = input("Enter a sentence: ")
    output = camel_case(sentence)
    print(output)

if __name__ == '__main__':
    main()