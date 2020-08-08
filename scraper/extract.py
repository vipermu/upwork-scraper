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
    title_class_name = "job-title-link break visited ng-binding"
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
    description_class_name = "m-sm-bottom ng-isolate-scope"
    description_soup = soup.find('div', class_=description_class_name)

    if not description_soup:
        return

    description = description_soup.text
    description = process.text(description)
    if description.split(' ')[-1] in ['less', 'more']:
        decription = ' '.join(description.split(' ')[:-1])

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
    fixed_prize_soup = soup.select_one(
        'span[data-ng-if="::jsuJobBudgetController.job.amount.amount"]')

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
    experience_class_name = "js-contractor-tier ng-binding ng-scope"
    experience_soup = soup.find('span', class_=experience_class_name)

    if not experience_soup:
        return

    experience = experience_soup.text.strip()
    experience = process.text(experience)

    return experience


def skills_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    """
    Get skills from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        str: strings representing the skills information from soup.
    """
    skill_class_name = "js-skill d-inline-block ng-scope"
    skill_soup_list = soup.find_all('span', class_=skill_class_name)

    if not len(skill_soup_list):
        return

    skill_list = [skill_soup.text.strip() for skill_soup in skill_soup_list]
    skill_list = [process.text(skill) for skill in skill_list]
    skill = ' - '.join(skill_list)

    return skill


def duration_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    """
    Get duration from soup element.

    Args:
        soup (bs4.BeautifulSoup): soup element.

    Returns:
        str: strings representing the duration information from soup.
    """
    duration_class_name = "js-duration ng-binding"
    duration_soup = soup.find('span', class_=duration_class_name)

    if not duration_soup:
        return
    duration = duration_soup.text.strip()
    # NOTE: remove 'est time'
    duration = ' '.join(duration.split(' ')[2:]).lower()

    return duration


def hourly_prize_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    hourly_prize_soup = soup.select_one(
        'strong[data-ng-if="::jsuJobTypeController.isHourlyRange()"]')

    if not hourly_prize_soup:
        return

    hourly_prize = hourly_prize_soup.text.strip()
    hourly_prize = ' '.join(hourly_prize.split(' ')[1:])

    return hourly_prize


def proposals_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    proposals_soup = soup.select_one(
        'strong[data-ng-bind="jsuJobProposalsController.proposalsTier"]')

    if not proposals_soup:
        return
    proposals = proposals_soup.text.strip()

    return proposals


def spent_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    spent_soup = soup.select_one(
        'strong[data-ng-bind="::jsuJobClientSpentTierController.totalSpent|moneyRange"]')

    if not spent_soup:
        return

    spent = spent_soup.text.strip()

    return spent


def location_from_soup(
    soup: bs4.BeautifulSoup,
) -> str:
    location_class_name = "text-muted client-location ng-binding"
    location_soup = soup.find('strong', class_=location_class_name)

    if not location_soup:
        return

    location = location_soup.text.strip()
    location = location.lower()

    return location
