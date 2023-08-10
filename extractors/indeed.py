from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import math


def get_page_count(keyword):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    base_url = "https://www.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    list_list = job_list.find_all("li", recursive=False)
    list_count = len(list_list)-1
    job_count = soup.find(
        "div", class_="jobsearch-JobCountAndSortPane-jobCount")
    job_number = int(job_count.find(
        "span", recursive=False).text.split(" ")[0].replace(",", ""))
    pages = math.ceil(job_number/list_count)
    print(pages)
    return pages

def extract_indeed_jobs(keyword):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
    pages = get_page_count(keyword)
    results=[]
    print("Found", pages, "page")
  
    for page in range(pages):
        base_url = "https://www.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"   
        print("Requesting", final_url)
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        pagination = soup.find("nav", {"role":"navigation"})
        nextPage = pagination.find(attrs={"aria-label": "Next Page"})
        print(nextPage)
        if nextPage != None:
            job_list = soup.find("ul", class_="jobsearch-ResultsList")
            jobs = job_list.find_all("li", recursive=False)
            for job in jobs:
                zone = job.find("div", class_="mosaic-zone")
                if zone == None:
                    anchor = job.select_one("h2 a")
                    title = anchor["aria-label"]
                    link = anchor["href"]
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")
                    job_data = {
                        "link": f"https://www.indeed.com{link}",
                        "company": company.string.replace(","," "),
                        "location": location.string.replace(","," "),
                        "position": title.replace(","," "),
                    }
                    results.append(job_data)
        else:
            return
    return results

