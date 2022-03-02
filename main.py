from pydoc import classname
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

success = 0
fail = 0

companies = []

fieldnames = ["name",
              "type", "rate", "description", "accreditations", "treatment", "programs", "financials", "levels_of_care", "clinical_services", "amenities", "address","url", "website", "phone"]


def getCompanyInfo(link):

    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    programsHTML = soup.find(id="programs").find_all("p")
    financialsHTML = soup.find(id="financials").find_all("p")
    amenitiesHTML = soup.find(id="amenities").find_all(class_="text")
    accreditationsHTML = soup.find(id="accreditations").find_all("h3")
    treatmentsHTML = soup.find(id="treatment").find_all("h3")
    levelOfCareHTML = soup.find(id="level_of_care").find_all("h3")
    clinicalServicesHTML = soup.find(id="clinicalservices").find_all("h3")

    accreditations = []
    treatments = []
    levelOfCares = []
    clinicalServices = []
    programs = []
    financials = []
    amenities = []

    try:
        for program in programsHTML:
            programs.append(program.text.replace("\n", "").replace(":", ""))
    except:
        print("program cannot be added")

    try:
        for financial in financialsHTML:
            financials.append(financial.text.replace(
                "\n", "").replace(":", ""))
    except:
        print("financial cannot be added")

    try:
        for amenity in amenitiesHTML:
            amenities.append(amenity.text.replace("\n", "").replace(":", ""))
    except:
        print("amenity cannot be added")

    try:
        for accreditation in accreditationsHTML:
            accreditations.append(
                accreditation.text.replace("\n", "").replace(":", ""))
    except:
        print("accreditation cannot be added")

    try:
        for treatment in treatmentsHTML:
            treatments.append(treatment.text.replace(
                "\n", "").replace(":", ""))
    except:
        print("treatment cannot be added")

    try:
        for levelOfCare in levelOfCareHTML:
            levelOfCares.append(levelOfCare.text.replace(
                "\n", "").replace(":", ""))
    except:
        print("levelOfCare cannot be added")

    try:
        for clinicalService in clinicalServicesHTML:
            clinicalServices.append(
                clinicalService.text.replace("\n", "").replace(":", ""))
    except:
        print("financial cannot be added")

    company = {
        "name": soup.find(id="hfn").get("title").replace("\n", ""),
        "type": soup.find(class_="vertical").text.replace("\n", ""),
        "rate": soup.find(id="reviews-summary").div.get("title").replace("\n", ""),
        "description": soup.find(id="header-description").text.replace("\n", ""),
        "accreditations": ",".join(accreditations),
        "treatment": ",".join(treatments),
        "programs": ",".join(programs),
        "financials": ",".join(financials),
        "levels_of_care": ",".join(levelOfCares),
        "clinical_services": ",".join(clinicalServices),
        "amenities": ",".join(amenities),
        "address": soup.find(id="contact").div.text.replace("\n", ""),
        "url": link,
        "website": soup.find(class_="text url").a.get("href").replace("\n", ""),
        "phone": soup.find(class_="phone call-rehab-trigger").get("href").replace("\n", "")
    }
    print(company)
    companies.append(company)


driver = webdriver.Chrome('./chromedriver')
for page in range(1, 3):
    driver.get("https://www.rehab.com/search?page="+str(page))
    time.sleep(3)
    images = driver.find_elements_by_class_name("image")
    for image in images:
        link = image.find_element_by_tag_name("a").get_attribute("href")
        try:
            getCompanyInfo(link)
            success = success + 1
        except Exception as e:
            print("an error ocurred")
            fail = fail + 1
            print(e)

with open('test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(companies)
    successRate = (success / (success + fail)) * 100
    print("Process completed. Success rate is: %"+str(successRate))
