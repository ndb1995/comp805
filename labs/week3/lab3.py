def switch_case(str_list):
    """
    Maps strings in the str_list to a new string of
    same characters, but the first letter contains
    the opposite case
    string_list: list of strings
    Returns: list of original strings, but with
    opposite casing
    """
    string_list = []
    for word in str_list:
        string_list.append(word[0].capitalize() + word[1:])
    return string_list

def only_even(mixed_list):
    """
    Filters out odd integers and strings that
    contain an odd number of characters.
    mixed_list: list of integers and/or strings
    Returns: list of only integers and strings that
    are even or have an even number of characters.
    """
    even_list = []
    for mixed in mixed_list:
        if type(mixed) == int:
            if mixed % 2 == 0:
                even_list.append(mixed)
        else:
            if len(mixed) % 2 == 0:
                even_list.append(mixed)
    return even_list

def greatest_difference(num_list):
    """
    Finds the maximum and minimum numbers in a_list
    and computes the difference.
    num_list: list of numbers
    Returns: the difference between the maximum and
    minimum numbers in num_list
    """
    high = max(num_list)
    low = min(num_list)
    return "High %d minus low %d equals" % (high, low), high - low

def make_title(words):
    """
    Maps words in a list to words in the same list,
    but as titled strings.
    words: list of words
    Returns:
    """

def test_title(names):
    """
    Filters out capitalized and non- cap words into
    their respective lists.
    names: list of names
    Returns: both lists for review
    """
    caps = []
    non_caps = []
    for name in names:
        if name.istitle():
            caps.append(name)
        else:
            non_caps.append(name)
    return caps, non_caps

def create_word(char_list):
    """
    Takes a list of characters and creates a word
    (list with alpha chars only) from them.
    letters: list of etters
    Returns: list that has alpha characters only
    """

def three_times_nums(num_list):
    """
    Maps numbers in the num_list to numbers that are
    3 times the original value
    num_list: list of numbers
    Returns: list of numbers that are of three times
    the values in num_list
    """
    three_times = []
    for num in num_list:
        three_times.append(num * 3)
    return three_times

def keep_lowercase(str_list):
    """
    Filters out strings that have uppercase values
    str_list: list of strings
    Returns: list of strings that do not contain
    uppercase values
    """
    lowercase = []
    for word in str_list:
        if not word.isupper():
            lowercase.append(word)
    return lowercase

def multiplication_total_of(num_list):
    """
    Multiplies all the numbers in num_list together
    and gives the total
    num_list: list of numbers
    Returns: the multiplied total of the numbers in
    the num_list
    """
    product = 1
    for num in num_list:
        product *= num
    return product


def square_nums(number_list):
    """
    Maps numbers in the number_list to numbers of
    same value, but squares the number given
    number_list: list of numbers
    Returns: list from number_list which are squared
    """
    squared_nums = []
    for num in number_list:
        squared_nums.append(num*num)
    return squared_nums

def lessthan_5(num_list):
    """
    Filters out numbers less than five
    num_list: list of numbers
    Returns: list of numbers in the original list
    that are less than five
    """
    lessthan = []
    for num in num_list:
        if num < 5:
            lessthan.append(num)
    return lessthan

def subtraction_of(number_list):
    """
    Subtracts the numbers in number_list
    number_list: list of numbers
    Returns: the difference of the numbers in the
    number_list
    """

def double_nums(num_list):
    """
    Maps numbers in the num_list to their doubles
    num_list: list of numbers
    Returns: list of doubled numbers
    """

def remove_special_characters(string_list):
    """
    Filters out strings that have non-alphanumeric
    elements
    char_list: list of strings
    Returns: list of strings that have only letters
    or numbers in them
    """
