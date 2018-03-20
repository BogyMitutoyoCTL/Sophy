from subprocess import Popen
from pathlib import Path


class HtmlDisplay:
    """
    HtmlDisplay: writes HTML into a temporary file on disk, then starts a web browser to display it.
    When displaying another website using the same object, the previous website is closed (web browser
    process is killed).
    Do not forget to call the close() method before exiting the program, to make sure that the web
    browser is closed before your program ends.
    """
    def __init__(self):
        self.previous_process = None

    def show_html(self, html: str) -> None:
        """
        Writes the HTML content into a temporary file,
        then opens a web browser to display that temporary file.
        :param html: HTML content as text (not a file name)
        :return: None
        """
        filename = self.__write_temp_html_file(html)
        self.__kill_previous_browser()
        self.__open_browser(filename)

    def close(self) -> None:
        """
        Closes the remaining web browser (if any).
        :return: None
        """
        self.__kill_previous_browser()

    def __open_browser(self, filename: str) -> None:
        browser = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        self.previous_process = Popen([browser, filename])
        print(self.previous_process)

    def __kill_previous_browser(self):
        if self.previous_process is not None:
            self.previous_process.kill()

    def __write_temp_html_file(self, html: str) -> str:
        filename = "{}/temp.html".format(str(Path.home()))
        print(filename)
        with open(filename, "w+") as file:
            file.write(html)
        return filename
