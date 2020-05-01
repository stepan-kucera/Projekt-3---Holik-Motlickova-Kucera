
def read_dictionary(dictionary_name):
    dictionary_words = []
    input_file = open(dictionary_name, "r")
    for line in input_file:
        word = line.strip()
        dictionary_words.append(word)
    input_file.close()
    return dictionary_words


def read_text(text_name):
    words = []
    input_file = open(text_name, "r")
    for line in input_file:
        words_on_line = line.strip().split()
        for word in words_on_line:
            words.append(word.strip(" .,!/':;-_?").lower())
    input_file.close()
    return words


def find_errors(dictionary_words, text_words):
    misspelled_words = []
    for word in text_words:
        if word not in dictionary_words:
            misspelled_words.append(word)
    return misspelled_words


def print_errors(error_list):
    print("Slova s pravopisnou chybou jsou: ")
    for word in error_list:
        print(word)

def first_order_variants(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in abeceda if b]
    inserts = [a + c + b for a, b in splits for c in abeceda]
    return set(deletes + transposes + replaces + inserts)


def second_order_variants(word):
    return set(e2 for e1 in first_order_variants(word) for e2 in first_order_variants(e1) if e2 in dictionary)


def known(words):
    return set(w for w in words if w in dictionary)


def correct(word):
    candidates = known(word) or known(*first_order_variants(word)) or second_order_variants(word) or [word]
    return max(candidates, key=dictionary.get)


def guesses(word):
    result = list(known(*first_order_variants(word)))
    result.sort()
    return result


def add(word, priority=4):
    dictionary[word.lower().strip()] = priority


def main():
    print("Vítejte v kontrole pravopisu")
    dictionary = input("Zadejte prosím název souboru slovníku v počítači: ")
    text = input("Zadejte prosím název souboru s textem ke kontrole: ")
    dictionary_list = read_dictionary(dictionary)
    text_list = read_text(text)
    error_list = find_errors(dictionary_list, text_list)
    print_errors(error_list)
    edits1(word)

main()
