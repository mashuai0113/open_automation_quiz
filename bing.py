from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
# 操作这个对象.
driver.get('https://cn.bing.com/')     # get方式访问bing.
time.sleep(2)
#input = 'document.getElementById("sb_form_q")'
# input.send_keys('西游记')
#input.set(1111)
# sys.stdin.readline()
driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('bing')
time.sleep(2)
# input.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="sb_form_go"]').send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//*[@id="b_results"]/li[16]/nav/ul/li[2]/a').click()  #因为li的值每次一变，所以不用xpath了
#driver.find_element_by_xpath('//div[@class="b_widePag"]/a[2]').click()
driver.find_elements_by_class_name('b_widePag')[1].click()
time.sleep(5)
results = driver.find_elements_by_xpath('//*[@id="b_results"]/child::li/child::h2')
lists = []
for i in results:
    a = i.text
    lists.append(a)
    print(a)  # 打印遍历标签出来的内容和获取href属性的内容
    time.sleep(4)
#driver.back()
driver.quit() 


