from database.models import LawFirm
from datetime import date
from .folder_subprocess import FolderJobs
from .browser_subprocess import BrowserJobs
from .robot_subprocess import RobotJobs
from .analysis_subprocess import AnalysisJobs

class MainJobs():

    @staticmethod
    def run():
        results = LawFirm.objects.all()
        for item in results:
            for issue in item.issues:
                mostRecentStatusFilePath = FolderJobs.getMostRecentStatusFilePath(item.name, issue.sud, issue.upisnik, issue.predmet, issue.godina)
                todayFolderPath = FolderJobs.createFolderOnPath(item.name, issue.sud, issue.upisnik, issue.predmet, issue.godina, date.today())
                url = FolderJobs.getIssueBasePathUrl(item.name, issue.sud, issue.upisnik, issue.predmet, issue.godina)
                BrowserJobs.open_browser()
                BrowserJobs.enter_link(url)
                BrowserJobs.override_captcha()
                BrowserJobs.copyContent()
                BrowserJobs.close_browser()
                todayStatusFilePath = FolderJobs.createStatusFile(todayFolderPath)
                AnalysisJobs.checkStatusFiles(mostRecentStatusFilePath, todayStatusFilePath)