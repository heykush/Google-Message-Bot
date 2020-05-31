from selenium import webdriver
from time import sleep
import platform
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument(" --incognito --start-maximized –-disable-notifications ")
                                       
if platform.system() == "Linux":                                # get the driver for individual browser
    driver = webdriver.Chrome('/usr/bin/chromedriver')
elif platform.system() == "Windows":
    driver = webdriver.Chrome(r"C:\Python\chromedriver.exe", options=options)
else:
    exit("404: Only Linux and Windows is supported")
                        
driver.get('https://messages.google.com/web/authentication')

def multi():
    input('Enter anything after scanning QR code..  Hit ENTER to start')

    names = []  
    na=input("Enter your Friend's name: ")
    cap=na.title()                                      
    names.extend(cap.split(","))                         
    msg = str(input("Enter your message: "))
    count = int(input("How many times: "))

    for name in names:
        driver.find_element_by_xpath(f'//*[contains(text(), "{name}")]').click()

    sleep(2)
    msg_box = driver.find_element_by_xpath('//textarea')

    for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath('(//span[@class="mat-button-wrapper"])[42]').click()


if __name__ == "__main__":        #loop for true value of sucess 
        while True:
            print("\n================= G O O G L E  M E S S A G E ===================\n")
            print("                      By Gaurav Kushwaha                     \n")

            print("Press 1 for sending multiple messages  \nPress 2 to exit")

            n = int(input())
            if n == 1:
                multi()
            elif n == 2:
                quit()
            else:
                print("Wrong Input. Try Again ")