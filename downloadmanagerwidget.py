import ctypes
try:
    from PySide6.QtWebEngineCore import QWebEngineDownloadRequest
    from PySide6.QtWidgets import QWidget, QFileDialog
    from PySide6.QtCore import QDir, QFileInfo, Qt
    import hashlib
    from downloadwidget import DownloadWidget
    from ui_downloadmanagerwidget import Ui_DownloadManagerWidget
    import hashlib
    from PySide6.QtWidgets import (QFileDialog,
                                QWidget)
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QWidget
except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể import các thư viện của cửa sổ tải xuống, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)

try:
    class DownloadManagerWidget(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            self._ui = Ui_DownloadManagerWidget()
            self._num_downloads = 0
            self._ui.setupUi(self)

        def download_requested(self, download):
            assert (download and download.state() == QWebEngineDownloadRequest.DownloadRequested)
            proposal_dir = download.downloadDirectory()
            proposal_name = download.downloadFileName()
            proposal = QDir(proposal_dir).filePath(proposal_name)
            path, _ = QFileDialog.getSaveFileName(self, "Lưu ở", proposal)
            if not path:
                return

            fi = QFileInfo(path)
            download.setDownloadDirectory(fi.path())
            download.setDownloadFileName(fi.fileName())
            download.accept()
            self.add(DownloadWidget(download))

            self.show()

        def add(self, downloadWidget):
            downloadWidget.remove_clicked.connect(self.remove)
            self._ui.m_itemsLayout.insertWidget(0, downloadWidget, 0, Qt.AlignTop)
            if self._num_downloads == 0:
                self._ui.m_zeroItemsLabel.hide()
            self._num_downloads += 1

        def remove(self, downloadWidget):
            self._ui.m_itemsLayout.removeWidget(downloadWidget)
            downloadWidget.deleteLater()
            self._num_downloads -= 1
            if self._num_downloads == 0:
                self._ui.m_zeroItemsLabel.show()
except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể khởi chạy cửa sổ tải xuống, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)
