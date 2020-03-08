from automagica import *

class RobotJobs():

    @staticmethod
    def check_issue2():
        wait(seconds=2)
        click(x=914, y=963)
        #buster click
        wait(seconds=6)
        press_key('enter')
        wait(seconds=2)
        click(x=685, y=667)
        #check mark
        wait(seconds=2)
        click(x=914, y=963)
        #buster click
        wait(seconds=6)
        click(x=672, y=787)
        #search
        wait(seconds=2)
        click(x=1586, y=474)
        #print
        wait(seconds=2)
        press_key_combination('ctrl','a')
        wait(seconds=2)
        press_key_combination('ctrl','c')
        wait(seconds=2)
        print( get_from_clipboard() )

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
        #check mark
        wait(seconds=2)
        click(x=914, y=963)
        #buster click
        wait(seconds=6)
        click(x=672, y=787)
        #search
        wait(seconds=2)
        click(x=1586, y=474)
        #print
        wait(seconds=2)
        press_key_combination('ctrl','a')
        wait(seconds=2)
        press_key_combination('ctrl','c')
        wait(seconds=2)
        write_current_state_to_folder(todaysFolderPath)

    @staticmethod
    def write_current_state_to_folder(folderPath):
        statusFolderPath = folderPath+"\\status.txt"
        open(statusFolderPath, "w")
        open_file(path=statusFolderPath)
        wait(seconds=2)
        press_key_combination('ctrl','v')
        press_key_combination('alt','space','c')
        press_key('s')
        press_key('enter')
        wait(seconds=2)        
