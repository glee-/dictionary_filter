
#Read word list
f = open("words.txt", "r")
words = []
line = True
while line:
    line = f.readline()
    words.append(line.strip())

##Takes in two lists of letters
# accept = ["a", "b", "c"]
# reject = ["d", "e", "f"]
def solve(accept, reject, used):

    new_words = []

    for word in words:
        valid = True
        for letter in accept:
            if letter not in word or "(" in word or "-" in word:
                valid = False

        if valid:
            new_words.append(word)

    words_buffer = []
    while reject:
        letter = reject.pop(0)
        for word in new_words:
            if letter not in word:
                words_buffer.append(word)
        new_words = words_buffer

    for word in used:
        if word in new_words:
            new_words.remove(word)

    return max(new_words, key=len)

def run():
    print("End the program by pressing '.'")
    accept, reject = "",""
    used_words = []
    while True:
        accept = input("Accept: ")
        reject = input("Reject: ")

        if accept == "." or reject == ".":
            break
        #Assume the inputs are not separated by any delimiter
        accept = list(accept)
        reject = list(reject)

        word = solve(accept, reject, used_words)
        used_words.append(word)
        print(used_words)
        print(word)

run()
