from typing import *

import bs4

import process as process


def title_from_soup(
    soup: bs4.BeautifulSoup,
) -> List[str]:
    """
    Get title from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        str: string with title information from soup.
    """
    title_class_name = 'job-title-link break visited'
    title_soup = soup.find('a', class_=title_class_name)

    if not title_soup:
        return

    title = title_soup.text
    title = process.text(title)

    return title


def description_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    """
    Get description from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        List[str]: string with description information from soup.
    """
    description_class_name = "js-description-text"
    description_soup = soup.find('span', class_=description_class_name)

    if not description_soup:
        return

    description = description_soup.text
    description = process.text(description)

    return description


def fixed_price_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    """
    Get fixed prize from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        str: string with the fixed prize information from soup.
    """
    fixed_prize_class_name = "js-budget"
    fixed_prize_soup = soup.find('strong', class_=fixed_prize_class_name)

    if not fixed_prize_soup:
        return

    fixed_prize = fixed_prize_soup.text.strip()

    return fixed_prize


def experience_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    """
    Get experience from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        str: string with the experience information from soup.
    """
    experience_class_name = "js-contractor-tier"
    experience_soup = soup.find('strong', class_=experience_class_name)

    if not experience_soup:
        return

    experience = experience_soup.text.strip()
    experience = process.text(experience)

    return experience


def skills_from_soup(
    soup: bs4.BeautifulSoup,
) -> List[str]:
    """
    Get skills from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        List[str]: list of strings with the skill information from soup.
    """
    skill_class_name = "js-skill d-inline-block"
    skill_soup_list = soup.find_all('span', class_=skill_class_name)

    if not len(skill_soup_list):
        return
    skill_list = [sill_soup.text.strip() for sill_soup in skill_soup_list]
    skill_list = [process.text(skill) for skill in skill_list]

    return skill_list
