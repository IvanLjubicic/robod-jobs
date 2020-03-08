from config import config
import datetime
import os.path
from os import path
from automagica import *

class FolderJobs():

    @staticmethod
    def createFolderOnPath(lawFirm, sud, upisnik, predmet, godina, datum):
        folderPath = config['robot']['base_folder_path'] + "\\" + lawFirm + "\\" + sud + "-" + upisnik + "-" + predmet + "-" + godina + "\\" + str(datum)
        if not path.exists(folderPath):
            os.makedirs(folderPath)
        return folderPath
    
    @staticmethod
    def getIssueBasePathFile(lawFirm, sud, upisnik, predmet, godina):
        return config['robot']['base_folder_path'] + "\\" + lawFirm + "\\" + sud + "-" + upisnik + "-" + predmet + "-" + godina + "\\" + config['robot']['base_issue_url_path_file']
    
    @staticmethod
    def getIssueBasePathUrl(lawFirm, sud, upisnik, predmet, godina):
        return config['robot']['base_url'] + "sud=" + sud + "&upisnik=" + upisnik + "&predmet=" + predmet + "&godina=" + godina

    def getMostRecentFolderPath(self, lawFirm, sud, upisnik, predmet, godina, datum):
        return config['robot']['base_folder_path'] + "\\" + lawFirm + "\\" + sud + "-" + upisnik + "-" + predmet + "-" + godina + "\\" + getMostRecentIssueFolder(lawFirm, sud, upisnik, predmet, godina)
    
    @staticmethod
    def getAllDirectoriesNamesInPath(lawFirm, sud, upisnik, predmet, godina):
        dirs = os.listdir(config['robot']['base_folder_path'] + "\\" + lawFirm + "\\" + sud + "-" + upisnik + "-" + predmet + "-" + godina)
        dirList = []
        # This would print all the files and directories
        for file in dirs:
            print (file)
            dirList.append(file)
        
        return dirList
    
    @staticmethod
    def getMostRecentIssueFolder(lawFirm, sud, upisnik, predmet, godina):
        dirList = FolderJobs.getAllDirectoriesNamesInPath(lawFirm, sud, upisnik, predmet, godina)

        mostRecentDate = datetime.datetime(1988, 4, 17).date()
        for directory in dirList:
            currentDate = datetime.datetime.strptime(directory, '%Y-%m-%d').date()
            print(currentDate)
            if currentDate > mostRecentDate:
                mostRecentDate = currentDate
                
        return mostRecentDate.strftime('%Y-%m-%d')

    @staticmethod
    def getMostRecentStatusFilePath(lawFirm, sud, upisnik, predmet, godina):
        folderPath = config['robot']['base_folder_path'] + "\\" + lawFirm + "\\" + sud + "-" + upisnik + "-" + predmet + "-" + godina + "\\" + FolderJobs.getMostRecentIssueFolder(lawFirm, sud, upisnik, predmet, godina) + "\\" + config['robot']['issue_status_file_name']
        print(folderPath)
        return folderPath

    @staticmethod
    def createStatusFile(folderPath):
        statusFilePath = folderPath + "\\" + config['robot']['issue_status_file_name']
        make_textfile(get_from_clipboard(), statusFilePath)
        return statusFilePath

