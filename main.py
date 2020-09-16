from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
from selenium.webdriver.support.ui import Select



options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=chrome-data/")
# options.add_extension('extension_1_0_7_0.crx')

AdvertiserCompanyName="AIS Service Inc"
Job_title="Human Resource Manager"
Location="Algeria"
fully_remote="NO"#,NO,YES,TEMPORARILY_DUE_TO_COVID_19
AdvertiserName="Ameur B"
AdvertiserPhoneNumber="+4420255820"
advertisercampaignsource=""
country="GB"

WORK_REMOTELY



driver = webdriver.Opera(executable_path='operadriver.exe',options=options)

username='salim.nadaa@gmail.com'
password='ameur000'

url="https://indeed.com/hire"
driver.get(url)

# Login
driver.find_element_by_xpath('//*[@id="u1y63qxkeyp"]/span').click()


driver.find_element_by_xpath('//*[@id="login-email-input"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="login-password-input"]').send_keys(password)

driver.find_element_by_xpath('//*[@id="login-submit-button"]').click()





# driver.get('https://whatismyipaddress.com')
driver.find_element_by_xpath('//*[@id="hireHeroPostJobButton"]').click()

driver.find_element_by_xpath('//*[@id="JobCompanyName"]').send_keys(AdvertiserCompanyName)
driver.find_element_by_xpath('//*[@id="JobTitle"]').send_keys(Job_title)
driver.find_element_by_xpath('//*[@id="cityOrPostalCode"]').send_keys(Location)


if 'no' in fully_remote.lower(): 
    driver.find_element_by_xpath('//*[@id="label-radio-work_remotely-NO"]').click()
elif 'yes' in fully_remote.lower():
    driver.find_element_by_xpath('//*[@id="label-radio-work_remotely-YES"]').click()
elif 'temp' in fully_remote.lower():
    driver.find_element_by_xpath('//*[@id="label-radio-work_remotely-TEMPORARILY_DUE_TO_COVID_19"]').click()
    
    
driver.find_element_by_xpath('//*[@id="sheet-next-button"]/span/a').click()

#Create your job posting account

    
driver.find_element_by_xpath('//*[@id="AdvertiserCompanyName"]').send_keys(AdvertiserCompanyName)
driver.find_element_by_xpath('//*[@id="AdvertiserName"]').send_keys(AdvertiserName) 
driver.find_element_by_xpath('//*[@id="AdvertiserName"]').send_keys(advertisercampaignsource)  
driver.find_element_by_xpath('//*[@id="AdvertiserCampaignSource"]/option[8]').click()  
driver.find_element_by_xpath('//*[@id="sheet-next-button"]/span/a').click()

#Getting Started url='https://employers.indeed.com/p/post-job#post-job/getting-started'

driver.find_element_by_xpath('//*[@id="change-country-link"]/span').click()
driver.find_element_by_xpath('//*[@value="{}"]'.format(country)).click()
driver.find_element_by_xpath('//*[@id="JobTitle"]').send_keys(Job_title)

 
  
