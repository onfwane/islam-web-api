from bs4 import BeautifulSoup
from bs4.element import ResultSet
from bs4.element import Tag
from typing import Union

base_url: str = "https://www.islamweb.net"


def results_filter(results: ResultSet) -> list[dict]:
    if not isinstance(results, ResultSet):
        raise TypeError(
            f"results argument must type of ResultSet got {results.__class__.__name__}"
        )
    data: list = []
    for result in results:
        title: str = result.find("h5").text.strip()
        link: str = result.find("a")["href"].rsplit("/", 1)[0]
        description: str = result.find("div", class_="desc").text.strip()
        category: str = (
            result.find("div", class_="book-name").text.strip().replace("\n", " > ")
        )
        data.append(
            {
                "title": title,
                "link": base_url + link,
                "description": description,
                "category": category,
            }
        )
    return data


def filter_fatwa_page(fatwa_page: BeautifulSoup) -> Union[dict[str], None]:
    if not isinstance(fatwa_page, BeautifulSoup):
        raise ValueError(
            f"Excepted type of BeautifulSoup for fatwa_page argument got {fatwa_page.__class__.__name__}"
        )
    elif fatwa_page.find("div", "alert-danger"):
        return
    fatwa_head: Tag = fatwa_page.find("div", class_="item-fatwa")
    fatwa_title: str = fatwa_head.find("div", class_="top-item").text.strip()
    fatwa_info_items: Tag = (
        fatwa_head.find("div", class_="footer-item").find("span").find_all("samp")
    )
    fatwa_num: int = int(fatwa_info_items[0].find("a").text.strip())
    fatwa_views: int = int(fatwa_info_items[1].find("a").text.strip())
    fatwa_date: str = fatwa_info_items[2].find("a").text.strip()
    fatwa_quest: str = (
        fatwa_page.find("div", "quest-fatwa")
        .find("div", attrs={"itemprop": "text"})
        .text
    )
    fatwa_answer: str = (
        fatwa_page.find("div", attrs={"itemprop": "acceptedAnswer"})
        .find("div", attrs={"itemprop": "text"})
        .text
    )
    data: dict = {
        "fatwa_title": fatwa_title,
        "fatwa_num": fatwa_num,
        "fatwa_views": fatwa_views,
        "fatwa_date": fatwa_date,
        "question": fatwa_quest.strip("\n"),
        "answer": fatwa_answer.strip("\n"),
    }
    return data
