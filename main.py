from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from setting import open_site, driver,  extract_data_form_excel,login



path_file=r"C:\Users\mahdi\Downloads\Telegram Desktop\updater (2).xlsx"
main_data=extract_data_form_excel(path_file)


website_key="6Ldfg4koAAAAABKRQfve_GSGoPGJadjdKTnakeeD"


def open_url(data):
    for (url, version, statuse, path, name) in data:
        open_site(url)
        login(url,website_key)
        sleep(5)


open_url(main_data)


