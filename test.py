from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DRIVER_PATH = './chromedriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://esad.targetiv.work/new-member-registration/')
import pandas as pd


df = pd.read_excel('esad_member_list_formated.xlsx', usecols='B:F')
df_to_list = df.values.tolist()
# print(df_to_list)

for id in df_to_list:
    # Full Name
    driver.find_element(By.ID, "wpf_input_494_customer_name").send_keys(id[0])

    # Phone number
    driver.find_element(By.ID, "phone_code_wpf_input_494_phone_input").send_keys(id[3])

    # Email
    driver.find_element(By.ID, "wpf_input_494_customer_email").send_keys(id[4])

    # SSC
    driver.find_element(By.ID, "wpf_input_494_number_3").send_keys(id[1])

    # HSC
    driver.find_element(By.ID, "wpf_input_494_number_2").send_keys(id[2])

    # 1st terms & condition
    driver.find_element(By.ID, "terms_conditions_494").click()

    # 2nd terms & condition
    driver.find_element(By.ID, "terms_conditions_1_494").click()

    # Pay Button
    driver.find_element(By.ID, "stripe_form_submit_494").click()
