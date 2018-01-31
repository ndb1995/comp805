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
