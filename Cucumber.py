from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import ImageGrab
import tkinter


import HTMLTestRunner

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)# 操作这个对象.
driver.get('https://templates.jinshuju.net/detail/Dv9JPD')     # get方式访问bing.
time.sleep(2)
iframe = driver.find_elements_by_xpath('//*[@id="__next"]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/iframe')[0]
driver.switch_to.frame(iframe)
driver.find_elements_by_xpath('//*[@id="new_entry"]/div[2]/div/div[4]/div[1]/div[2]/div/div[2]/div/label[2]/div/div[1]/i')[0].click()
time.sleep(2)
img = ImageGrab.grab(bbox=(0, 0, 1024, 1024))
img.save('D:\MSwork\python\p1.jpg')
driver.find_element_by_xpath('//*[@id="new_entry"]/div[2]/div/div[5]/a[2]').click()
time.sleep(2)
driver.switch_to.default_content()


driver.switch_to.frame(iframe)
driver.find_element_by_id('entry_field_18').send_keys("2020/3/12") #首先需要点击日期输入框
driver.find_element_by_id('entry_field_19').send_keys("自动化")
driver.find_element_by_id('entry_field_20').send_keys("13888888888")
time.sleep(3)
img = ImageGrab.grab(bbox=(0, 0, 1024, 1024))
img.save('D:\MSwork\python\p2.jpg')
driver.find_element_by_xpath('//*[@id="new_entry"]/div[2]/div/div[5]/a[2]').click()
time.sleep(2)
driver.switch_to.default_content()

driver.switch_to.frame(iframe)
driver.find_element_by_id('entry_field_23').send_keys("测试公司") #报备单位测试公司
driver.find_element_by_id('entry_field_24').send_keys("99")#在岗人数99
driver.find_element_by_id('entry_field_25').send_keys("2020/3/12")#报备日期今天
driver.find_element_by_id('entry_field_26').send_keys("0") #湖北籍员工、前往湖北以及与湖北人员密切接触的员工（人数）	0
driver.find_element_by_id('entry_field_27').send_keys("CEO")#单位负责人 CEO
driver.find_element_by_id('entry_field_28').send_keys("13888888888")#联系方式 13888888888
driver.find_element_by_id('entry_field_29').send_keys("测试内容")#疫情防控方案	 测试内容
time.sleep(3)
img = ImageGrab.grab(bbox=(0, 0, 1024, 1024))
img.save('D:\MSwork\python\p3.jpg')
driver.find_element_by_xpath('//*[@id="new_entry"]/div[2]/div/div[5]/input[1]').click()
time.sleep(2)
driver.switch_to.default_content()
driver.quit() 

dir = "D:/MSwork/python/test.html"    #定义测试报告文件
filename = open(dir,"wb")     #"wb"新建或者打开一个二进制文件，写入执行完的数据
runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title="Testcase Report",description=u"测试用例明细")    
#调用HTMLTestRunner类定义测试报告内容
runner.run(suit)    #调用HTMLTestRunner类下面的run()方法运行用例套件
filename.close()    #关闭测试报告文件

