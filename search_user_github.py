import requests
from bs4 import BeautifulSoup
import csv_writer
import re


def get_inidividual_github_details(href):
    response = requests.get(href)
    response_code = response.status_code
    if response_code != 200:
        print("Error")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'lxml')
    text = dom.get_text()
    try:
        email = re.findall(r'[a-z0-9]+@\S+.com', str(text))
        return email[0]
    except:
        return ''


def get_github_search_results():
    url_to_call = "https://github.com/search?q=hackathon+location%3Aindia+language%3APython&type=users"
    response = requests.get(url_to_call)
    response_code = response.status_code
    if response_code != 200:
        print("Error")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all_users = dom.select('div.Box-row')
    for each_user in all_users:
        description = (each_user.p.text.strip())
        user = each_user.find("a", {"class": "mr-1"})
        location = each_user.find("div", {"class": "text-small"}).text
        href = "https://github.com{}".format(user.attrs["href"])
        user_info = [user.text, user.attrs["href"],
                     description, location.strip(), href]
        email = get_inidividual_github_details(href)
        if(email):
            user_info.append(email)
        print(user_info)

        try:
            csv_writer.csv_writer(user_info)
        except:
            continue


if __name__ == "__main__":
    print("Started Scrapping")
    get_github_search_results()
    print("Finished Scrapping")
