alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "\"", "#", "$",
            "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]",
            "^", "_", "`", "{", "|", "}", "~", "\n", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "'"]

def encryption(text, keyword):
    # turns "text" into string
    text = "".join(map(str, text))

    # create a list of characters
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "\"", "#", "$",
                "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]",
                "^", "_", "`", "{", "|", "}", "~", "\n", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "'"]

    # initialize variable for while loop which serves to traverse the keyword
    j = 0

    # initialize variable to add encrypted result to
    result = ""

    # traverse through all characters in text
    for i in range(len(text)):
        # initialize variable to the index in "alphabet" of the current character in iteration of "text"
        text_letter_index = alphabet.index(text[i])

        while j < len(keyword):
            # # initialize variable to the index in "alphabet" of the current character in iteration of "keyword"
            keyword_letter_index = alphabet.index(keyword[j])
            j += 1
            if j >= len(keyword):
                # subtracts len(keyword) from j to go back to first letter of keyword essentially rehashing the keyword
                j -= len(keyword)
            else:
                break

        encrypted_letter_index = text_letter_index + keyword_letter_index

        # modulo 96 is done in case encrypted_letter_index is greater than 96 which is the number of characters in "alphabet"
        result += alphabet[encrypted_letter_index % 96]
    return result


def decryption(text, keyword):
    # turns "text" into string
    text = "".join(map(str, text))

    # create a list of characters
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "\"", "#", "$",
                "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]",
                "^", "_", "`", "{", "|", "}", "~", "\n", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "'"]

    # initialize variable for while loop which serves to traverse the keyword
    j = 0

    # initialize a variable to add encrypted result to
    result = ""

    # traverse through all characters in text
    for i in range(len(text)):
        # initialize variable to the index in "alphabet" of the current character in iteration of "text"
        text_letter_index = alphabet.index(text[i])

        while j < len(keyword):
            # # initialize variable to the index in "alphabet" of the current character in iteration of "keyword"
            keyword_letter_index = alphabet.index(keyword[j])
            # adds 1 to j to move to next letter of keyword
            j += 1

            if j >= len(keyword):
                # subtracts len(keyword) from j to go back to first letter of keyword essentially rehashing the keyword
                j -= len(keyword)
            else:
                break
        encrypted_letter_index = text_letter_index - keyword_letter_index

        # modulo 96 is done in case encrypted_letter_index is less than 0
        result += alphabet[encrypted_letter_index % 96]
    return result
