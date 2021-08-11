from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
from PIL import Image
from os import system

def show_image():
    system("feh canvas.png &")
    qr_scan = input("did you scan the qr code? Y/N: ")
    if qr_scan == "Y" or "y" or "yes" or "Yes" or "YES":
        system("pkill feh &")
        system("rm -f canvas.png")
    else:
        system("pkill feh &")
        system("rm -f canvas.png")
        quit()
        return 1
    


driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com")

element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, "b77wc"))
    )

canvas = driver.find_element_by_css_selector("canvas")
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

canvas_png = base64.b64decode(canvas_base64)

with open(r"canvas.png", 'wb') as f:
    f.write(canvas_png)

show_image()
WebDriverWait(driver,120).until(EC.presence_of_element_located((By.CLASS_NAME, "_3Qnsr")))
chat_select = input("Who Would you like to chat with: ")
driver.find_element_by_xpath(" //*[ contains (text(), '" + chat_select + "' )]").click()

message_bar = driver.find_element_by_xpath(" //*[ contains (text(), 'Type a message')]")
message_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')

def message_send(ctx, args):
    #message_bar.click()
    message_bar.send_keys(args)

message_input_text = input("Test Message Send: ")
message_send("", message_input_text)



