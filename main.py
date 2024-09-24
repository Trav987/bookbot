def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    countCharDict = {}
    lower_file_contents = file_contents.lower()
    for c in lower_file_contents[0:]:
        try:
            countCharDict[c] += 1
        except KeyError:
            countCharDict[c] = 1

    return countCharDict

def sort_on(dict):

    return dict['value']

def print_report(file_contents):
    words = count_words(file_contents)
    charDict = count_characters(file_contents)
  
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n\n")

    charDict = dict(sorted(charDict.items(),key=lambda item: item[1], reverse=True))

    for c,num in charDict.items():
        if c.isalpha():
            print(f"The \'{c}\' character was found \'{num}\' times")
    
    print("--- End report ---")




def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        print_report(file_contents)






main()