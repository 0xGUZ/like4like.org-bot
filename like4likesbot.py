from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AMFBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    
    def open(self):
        bot = self.bot
        bot.get("https://www.like4like.org/login/")
        usuario = bot.find_element_by_name("username")
        senha = bot.find_element_by_name("password")
        usuario.clear()
        senha.clear()
        usuario.send_keys(self.username)
        senha.send_keys(self.password)
        bot.find_element_by_class_name('form-button').click()
        time.sleep(5)
        ed.twtlk()
    
    def twtlk(self):
        bot = self.bot
        bot.get("https://www.like4like.org/free-twitter-followers.php")
        time.sleep(5)
        bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']").click()
        bot.switch_to_window(bot.window_handles[1])
        #window
        try:
            usuario = bot.find_element_by_id("username_or_email")
            if usuario.is_displayed():
                senha = bot.find_element_by_id("password")
                usuario.clear()
                senha.clear()
                usuario.send_keys("gus232321")
                senha.send_keys("12345qwert")
                bot.find_element_by_name('commit').click()
                follow = bot.find_element_by_xpath('//*[@id="follow_btn_form"]/button')
                if follow.is_displayed():
                    follow.click()
                time.sleep(5)
            else:
                follow = bot.find_element_by_xpath('//*[@id="follow_btn_form"]/button')
                if follow.is_displayed():
                    follow.click()
                time.sleep(5)

        except bot.NoSuchElementException:
            bot.close()
            bot.switch_to_window(bot.window_handles[0])
            time.sleep(5)
            bot.get("https://www.like4like.org/free-twitter-followers.php")
            ed.twttwo()
        
        #window
        bot.close()
        bot.switch_to_window(bot.window_handles[0])
        time.sleep(5)
        ed.twttwo()
    
    def twttwo(self):
        bot = self.bot
        bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']").click()
        bot.switch_to_window(bot.window_handles[1])
        #window

        usuario = bot.find_element_by_id("username_or_email")
        if usuario.is_displayed():
            senha = bot.find_element_by_id("password")
            usuario.clear()
            senha.clear()
            usuario.send_keys("your_username")
            senha.send_keys("your_password")
            bot.find_element_by_name('commit').click()
            bot.find_element_by_xpath('//*[@id="follow_btn_form"]/button').click()
            time.sleep(5)
        else:
            bot.find_element_by_xpath('//*[@id="follow_btn_form"]/button').click()
            time.sleep(5)

        #window
        bot.close()
        bot.switch_to_window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()


ed = AMFBot('your_user', 'your_password')
ed.open()