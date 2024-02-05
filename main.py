
def main():
    path = "books/frankenstein.txt"
    text = book_reader(path)
    # print(text)
    print(f"--- Begin report of {path} ---")
    No_of_words = word_counter(text)
    print(No_of_words," words found in the document", "\n")
    letter_tracker_dict = letter_counter(text)
    letter_tracker_list = dict_to_list_coverter(letter_tracker_dict)
    # print(letter_tracker_list)
    for item in sorted(letter_tracker_list, reverse=True, key=lambda item: item["count"]):
        print(f"The '{item["letter"]}' character was found {item["count"]} times")

    print("--- End report ---")

def dict_to_list_coverter(letter_dict):
    letter_tracker_list = []
    for letter, count in letter_dict.items():
        letter_tracker_list.append({"letter": letter, "count": count })
    return letter_tracker_list

def word_counter(straight_string):
    words = straight_string.split()
    return len(words)

def letter_counter(straight_string):
    letter_tracker = {}
    # spaces get removed here
    words = straight_string.lower().split()
    for word in words:
        # nesting isn't efficient but we have to sorta do this anyways
        for letter in word:
            if letter.isalpha(): 
                # check if letter is in the dict 
                if letter_tracker.get(letter) == None:
                    letter_tracker[letter] = 1
                else:
                    letter_tracker[letter] += 1
            else:
                continue
    return letter_tracker



def book_reader(path):    
    with open(path, "r") as file:
        return file.read()

if __name__ == "__main__":
    main()
