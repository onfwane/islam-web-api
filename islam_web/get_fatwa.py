from .helpers import filter_fatwa_page, base_url
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from bs4.element import Tag
from typing import Union
from user_agent import generate_user_agent
import requests


def get_fatwa(fatwa_num: int = None, fatwa_link: str = None) -> dict:
    if fatwa_num and fatwa_link:
        raise Exception("Can not take a value for fatwa_num and fatwa_link together.")
    elif fatwa_num is None and fatwa_link is None:
        raise Exception("Can not take no values.")
    elif fatwa_link and not isinstance(fatwa_link, str):
        raise ValueError(
            f"Excepted type of str for fatwa_link got {fatwa_link.__class__.__name__}"
        )
    elif fatwa_num and not isinstance(fatwa_num, int):
        raise ValueError(
            f"Excepted type of int for fatwa_num got {fatwa_num.__class__.__name__}"
        )
    if fatwa_num:
        api_url: str = base_url + "/ar/fatwa/" + str(fatwa_num)
    elif fatwa_link:
        api_url: str = fatwa_link
    default_headers: dict[str] = {"User-Agent": generate_user_agent()}
    data: dict = {}
    try:
        response: requests.Response = requests.get(api_url, headers=default_headers)
    except Exception as e:
        data["ok"] = False
        data["status_code"] = response.status_code
        data["error_message"] = str(e)
    else:
        data["status_code"] = response.status_code
        if response.status_code != 200:
            data["ok"] = False
            data["error_message"] = "status code not equals 200."
        else:
            soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
            filtered_fatwa: Union[dict, None] = filter_fatwa_page(soup)
            if filtered_fatwa is None:
                data["ok"] = False
                data["error_message"] = "No results found."
            else:
                data["ok"] = True
                data["result"] = filtered_fatwa
    return data
