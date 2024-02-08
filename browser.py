import ctypes
try:
    from PySide6.QtWebEngineCore import (qWebEngineChromiumVersion,
                                        QWebEngineProfile, QWebEngineSettings)
    from PySide6.QtCore import QObject, Qt, Slot

    from downloadmanagerwidget import DownloadManagerWidget
    from browserwindow import BrowserWindow
except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể import các thư viện lõi trình duyệt, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)

try:
    class Browser(QObject):

        def __init__(self, parent=None):
            super().__init__(parent)
            self._windows = []
            self._download_manager_widget = DownloadManagerWidget()
            self._profile = None
            self._download_manager_widget.setAttribute(Qt.WA_QuitOnClose, False)

            dp = QWebEngineProfile.defaultProfile()
            dp.downloadRequested.connect(self._download_manager_widget.download_requested)

        def create_hidden_window(self, offTheRecord=False):
            if not offTheRecord and not self._profile:
                name = "Monarch." + qWebEngineChromiumVersion()
                self._profile = QWebEngineProfile(name)
                s = self._profile.settings()
                s.setAttribute(QWebEngineSettings.PluginsEnabled, True)
                s.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)
                s.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
                s.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, False)
                self._profile.downloadRequested.connect(self._download_manager_widget.download_requested)

            profile = QWebEngineProfile.defaultProfile() if offTheRecord else self._profile
            main_window = BrowserWindow(self, profile, False)
            self._windows.append(main_window)
            main_window.about_to_close.connect(self._remove_window)
            return main_window

        def create_window(self, offTheRecord=False):
            main_window = self.create_hidden_window(offTheRecord)
            main_window.show()
            return main_window

        def create_dev_tools_window(self):
            profile = (self._profile if self._profile
                    else QWebEngineProfile.defaultProfile())
            main_window = BrowserWindow(self, profile, True)
            self._windows.append(main_window)
            main_window.about_to_close.connect(self._remove_window)
            main_window.show()
            return main_window

        def windows(self):
            return self._windows

        def download_manager_widget(self):
            return self._download_manager_widget

        @Slot()
        def _remove_window(self):
            w = self.sender()
            if w in self._windows:
                del self._windows[self._windows.index(w)]

except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể khởi chạy lõi của trình duyệt, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)
