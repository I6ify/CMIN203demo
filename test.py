from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\isaac\Documents\CMIN203demo\geckodriver.exe")
driver.get('https://www.youtube.com/watch?v=eGkmdPCsMkE&list=PLL7USe8wzBxUFfnXNkOwliau_XZixxMBM')

print (driver.title)
print (driver.current_url)
