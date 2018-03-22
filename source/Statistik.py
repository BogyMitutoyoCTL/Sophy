from HighScoreEntry import *
import xlsxwriter


class Statistik:
    def __init__(self):
        self.entries = []
        pass

    def save_entry(self, entry: HighScoreEntry):
        self.entries.append(entry)

    def save_to_file(self):
        workbook = xlsxwriter.Workbook("../values/statistics.xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, "name")
        worksheet.write(0, 1, "speed in km/h")
        worksheet.write(0, 2, "duration")
        worksheet.write(0, 3, "distance in mm")
        worksheet.write(0, 4, "date")

        for i in range(0, len(self.entries)):
            entry = self.entries[i]  # type: HighScoreEntry
            worksheet.write(i+1, 0, entry.name)
            worksheet.write(i+1, 1, entry.speed)
            worksheet.write(i+1, 2, entry.duration)
            worksheet.write(i+1, 3, entry.distance)
            worksheet.write(i+1, 4, entry.record_date)
        workbook.close()