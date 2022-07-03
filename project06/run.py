import unittest
from unittestreport import TestRunner
from common.handle_path import CASES_DIR, REPORT_DIR
from unittestreport.core.sendEmail import SendEmail


def run():
    suite = unittest.defaultTestLoader.discover(CASES_DIR)

    runner = TestRunner(suite, filename="py666.html",
                        report_dir=REPORT_DIR, )

    runner.run()
    # 发送邮件
    # runner.send_email(host='smtp.qq.com',
    #                   port=465,
    #                   user='1406615758@qq.com',
    #                   password='belrrxyxaglgbafb',
    #                   to_addrs='1156885305@qq.com',
    #                   is_file=True)

    # ------------------------自定义邮件内容------------------------
    # em = SendEmail(host='smtp.qq.com',
    #                port=465,
    #                user='1406615758@qq.com',
    #                password='belrrxyxaglgbafb')
    #
    # em.send_email(subject="测试报告",
    #               content='666',
    #               filename='666',
    #               to_addrs='666')
    # ----------------------------发送钉钉----------------------------------
    # runner.dingtalk_notice()


if __name__ == '__main__':
    run()
