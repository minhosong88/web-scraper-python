from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import math


# def get_page_count(city, state_abbrev):
#     options = Options()
#     options.add_experimental_option("detach", True)
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     browser = webdriver.Chrome(service=Service(
#         ChromeDriverManager().install()), options=options)

#     base_url = "https://www.zillow.com/"
#     browser.get(f"{base_url}{city}-{state_abbrev}")
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     house_list = soup.find("ul", class_="List-c11n-8-84-3__sc-1smrmqp-0")
#     houses = house_list.find_all(
#         "li", class_="ListItem-c11n-8-84-3__sc-10e22w8-0")
#     house_count = len(houses)
#     result_count = int(
#         soup.find("span", class_="result-count").text.split(" ")[0].replace(",", ""))
#     pages = math.ceil(result_count/house_count)
#     return pages


# def extract_zillow_houses(city, state_abbrev):
#     options = Options()
#     options.add_experimental_option("detach", True)
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     browser = webdriver.Chrome(service=Service(
#         ChromeDriverManager().install()), options=options)
#     pages = 1
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     pagination = soup.find("nav", {"role": "navigation"})
#     nextPage = pagination.find(attrs={"title": "Next page"})
#     results=[]
#     print("Found", pages, "page")
#     for page in range(pages):
#         base_url = "https://www.zillow.com/"
#         final_url = f"{base_url}{city}-{state_abbrev}/{page}_p"
#         print("Requesting", final_url)
#         browser.get(final_url)
#         if not nextPage.has_attr("disabled"):
#             house_list = soup.find("ul", class_="List-c11n-8-84-3__sc-1smrmqp-0")
#             houses = house_list.find_all(
#                 "li", class_="ListItem-c11n-8-84-3__sc-10e22w8-0")
#             for house in houses:
#                 ad = house.find("p", recursive=False)
#                 if ad == None:
#                     anchor = house.select_one("a")
#                     link = anchor["href"]
#                     address = anchor.find("address")
#                     price = house.find(attrs={"data-test":"property-card-price"})
#                     condition = house.find("ul")
#                     house_data = {
#                         "link": link,
#                         "address": address.string.replace(",", " "),
#                         "condition": condition.string,
#                         "price": price.string.replace(",","")
#                     }
#                     results.append(house_data)
#                     print(results)
#         else:
#             return
#     return results

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
pages = 1
city = "olympia"
state_abbrev = "wa"

results=[]
print("Found", pages, "page")
for page in range(pages):
    base_url = "https://www.zillow.com/"
    final_url = f"{base_url}{city}-{state_abbrev}/{page+1}_p"
    print("Requesting", final_url)
    browser.get(final_url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find(attrs={"aria-label":"Pagination"})
    print(pagination)
    nextPage = pagination.find("a", class_="StyledButton-c11n-8-84-3__sc-wpcbcc-0")
    print(nextPage)
    # if not nextPage.has_attr("disabled"):
    #     house_list = soup.find("ul", class_="List-c11n-8-84-3__sc-1smrmqp-0")
    #     houses = house_list.find_all(
    #         "li", class_="ListItem-c11n-8-84-3__sc-10e22w8-0")
    #     for house in houses:
    #         ad = house.find("p", recursive=False)
    #         if ad == None:
    #             anchor = house.select_one("a")
    #             link = anchor["href"]
    #             address = anchor.find("address")
    #             price = house.find(attrs={"data-test":"property-card-price"})
    #             condition = house.find("ul")
    #             house_data = {
    #                 "link": link,
    #                 "address": address.string.replace(",", " "),
    #                 "condition": condition.string,
    #                 "price": price.string.replace(",","")
    #             }
    #             results.append(house_data)
    #             print(results)


    #StyledPagination-c11n-8-84-3__sc-2vwigm-0