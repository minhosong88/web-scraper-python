from requests import get
from bs4 import BeautifulSoup

fullstack_url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
backend_url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"
base_url="https://weworkremotely.com/remote-jobs/search?&term="

search_term = "python"

response = get(f"{base_url}{search_term}");
if response.status_code != 200:
    print("Cane't request website");
else:
    soup = BeautifulSoup(response.text,"html.parser");
    print(soup.find_all("section", class_="jobs"))
