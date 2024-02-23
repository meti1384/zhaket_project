from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
from time import sleep
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options



options=Options()
service=Service()
driver=webdriver.Edge(service=service)
driver.implicitly_wait(20)

def open_site(url):
    try:
        driver.get(url)
        result=driver.execute_script("return document.readyState")
        if result!="complete":
            raise Exception("site is not loaded!")
    except:
        sleep(12)

    


def extract_data_form_excel(path):
    file_path = path

    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active

    data = []

    for row in worksheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    workbook.close()
    return data


def captchat_solve(url, website_key):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("c47fa5e7f23c36ab7ed95ac11bdf57af")
    solver.set_website_url(url)
    solver.set_website_key(website_key)

    g_response = solver.solve_and_return_solution()
    if g_response!= 0:
        print("g_response"+g_response)
    else:
        print("task finished with error"+solver.error_code)


    driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "<g_response>";')
    sleep(2)
    driver.execute_script(f"___grecaptcha_cfg.clients[0].N.N.callback('{g_response}');")
    sleep(5)



def login(url, website_key):
        try:
            try: 
                if driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']"):
                    captchat_solve(url, website_key)
            except:
                sleep(5)

            driver.find_element(By.CSS_SELECTOR , "input#username").send_keys("9026916035")
            driver.find_element(By.CSS_SELECTOR, "button[class^=btn]").click()
            driver.find_element(By.CSS_SELECTOR , "input#password").send_keys("meti13842006")
            driver.find_element(By.XPATH, "//button[@class='btn btn--orange btn--full' and @type='submit']").click()
            sleep(3)
            
              
        except:
            driver.quit()