def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared_nums
    """

    squared_list = []
    for number in num_list:
        squared_list.append(number * number)
    return(squared_list)

def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are title_list
    """
    correct_list = []
    for title in title_list:
        if (type(title) != int):
            if (title.istitle()):
                correct_list.append(title)
            else:
                title_listtitle = ""
    return(correct_list)

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: ad dictionary with:
     key: string that is the name of the inventory item
     value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """
    for key, value in inventory.iteritems():
            inventory[key] = value + 10
    return (inventory)

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
       key: tring that is the name of the inventory item
       value: nteger that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """
    for key in list(inventory.keys()):
            if (inventory[key] == 0):
                del inventory[key]
    return (inventory)

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    avg_grades = []
    for key,value in grades.iteritems():
        avg_grades.append(key)
        avg_grades.append(sum(value)/ float(len(value)))
    return (avg_grades)
