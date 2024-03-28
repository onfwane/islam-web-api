from .helpers import results_filter, base_url
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from bs4.element import Tag
from user_agent import generate_user_agent
import requests


def search(query: str, params: dict = {}, headers: dict = {}) -> dict:
    api_url: str = base_url + "/ar/SearchEngine/fattab.php"
    default_params: dict[str] = {
        "debug_srch_url": "0",
        "lang": "A",
        "myRange": "50",
        "synonym": "0",
        "indexid": "-2",
        "device": "1",
        "generalsearch": "1",
        "exact": "0",
        "extended": "0",
        "range": "0",
        "txt": query.strip(),
        "R1": "7",
        "R2": "0",
        "_": "1710867514538",
    }
    default_headers: dict[str] = {
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": generate_user_agent(),
    }
    default_params.update(params)
    default_headers.update(headers)
    data: dict = {}
    try:
        response: requests.Response = requests.get(
            api_url, params=default_params, headers=default_headers
        )
        data["status_code"] = response.status_code
    except Exception as e:
        data["ok"] = False
        data["error_message"] = str(e)
    else:
        if response.status_code != 200:
            data["ok"] = False
            data["error_message"] = "status code not equals 200."
        else:
            soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
            search_results_ul: Tag = soup.find("ul", class_="oneitems")
            if search_results_ul is None:
                data["ok"] = False
                data["error_message"] = "No results found."
            else:
                search_results: ResultSet = search_results_ul.find_all("li")
                filtered_results: list[dict] = results_filter(search_results)
                data["ok"] = True
                data["results"] = filtered_results
    return data
