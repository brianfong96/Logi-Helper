from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def CreateDriver(extra_arguments = ["--start-maximized"]):
    arguments = ['--ignore-certificate-errors', '--incognito']
    arguments += extra_arguments
    arguments.append('headless')
        

    #Use selenium and open webdriver
    options = webdriver.ChromeOptions()
    for arg in arguments:
        options.add_argument(arg)    

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

def SetupDriver():
    driver = CreateDriver()
    if driver:
        driver.quit()
    return

enter_key = Keys.ENTER

if __name__ == "__main__":
    driver = CreateDriver()
    
    pass