import csv
import time
import random
from typing import *

import requests
import bs4
from tqdm import tqdm
from bs4 import BeautifulSoup
from pycookiecheat import chrome_cookies

import extract as extract
import requests_settings as req_settings


def get_soup_from_url(
    url: str,
    referer:str,
) -> BeautifulSoup:
    headers = {
        "User-Agent": random.choice(req_settings.USER_AGENT_LIST),
        "referer": referer,
    }
    cookies = chrome_cookies(url=url)

    resp = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup


def get_data_from_soup(
    soup: bs4.BeautifulSoup,
) -> List[Dict[str, Any]]:
    section_soup_list = soup.find_all("section")

    if not len(section_soup_list) > 3:
        return
    else:
        # NOTE: positions 0, -2 and -1 are not
        section_soup_list = section_soup_list[1:-2]

    data_dict_list = []

    for section_soup in section_soup_list:
        data_dict = {}
        data_dict['title'] = extract.title_from_soup(section_soup)
        data_dict['description'] = extract.description_from_soup(section_soup)
        data_dict['fixed_price'] = extract.fixed_price_from_soup(section_soup)
        data_dict['experience'] = extract.experience_from_soup(section_soup)
        data_dict['skills'] = extract.skills_from_soup(section_soup)
        data_dict_list.append(data_dict)

    return data_dict_list


def get_data_from_upwork():
    keyword = "writing"
    page_num = 1
    data_dict_list = []
    referer = random.choice(req_settings.REFERER_LIST)

    while True:
        print(f"Extracting page {page_num}")
        url = (
            "https://www.upwork.com/search/jobs/?"
            f"page={page_num}&q={keyword}"
        )

        soup = get_soup_from_url(url=url, referer=referer)
        extracted_data_dict_list = get_data_from_soup(soup)

        if not extracted_data_dict_list:
            print(f"{page_num} pages extracted.")
            break

        data_dict_list += extracted_data_dict_list

        referer = url
        page_num += 1
        time.sleep(random.randrange(3, 10))

    return data_dict_list


def write_csv_from_data_dict_list(data_dict_list) -> None:
    csv_file_path = './upwork_data.csv'
    attr_list = list(data_dict_list[0].keys())

    with open(csv_file_path, 'w') as csv_file:
        header = ','.join([attr for attr in attr_list]) + '\n'
        csv_file.write(header)

        for data_dict in tqdm(data_dict_list):
            item_list = ','.join(
                [f'{item}' for item in data_dict.values()]) + '\n'
            csv_file.write(item_list)


if __name__ == '__main__':
    data_dict_list = get_data_from_upwork()
    _none = write_csv_from_data_dict_list(data_dict_list)
