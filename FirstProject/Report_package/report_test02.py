# -*- coding: utf-8 -*-

from Repor_test01 import TestCnblogs
import HTMLTestRunner
import unittest

testreport = unittest.TestSuite()

testreport.addTest(TestCnblogs("test_cnblogs_login"))
filename = "E:workpython projectselenium_pythonreport.html"
fp = file(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"博客园测试报告",
        description=u"用例执行情况：")
runner.run(testreport)
