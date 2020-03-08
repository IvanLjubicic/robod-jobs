class AnalysisJobs():

    @staticmethod
    def checkStatusFiles(firstFilePath, secondFilePath):
        issueChecker = False
        with open(firstFilePath,'r', encoding="utf8") as f:
            d=set(f.readlines())

        with open(secondFilePath,'r', encoding="utf8") as f:
            e=set(f.readlines())

        for line in list(d-e):
            issueChecker = True
