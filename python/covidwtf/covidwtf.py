import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from prometheus_client import (
    start_http_server,
    Gauge,
    Info,
    Counter
)
import threading


URL = os.getenv("URL", "https://www.who.int/home")
METRICS = {}
METRICS["info"] = Info("covid_what_the_f", "Version: 0.1")
TARGETS = ["confirmed_cases", "confirmed_deaths"]
HTTP_PORT = int(os.getenv("HTTP_PORT", "9999"))

def get_cases_int(text):
    result = False
    try:
        result = int(text.replace(" ", ""))
    except:
        result = False
    return result

def get_who_covid_cases():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors=yes")
    driver = webdriver.Chrome(options=options)

    driver.get(URL)
    
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/section/div[2]/div/div[1]/article/main/div/a')
        )
    )
    element.click()
    
    confirmed_cases_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.ID, 'confirmedCases')))
    confirmed_deaths_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.ID, 'confirmedDeaths')))

    
    confirmed_cases = get_cases_int(confirmed_cases_element.text)
    confirmed_deaths = get_cases_int(confirmed_deaths_element.text)

    print(f"Confirmed cases: {confirmed_cases}, deaths: {confirmed_deaths}")
    driver.save_screenshot("/home/epictet/ny/1.png")
    driver.quit()
    return {"confirmed_cases": confirmed_cases, "confirmed_deaths": confirmed_deaths}
    

def add_prometheus_metric(name):
    METRICS[name] = Gauge(name, name)
    METRICS[f"{name}_counter"] = Counter(f"{name}_counter", name)

def schedule_task():
    result = get_who_covid_cases()
    for target in TARGETS:
        METRICS[target].set(result.get(target))
        METRICS[f"{target}_counter"].inc()
    threading.Timer(10, schedule_task).start()

if __name__ == '__main__':
    
    for target in TARGETS:
        add_prometheus_metric(name=target)
    schedule_task()
    start_http_server(HTTP_PORT)