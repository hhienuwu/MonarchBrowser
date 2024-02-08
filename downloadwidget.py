import ctypes
try:
    from pathlib import Path
    from ui_downloadwidget import Ui_DownloadWidget

    from PySide6.QtWebEngineCore import QWebEngineDownloadRequest
    from PySide6.QtWidgets import QFrame, QWidget
    from PySide6.QtGui import QIcon
    from PySide6.QtCore import QElapsedTimer, Signal, Slot
except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể import các thư viện của cửa sổ tải xuống, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)

try:
    def with_unit(bytes):
        if bytes < (1 << 10):
            return f"{bytes} Byte(s)"
        if bytes < (1 << 20):
            s = bytes / (1 << 10)
            return f"{int(s)} KB"
        if bytes < (1 << 30):
            s = bytes / (1 << 20)
            return f"{int(s)} MB"
        s = bytes / (1 << 30)
        return f"{int(s)} GB"


    class DownloadWidget(QFrame):
        remove_clicked = Signal(QWidget)

        def __init__(self, download, parent=None):
            super().__init__(parent)
            self._download = download
            self._time_added = QElapsedTimer()
            self._time_added.start()
            self._cancel_icon = QIcon(".\\data\\stop.png")
            self._remove_icon = QIcon(".\\data\\clear.png")

            self._ui = Ui_DownloadWidget()
            self._ui.setupUi(self)
            self._ui.m_dstName.setText(self._download.downloadFileName())
            self._ui.m_srcUrl.setText(self._download.url().toDisplayString())

            self._ui.m_cancelButton.clicked.connect(self._canceled)

            self._download.totalBytesChanged.connect(self.update_widget)
            self._download.receivedBytesChanged.connect(self.update_widget)

            self._download.stateChanged.connect(self.update_widget)

            self.update_widget()

        @Slot()
        def _canceled(self):
            state = self._download.state()
            if state == QWebEngineDownloadRequest.DownloadInProgress:
                self._download.cancel()
            else:
                self.remove_clicked.emit(self)

        def update_widget(self):
            total_bytes_v = self._download.totalBytes()
            total_bytes = with_unit(total_bytes_v)
            received_bytes_v = self._download.receivedBytes()
            received_bytes = with_unit(received_bytes_v)
            elapsed = self._time_added.elapsed()
            bytes_per_second_v = received_bytes_v / elapsed * 1000 if elapsed else 0
            bytes_per_second = with_unit(bytes_per_second_v)

            state = self._download.state()

            progress_bar = self._ui.m_progressBar
            if state == QWebEngineDownloadRequest.DownloadInProgress:
                if total_bytes_v > 0:
                    progress = round(100 * received_bytes_v / total_bytes_v)
                    progress_bar.setValue(progress)
                    progress_bar.setDisabled(False)
                    fmt = f"%p% - {received_bytes} trên {total_bytes} đã tải - {bytes_per_second}/s"
                    progress_bar.setFormat(fmt)
                else:
                    progress_bar.setValue(0)
                    progress_bar.setDisabled(False)
                    fmt = f"Kích thước không xác định - {received_bytes} đã tải - {bytes_per_second}/s"
                    progress_bar.setFormat(fmt)
            elif state == QWebEngineDownloadRequest.DownloadCompleted:
                progress_bar.setValue(100)
                progress_bar.setDisabled(True)
                fmt = f"Hoàn thành - {received_bytes} đã tải - {bytes_per_second}/s"
                progress_bar.setFormat(fmt)
            elif state == QWebEngineDownloadRequest.DownloadCancelled:
                progress_bar.setValue(0)
                progress_bar.setDisabled(True)
                fmt = f"Đã hủy - {received_bytes} đã tải - {bytes_per_second}/s"
                progress_bar.setFormat(fmt)
            elif state == QWebEngineDownloadRequest.DownloadInterrupted:
                progress_bar.setValue(0)
                progress_bar.setDisabled(True)
                fmt = "Bị gián đoạn: " + self._download.interruptReasonString()
                progress_bar.setFormat(fmt)

            if state == QWebEngineDownloadRequest.DownloadInProgress:
                self._ui.m_cancelButton.setIcon(self._cancel_icon)
                self._ui.m_cancelButton.setToolTip("Dừng download")
            else:
                self._ui.m_cancelButton.setIcon(self._remove_icon)
                self._ui.m_cancelButton.setToolTip("Xóa khỏi danh sách")
except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể khởi chạy cửa sổ tải xuống, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)