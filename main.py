from pathlib import Path
import sys
from argparse import ArgumentParser, RawTextHelpFormatter
from tkinter import *
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, QLoggingCategory, QUrl
import sys
from browser import Browser

import shutil

try:
    file_to_copy = '.\\data\\hosts'

    destination_directory = 'C:\\Windows\\System32\\drivers\\etc'

    shutil.copy(file_to_copy, destination_directory)
except:
    print("Adblock Error!")

if __name__ == "__main__":
    parser = ArgumentParser(description="Monarch",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("--single-process", "-s", action="store_true",
                        help="Có vấn đề với phần mềm, vui lòng khởi động lại.")
    parser.add_argument("url", type=str, nargs="?", help="URL")
    args = parser.parse_args()

    QCoreApplication.setOrganizationName("Monarch")

    app_args = sys.argv
    if args.single_process:
        app_args.extend(["--webEngineArgs", "--single-process"])
    app = QApplication(app_args)
    app.setWindowIcon(QIcon(".\\data\\logo.png"))
    QLoggingCategory.setFilterRules("qt.webenginecontext.debug=true")
    s = QWebEngineProfile.defaultProfile().settings()
    s.setAttribute(QWebEngineSettings.PluginsEnabled, True)
    s.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)
    browser = Browser()
    window = browser.create_hidden_window()

    url = QUrl.fromUserInput(args.url) if args.url else QUrl("https://google.com/")
    window.tab_widget().set_url(url)
    window.show()
    sys.exit(app.exec())
