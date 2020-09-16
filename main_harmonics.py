from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
from selenium.webdriver.support.ui import Select
import configparser
import uvicorn
script =''' (function() {
        
        	
            WebSocket.prototype._send = WebSocket.prototype.send;
            WebSocket.prototype.send = function(data) {
                this._send(data);
                this.addEventListener('message', function(msg) {
        			
                
                let name1 = get_symbol_name()
        			
                  let data = {name: name1,payload:msg.data};
        
                  fetch("http://127.0.0.1:8000/get_data", {
                    method: "POST", 
                    body: JSON.stringify(data)
                  });
        
              
        
                    console.log('>> ' + msg.data);
                }, false);
                this.send = function(data) {
                    this._send(data);
                    console.log("<< " + data);
                };
            }
        })();'''



config = configparser.ConfigParser()
config.read('config.ini')
username=config['CONFIG']['Username']
password=config['CONFIG']['Password']
broker=int(config['CONFIG']['broker'])
timeframe=int(config['CONFIG']['timeframe'])
ts=int(config['CONFIG']['ts'])




def generate_tabs(driver):
        i=1
        while True:
            # for i in range(1,14):
            try:
                driver.execute_script("window.open('https://harmonics.im/');")
                time.sleep(ts)    
        
                driver.switch_to.window(driver.window_handles[i])
                time.sleep(2*ts)   
                driver.find_element_by_xpath('//*[@id="timeframes"]/div[{}]/a'.format(timeframe)).click()
                time.sleep(2*ts)
                driver.find_element_by_xpath('//*[@id="rightMenu"]/div[2]/button').click()
                time.sleep(2*ts)
                driver.find_element_by_xpath('//*[@id="rightMenu"]/div[2]/div/div/ul/li[{}]'.format(broker)).click()
                time.sleep(2*ts)
                driver.find_element_by_xpath('//*[@id="symbols"]/tbody/tr[{}]'.format(i)).click()
                time.sleep(2*ts)
                driver.execute_script(script)
                i=i+1
            except Exception as e:
                print(e)
                break
        return driver
    
def refresh_tabs(driver):
        i=1
        while True:
            # for i in range(1,14):
            try:  
                driver.switch_to.window(driver.window_handles[i])
                time.sleep(2*ts)   
                driver.find_element_by_xpath('//*[@id="timeframes"]/div[{}]/a'.format(timeframe)).click()
                time.sleep(2*ts)
                driver.find_element_by_xpath('//*[@id="rightMenu"]/div[2]/button').click()
                time.sleep(2*ts)
                driver.find_element_by_xpath('//*[@id="rightMenu"]/div[2]/div/div/ul/li[{}]'.format(broker)).click()
                time.sleep(2*ts)
                driver.find_element_by_xpath('//*[@id="symbols"]/tbody/tr[{}]'.format(i)).click()
                time.sleep(2*ts)
                driver.execute_script(script)
                i=i+1
            except Exception as e:
                print(e)
                break
        return driver    

def get_session():

        
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=chrome-data/")
        options.add_extension('extension_1_0_7_0.crx')
        
        
        driver = webdriver.Opera(executable_path='chromedriver.exe',options=options)
        
        # username='israelramirez1001'
        # password='Qwerty1!'
        url="https://harmonics.im/"
        driver.get(url)
        stat=True
        j=0
        print('logging in the server................')
        while stat :
            try:
                driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
                driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
                driver.find_element_by_xpath('//button[@type="submit"]').click()
            
            except:
                stat=False
            time.sleep(20)
            try:
                driver.find_element_by_xpath('//input[@name="username"]')
                stat=True
                j=j+1
                time.sleep(300)
        
            except:
                stat=False
            if j==2:
                stat=False
    
        
        # driver.find_element_by_xpath('//*[@id="rightMenu"]/div[2]/button').click()
        # driver.find_element_by_xpath('//*[@id="rightMenu"]/div[2]/div/div/ul/li[1]').click()
        
        
        # driver.find_element_by_xpath('//*[@id="symbols"]/tbody/tr[1]').click()
        print('open channels ................')
        
        driver=generate_tabs(driver)
        return driver
    
        



driver=get_session()
while True :
    

    driver=refresh_tabs(driver)
    print('refrech status of channels ........................')
    time.sleep(300)   

    