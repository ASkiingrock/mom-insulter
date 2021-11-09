import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
for item in job_elements:
    '''title_element = item.find("h2", class_="title")
    company_element = item.find("h3", class_="company")
    location_element = item.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()'''
    python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
    print(python_jobs)