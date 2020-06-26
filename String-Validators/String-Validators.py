def word_split(word):
    return [char for char in word]


def alphanumeric_characters(list):
    """

        :type list: object
    """
    bool_alnum = []
    final_value = True
    for i in range(len(list)):
        bool_alnum.append(list[i].isalnum())

    final_value = True in (i for i in bool_alnum)

    return final_value


def alphabetical_characters(list):
    """

        :type list: object
    """
    bool_alpha = []
    final_value = False
    for i in range(len(list)):
        bool_alpha.append(list[i].isalpha())

    final_value = True in (i for i in bool_alpha)

    return final_value


def digit(list):
    """

    :type list: object
    """
    bool_digit = []
    final_value = True
    for i in range(len(list)):
        bool_digit.append(list[i].isdigit())

    final_value = True in (i for i in bool_digit)

    return final_value


def lowercase_characters(list):
    """

        :type list: object
    """
    bool_lowercase_characters = []
    final_value = True
    for i in range(len(list)):
        bool_lowercase_characters.append(list[i].islower())

    final_value = True in (i for i in bool_lowercase_characters)

    return final_value


def uppercase_characters(list):
    """

        :type list: object
    """
    bool_uppercase_characters = []
    final_value = True
    for i in range(len(list)):
        bool_uppercase_characters.append(list[i].isupper())

    final_value = True in (i for i in bool_uppercase_characters)

    return final_value


if __name__ == '__main__':
    s = input()

    # Splitting the words
    split_it = word_split(s)

    # checking alphanumeric characters
    check_alphanumeric_characters = alphanumeric_characters(split_it)
    print(check_alphanumeric_characters)

    # checking alphabetical characters
    check_alphabetical_characters = alphabetical_characters(split_it)
    print(check_alphabetical_characters)

    # checking for digits
    check_digit = digit(split_it)
    print(check_digit)

    # checking lowercase characters
    check_lowercase_characters = lowercase_characters(split_it)
    print(check_lowercase_characters)

    # Checking for uppercase characters
    check_uppercase_characters = uppercase_characters(split_it)
    print(check_uppercase_characters)
