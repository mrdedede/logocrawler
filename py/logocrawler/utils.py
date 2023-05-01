import math

def divide_list(primary_list, ammount):
    """
    Given a list and an ammount, this function divides this list, with all members in lists of
    roughly the same size in the desired ammount

    Args:
        primary_list (list): The list we are looking to divide
        ammount (int): The ammount of lists we want to divide them on
    
    returns
        list: list of lists including all terms
    """
    list_chunk = math.ceil(len(primary_list)/ammount)
    divided_list = [primary_list[index:index+list_chunk] for index in range(0, len(primary_list), list_chunk)]
    return divided_list