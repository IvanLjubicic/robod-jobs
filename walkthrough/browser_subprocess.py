import subprocess
from automagica import *

class BrowserJobs():

    @staticmethod
    def open_browser():
        subprocess.call('start firefox', shell=True)
        
    @staticmethod
    def close_browser():
        press_key_combination('alt','f4')
    
    @staticmethod
    def enter_link(link):
        set_to_clipboard(link)
        wait(seconds=1)
        press_key_combination('ctrl','v')
        wait(seconds=1)
        press_key('enter')
    
    @staticmethod
    def override_captcha():
        wait(seconds=2)
        #check mark
        click(x=685, y=667)
        wait(seconds=2)
        #buster click
        click(x=914, y=963)
        wait(seconds=6)
        press_key('enter')
        wait(seconds=2)
        #check mark
        click(x=685, y=667)
        wait(seconds=2)
        #buster click
        click(x=914, y=963)
        wait(seconds=6)
        #search
        click(x=672, y=787)
        wait(seconds=2)
        #print
        click(x=1586, y=474)

    @staticmethod
    def check_issue(issueBasePath, todaysFolderPath):
        wait(seconds=3)
        open_file(path=issueBasePath)
        wait(seconds=3)
        press_key_combination('win','4')
        press_key_combination('win','5')
        press_key_combination('ctrl','a')
        wait(seconds=2)
        press_key_combination('ctrl','c')
        wait(seconds=2)
        press_key_combination('alt','space','c')
        press_key_combination('ctrl','l')
        wait(seconds=2)
        press_key_combination('ctrl','v')
        press_key('enter')
        wait(seconds=2)
        click(x=685, y=667)
        #check mark
        wait(seconds=2)
        click(x=914, y=963)
        #buster click
        wait(seconds=6)
        press_key('enter')
        wait(seconds=2)
        click(x=685, y=667)
    
    @staticmethod
    def copyContent():
        wait(seconds=2)
        press_key_combination('ctrl','a')
        press_key_combination('ctrl','c')
    
    @staticmethod
    def close_browser():
        wait(seconds=2)
        press_key_combination('alt','f4')
