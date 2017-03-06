# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import identifySimilarImage
from PIL import Image
import senceCheck
defaultSSPath = "screenshot.png"
tanSuoPath = "prePic/tanSuoRuKou.png"
tanSuoPath_10 = "prePic/tanSuo_10.png"
tanSuoPath_10_tanSuo = "prePic/tanSuo_10_tanSuo.png"
tanSuoPath_10_tanSuo_kick = "prePic/tanSuo_10_tanSuo_kick.png"

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def click_pic(self,picPathToClick):
                #点击探索
        toClick = identifySimilarImage.gen_similar_cut_pic_center_x_y(defaultSSPath,picPathToClick)
        sleep(3)
        print type(toClick["x"]),toClick["x"],toClick["y"]
        #最好点击两次探索灯笼
        self.driver.tap([(toClick["x"],toClick["y"])],duration=500)
        sleep(2)
        self.driver.tap([(toClick["x"],toClick["y"])],duration=500)
        sleep(2)
        self.shot_screen()

    def shot_screen(self):
        self.driver.get_screenshot_as_file("screenshotPre.png")

        img = Image.open("screenshotPre.png")
        img2 = img.transpose(Image.ROTATE_270)
        img2.save("screenshot.png")


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'kindle fire HD'
        desired_caps['appPackage'] = 'com.netease.onmyoji.huawei'
        desired_caps['appActivity'] = 'com.netease.onmyoji.Launcher'
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):


        self.shot_screen()
        i = 6
        while(i > 0):
            i = i-1
            self.driver.tap([(1280,1176)])
            sleep(4)
        ##这段执行完后，可以登录到庭院


        self.shot_screen()
        sleep(1)
        #电击探索
        self.click_pic(tanSuoPath)
        self. click_pic(tanSuoPath_10)
        self. click_pic(tanSuoPath_10_tanSuo)
        #打消怪
        sleep(4)
        self.shot_screen()

        self. click_pic(tanSuoPath_10_tanSuo_kick)



        sleep(4)
        self.shot_screen()

        #一下开始打探索副本了，请各单位注意了



        # i = 50
        # while(i > 0):
        #     i = i-1
        #     self.driver.tap([(92,76)])
        #     sleep(2)
        # sleep(5)
        # self.driver.tap([(92,76)])





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
