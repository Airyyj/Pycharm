# -*- coding: utf-8 -*-

import time
import unittest
from selenium import webdriver
class TestCnblogs(unittest.TestCase):
    def setUp(self):
        print u"自动化测试用例执行开始"
        #self.driver = webdriver.Firefox(executable_path="D:/ProgramFiles/Firefox/firefox.exe")
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        # 智能等待3S
        self.Errors = []
        # 错误信息列表

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.Errors)
        # 检查错误信息列表 若不为空则返回显示
        print u"自动化测试用例执行结束"
    def test_cnblogs_login(self):
        u"""博客园登录"""
        driver = self.driver
        driver.get("http://www.cnblogs.com/")
        # 测试地址 后面可以添加响应地址
        driver.find_element_by_css_selector("a[onclick = 'login();return false']").click()
        driver.find_element_by_css_selector("input[type = 'text']").clear()
        driver.find_element_by_css_selector("input[type = 'text']").send_keys(u"Skyyj")
        # 这里用户名由于是中文前面要加 u
        driver.find_element_by_css_selector("input[type = 'password']").clear()
        driver.find_element_by_css_selector("input[type = 'password']").send_keys("CHINA927_skyyj")
        # 输入密码、密码当然按照实际内容添加
        driver.find_element_by_css_selector("input[type = 'submit']").click()
        time.sleep(2)
        driver.close()


if __name__ == "__main__":
    unittest.main()