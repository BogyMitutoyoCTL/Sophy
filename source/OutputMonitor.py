

class HtmlOutput:
    def __init__(self, listOfNames):
        self.listOfNames = listOfNames

    def GetHtmlBegin(self):
        return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="30"><title>Title</title><link rel="stylesheet" type="text/css" href="OutputRankCss.css"></head><body><h1>Best of The Best</h1><ol>'

    def GetHtmlEnd(self):
        return '</ol></body></html>'

    def GetHtmlNames(self):
        output = ""
        for name in self.listOfNames:
            output = output + '<li>' + name + '</li>'
        return output

    def GetHtml(self):
        output = self.GetHtmlBegin()
        output = output + self.GetHtmlNames()
        output = output + self.GetHtmlEnd()
        return output


names = ["Dimitri", "Jane", "Paul", "Test"]
print(HtmlOutput(names).GetHtml())
with open('OutputTime2.html', 'w') as file:
    file.write(HtmlOutput(names).GetHtml())