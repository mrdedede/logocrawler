import random

def get_websites_list_csv(csv_file):
    """
    Given a csv file, this function will open it and return a list of all websites within it

    Args:
        csv_file (str): The location where the csv file that needs to be read is
    
    returns:
        list: list of all websites within the file
    """
    websites_file = open(csv_file, mode='r')
    websites_list_raw = websites_file.readlines()
    websites_file.close()
    fix_links = lambda link: link.split("\n")[0]
    return list(map(fix_links, websites_list_raw))

def get_websites_list_ammount(csv_file, ammount):
    """
    Given a csv file, this function will open it and return a list of a specific size of websites within it

    Args:
        csv_file (str): The location where the csv file that needs to be read is
        ammount (int): The ammount of websites that is wanted to be retrieved
    
    returns:
        list: List with the correct ammount of websites
    """
    all_websites = get_websites_list_csv(csv_file)
    return get_list_ammount(all_websites, ammount)

def get_random_websites(csv_file, ammount=None):
    """
    Given a csv file, this function will open it and return a list of a specific size of websites within it

    Args:
        csv_file (str): The location where the csv file that needs to be read is
        ammount (int): The ammount of websites that is wanted to be retrieved
    
    returns:
        list: List with the correct ammount of websites
    """
    all_websites = get_websites_list_csv(csv_file)
    random.shuffle(all_websites)
    return get_list_ammount(all_websites, ammount)

def get_list_ammount(cur_list, ammount):
    """
    Returns a sub-list of the input list containing only the specified number of elements.

    Args:
        cur_list (list): The input list.
        ammount (int or None): The desired number of elements in the sub-list. If None, the entire input list is returned.

    Returns:
        list: A sub-list of the input list containing only the specified number of elements.
    """
    if ammount is None:
        return cur_list
    elif ammount <= len(cur_list):
        return cur_list[0:ammount]
    else:
        return cur_list