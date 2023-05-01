from extract import get_urls
from transform import find_images, filter_images
from load import write_results
from random import choice
from utils import divide_list
from os import cpu_count
import concurrent.futures

def extract_transform(website_list):
    """
    Applied to be the extraction of information and transformation lifecycle of the script

    Args:
        website_list (list): List of URLs to be consulted

    Returns:
        list: List with all website URLs besides its fetched image
    """
    website_bodies = get_urls(website_list)
    images_map = []
    for index in range(len(website_list)):
        print(website_list[index])
        cur_body = next(website_bodies)
        img_raw = find_images(cur_body)
        img_treated = filter_images(img_raw, website_list[index])
        if len(img_treated) == 1:
            images_map.append([website_list[index], img_treated[0]])
        elif len(img_treated) > 1:
            images_map.append([website_list[index], choice(img_treated)])
        else:
            images_map.append([website_list[index], ''])
    return images_map

def main_lifecycle():
    """
    Runs the main lifecycle of the app, including all function in this file
    """
    websites_list_raw = input("Please input a whitespace-separated list of all websites: ")
    websites_list = websites_list_raw.split(" ")

    # Counting the available CPUs (except when there are less than 1)
    # This will serve as a parameter to our thread creation
    total_cpus = cpu_count()
    if len(websites_list) >= total_cpus:
        if total_cpus <= 3:
            available_cpus = 1
        else:
            available_cpus = total_cpus//2
    else:
        available_cpus = len(websites_list)

    divided_websites_list = divide_list(websites_list, available_cpus)

    with concurrent.futures.ThreadPoolExecutor(max_workers=available_cpus) as executor:
        futures = [executor.submit(extract_transform, cur_websites) for cur_websites in divided_websites_list]
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())
        
        write_results(results)