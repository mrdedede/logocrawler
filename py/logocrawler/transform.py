import re

def find_images(body):
    """
    Given a string (preferably a body from HTTP request),
    this function tries to find image links in them

    Args:
        body (str): The string where we will search for the images

    Returns:
        list: List of references of images found in the given document
    """
    image_regex = r'(?:https?:\/\/)?[\w\/\-?=%.]+\.(?:svg|png|jpg|jpeg)'
    images_found = list(set(re.findall(image_regex, body)))
    return images_found

def filter_images(images_list, url):
    """
    Given a list of Image URLs and a URL from the main website this function aims to
    filter which of the Image URLs most closely resemble the logo for a page

    Args:
        images_list (list): List containing image URLs
        url (str): String relating to the URL

    Returns
        list: A list of all the filtered images that may most closely resemble a logo
    """
    if images_list is None or len(images_list) == 0:
        return []
    elif len(images_list) == 1:
        return [link_images(images_list[0], url)]

    preprocessed_paths = [link_images(img, url) for img in images_list]
    preprocessed_paths = list(filter(lambda img: len(img) >= 16, preprocessed_paths))
    preprocessed_paths = list(filter(lambda img: not re.search('[2-9]x.\.(png|jpg|jpeg|svg)', img), preprocessed_paths))
    preprocessed_paths = list(filter(lambda img: "testimonial" not in img, preprocessed_paths))
    preprocessed_paths = list(filter(lambda img: "reversed" not in img, preprocessed_paths))
    if len(preprocessed_paths) == 1:
        return preprocessed_paths

    url_main_name = url.split('.')[0]
    website_name = list(filter(lambda img: re.search(f'(?i){url_main_name}', img.split('/')[-1]), preprocessed_paths))
    if len(website_name) == 1:
        return website_name

    only_logos = list(filter(
        lambda img: re.search('(?i)([-_])?logo', img), preprocessed_paths))
    if len(only_logos) > 1:
        only_website_logos = list(filter(
            lambda img: re.search(f'(?i){url_main_name}', img.split('/')[-1]), only_logos))
        if len(only_website_logos) >= 1:
            return only_website_logos
        else:
            only_home_logos = list(filter(
                lambda img: re.search('(?i)home', img.split('/')[-1]), only_logos))
            if len(only_home_logos) >= 1:
                return only_home_logos
            else:
                return only_logos
    elif len(only_logos) == 1:
        return only_logos
    else:
        return preprocessed_paths

def link_images(img, url):
    """
    Given an image URL and a website URL from which the image has been fetched from, this
    function will treat the image URL to be foundable through a get request

    Args:
        img (str): URL of where the image is located
        url (str): URL of the website where the image has been fetched from

    Returns:
        str: fixed img URL
    """
    # There are probably better approaches to check this.
    domain_endings = ['.com', '.ai', '.net', '.io', '.me', '.co', '.ca', '.gov', '.br', '.jp',
                      '.cn', '.zh', '.ru', '.edu', '.es', '.pe', 'co', '.ar', '.uy', '.pt', '.us',
                      '.ae', '.pl']
    if img.startswith('.'):
        img = img[1:]
    if '=' in img:
        img = img.split('=')[1]
    if img[0:4] != 'http' and img[0] != '/':
        img = f'/{img}'
    if img[0] == "/" and img[1] != "//":
        img = f'http://{url}{img}'
    if not re.search(f'({"|".join(domain_endings)})', img):
        img = f'http://{url}{img}'
    if "http" not in img and '//' in img:
        img = f'http:{img}'
    return img