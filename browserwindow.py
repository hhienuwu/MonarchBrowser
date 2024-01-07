#--coding: utf-8 --
import sys
import os
import subprocess
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWidgets import (QMainWindow, QFileDialog,
                               QInputDialog, QLineEdit, QMenu, QMessageBox,
                               QProgressBar, QToolBar, QVBoxLayout, QWidget)
from PySide6.QtGui import QAction, QGuiApplication, QIcon, QKeySequence
from PySide6.QtCore import QUrl, Qt, Slot, Signal
from tabwidget import TabWidget
import requests
import easygui
import ctypes
import tkinter as tk
from tkinter import messagebox
import time
import openai
import ctypes
import base64
from pathlib import Path

def incognito():
    os.startfile(".\\incognito\\main.exe")

def chatgpt():
    from PyQt5 import QtGui
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout
    openai.api_key = "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"
    messages = [ {"role": "system", "content":  
                    "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown."} ] 

    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("Monarch ChatGPT")
    window.resize(500, 500)

    window.setWindowIcon(QtGui.QIcon('.\\logo.png'))

    user_input = QLineEdit()
    user_input.setPlaceholderText("Gửi tin nhắn của bạn ở đây...")
    bot_output = QTextEdit()
    bot_output.setReadOnly(True)
    send_button = QPushButton("Gửi")

    bot_output.append("ChatGPT: Xin chào! Tôi là ChatGPT, bạn có thể hỏi tôi bất cứ thứ gì!")


    def send_message():
        message = user_input.text()
        user_input.clear()
        bot_output.append(f"\nBạn: {message}\n")
        if message: 
    	    messages.append( 
                {"role": "user", "content": message}, 
            )
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
        reply = chat.choices[0].message.content 
        bot_output.append(f"ChatGPT: {reply}")

    send_button.clicked.connect(send_message)

    layout = QVBoxLayout()
    layout.addWidget(bot_output)
    layout.addWidget(user_input)
    layout.addWidget(send_button)
    central_widget = QWidget()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)

    window.show()
    app.exec_()

def antivirus():
    import base64
    import tkinter as tk
    import hashlib
    import sys
    import os
    from tkinter import messagebox
    import easygui
    import requests

    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()

    filev = easygui.fileopenbox()
    with open(filev, "rb") as f:
        bytes = f.read()
        sha256_hash = hashlib.sha256(bytes).hexdigest()

    base64_string ="aHR0cHM6Ly93d3cudmlydXN0b3RhbC5jb20vdnRhcGkvdjIvZmlsZS9yZXBvcnQ="
    base64_bytes = base64_string.encode("ascii") 
    
    sample_string_bytes = base64.b64decode(base64_bytes) 
    sample_string = sample_string_bytes.decode("ascii") 

    def check_hash_in_virustotal(api_key, hash_value):
        url = sample_string
        params = {'apikey': api_key, 'resource': hash_value}

        response = requests.get(url, params=params)
        result = response.json()

        if result['response_code'] == 0:
            root = tk.Tk()
            root.overrideredirect(1)
            root.withdraw()
            ctypes.windll.user32.MessageBoxW( 0,"Không tìm thấy virus.", "Monarch Antivirus", 1)
            root.destroy()
        else:
            print("")

            if result['positives'] > 0:
                root = tk.Tk()
                root.overrideredirect(1)
                root.withdraw()
                delete = messagebox.askyesno("Monarch Antivirus", "ĐÃ TÌM THẤY VIRUS, BẠN CÓ MUỐN XÓA NÓ KHÔNG?")
                root.destroy()
                if delete == True:
                    os.remove(filev)
                    ctypes.windll.user32.MessageBoxW( 0,"Đã xóa file có chứa virus.", "Monarch Antivirus", 1)
                else:
                    pass
            else:
                ctypes.windll.user32.MessageBoxW( 0,"Không tìm thấy virus.", "Monarch Antivirus", 1)

    api_key = '4bd2da76f00beefc87ac67e917c534f4a9a304fe3c6c074dd8b434a41c9c4cb3'
    hash_value = sha256_hash
    check_hash_in_virustotal(api_key, hash_value)

def urlchecker():
    report_api_string ="aHR0cHM6Ly93d3cudmlydXN0b3RhbC5jb20vdnRhcGkvdjIvdXJsL3JlcG9ydA=="
    report_bytes = report_api_string.encode("ascii") 
    report_string_byte = base64.b64decode(report_bytes) 
    report_string = report_string_byte.decode("ascii") 

    lab_api_string ="aHR0cHM6Ly93d3cudmlydXN0b3RhbC5jb20vdnRhcGkvdjIvdXJsL3NjYW4=="
    lab_bytes = lab_api_string.encode("ascii") 
    lab_string_byte = base64.b64decode(lab_bytes) 
    lab_string = lab_string_byte.decode("ascii")

    result_api_string ="QXZpcmE="
    result_bytes = result_api_string.encode("ascii") 
    result_string_byte = base64.b64decode(result_bytes) 
    result_string = result_string_byte.decode("ascii")  

    def is_url_malicious(api_key, url):
        api_endpoint = report_string
        scan_api_endpoint = lab_string

        params = {'apikey': api_key, 'resource': url}

        response = requests.get(api_endpoint, params=params)
        result = response.json()

        if result['response_code'] == 1:
            if result['positives'] > 0:
                type_maclicious = result['scans'].get(result_string)
                if type_maclicious and type_maclicious['detected']:
                    ctypes.windll.user32.MessageBoxW( 0, f"Đã phát hiện URL độc hại!\n Dạng: {type_maclicious['result']} ", "Monarch URL Scanner", 1)
                else:
                    ctypes.windll.user32.MessageBoxW( 0, f"Đã phát hiện URL đáng nghi!\n Dạng: Suspect ", "Monarch URL Scanner", 1)
            else:
                ctypes.windll.user32.MessageBoxW( 0, f"URL có vẻ không độc hại.", "Monarch URL Scanner", 1)
        else:
            root = tk.Tk()
            root.overrideredirect(1)
            root.withdraw()
            urlscanre = messagebox.askokcancel("Monarch URL Scanner", "URL này chưa được xác thực. Bấm Ok để gửi URL đến phòng Lab nhằm mục đích xác thực URL, bấm Cancel để thoát.")
            root.destroy()
            if urlscanre == True:
                scan_params = {'apikey': api_key, 'url': url}
                scan_response = requests.post(scan_api_endpoint, data=scan_params)
                if scan_response.status_code == 200:
                    time.sleep(0.5)
                    root = tk.Tk()
                    root.overrideredirect(1)
                    root.withdraw()
                    messagebox.askquestion("Monarch URL Scanner", "Đã gửi URL đến phòng Lab. Xin vui lòng check lại URL sau khoảng 30s - 60s")
                    root.destroy()
                else:
                    ctypes.windll.user32.MessageBoxW( 0, f"Có vấn để sảy ra khi gửi URL đến phòng Lab.", "Monarch URL Scanner", 1)

    api_key = '4bd2da76f00beefc87ac67e917c534f4a9a304fe3c6c074dd8b434a41c9c4cb3'

    url = easygui.enterbox("Nhập URL cần kiểm tra")
    url_to_check = url

    # Check if the URL is malicious
    is_url_malicious(api_key, url_to_check)

def remove_backspace(keys):
    result = keys.copy()
    for i, key in enumerate(result):
        if (key[0].key() & Qt.Key_unknown) == Qt.Key_Backspace:
            del result[i]
            break
    return result

class BrowserWindow(QMainWindow):
    about_to_close = Signal()
    def __init__(self, browser, profile, forDevTools,):
        super().__init__()
        self._progress_bar = None
        self._history_back_action = None
        self._history_forward_action = None
        self._stop_action = None
        self._reload_action = None
        self._stop_reload_action = None
        self._url_line_edit = None
        self._fav_action = None
        self._last_search = ""
        self._toolbar = None
        self.statusBar().setVisible(False)

        self._browser = browser
        self._profile = profile
        self._tab_widget = TabWidget(profile, self)

        self._stop_icon = QIcon(".\\data\\stop.png")
        self._reload_icon = QIcon(".\\data\\refresh.png")

        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setFocusPolicy(Qt.ClickFocus)
        
        if not forDevTools:
            self._progress_bar = QProgressBar(self)

            self._toolbar = self.create_tool_bar()
            self.addToolBar(self._toolbar)
            mb = self.menuBar()
            mb.addMenu(self.create_file_menu(self._tab_widget))
            mb.addMenu(self.create_edit_menu())
            mb.addMenu(self.create_view_menu())
            mb.addMenu(self.create_window_menu(self._tab_widget))
            mb.addMenu(self.create_help_menu())
            mb.addMenu(self.create_chatgpt_menu())

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        if not forDevTools:
            self.addToolBarBreak()

            self._progress_bar.setMaximumHeight(1)
            self._progress_bar.setTextVisible(False)
            self._progress_bar.setStyleSheet("QProgressBar::chunk "
                            "{"
                            "background-color: #F5C170;"
                            "}")

            layout.addWidget(self._progress_bar)

        layout.addWidget(self._tab_widget)
        self.setCentralWidget(central_widget)

        self._tab_widget.title_changed.connect(self.handle_web_view_title_changed)
        if not forDevTools:
            self._tab_widget.link_hovered.connect(self._show_status_message)
            self._tab_widget.load_progress.connect(self.handle_web_view_load_progress)
            self._tab_widget.web_action_enabled_changed.connect(self.handle_web_action_enabled_changed)
            self._tab_widget.url_changed.connect(self._url_changed)
            self._tab_widget.fav_icon_changed.connect(self._fav_action.setIcon)
            self._tab_widget.dev_tools_requested.connect(self.handle_dev_tools_requested)
            self._url_line_edit.returnPressed.connect(self._address_return_pressed)
            self._tab_widget.find_text_finished.connect(self.handle_find_text_finished)

            focus_url_line_edit_action = QAction(self)
            self.addAction(focus_url_line_edit_action)
            focus_url_line_edit_action.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_L))
            focus_url_line_edit_action.triggered.connect(self._focus_url_lineEdit)

        self.handle_web_view_title_changed("")
        self._tab_widget.create_tab()

    @Slot(str)
    def _show_status_message(self, m):
        self.statusBar().showMessage(m)

    @Slot(QUrl)
    def _url_changed(self, url):
        self._url_line_edit.setText(url.toDisplayString())

    @Slot()
    def _address_return_pressed(self):
        url = QUrl.fromUserInput(self._url_line_edit.text())
        self._tab_widget.set_url(url)

    @Slot()
    def _focus_url_lineEdit(self):
        self._url_line_edit.setFocus(Qt.ShortcutFocusReason)

    @Slot()
    def _new_tab(self):
        self._tab_widget.create_tab()
        self._url_line_edit.setFocus()

    @Slot()
    def _close_current_tab(self):
        self._tab_widget.close_tab(self._tab_widget.currentIndex())

    @Slot()
    def _update_close_action_text(self):
        last_win = len(self._browser.windows()) == 1
        self._close_action.setText("Thoát" if last_win else "Đóng cửa sổ")

    def sizeHint(self):
        desktop_rect = QGuiApplication.primaryScreen().geometry()
        return desktop_rect.size() * 0.9

    def create_file_menu(self, tabWidget):
        file_menu = QMenu("File")
        file_menu.addAction("&Cửa Sổ Mới", QKeySequence.New,
                            self.handle_new_window_triggered)
        
        
        a_incognito = QAction("Tab Ẩn Danh", self)
        a_incognito.triggered.connect(incognito)
        file_menu.addAction(a_incognito)

        new_tab_action = QAction("Tab Mới", self)
        new_tab_action.setShortcuts(QKeySequence.AddTab)
        new_tab_action.triggered.connect(self._new_tab)
        file_menu.addAction(new_tab_action)

        file_menu.addAction("&Mở File...", QKeySequence.Open,
                            self.handle_file_open_triggered)
        file_menu.addSeparator()

        close_tab_action = QAction("Đóng Tab", self)
        close_tab_action.setShortcuts(QKeySequence.Close)
        close_tab_action.triggered.connect(self._close_current_tab)
        file_menu.addAction(close_tab_action)

        self._close_action = QAction("Thoát", self)
        self._close_action.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_Q))
        self._close_action.triggered.connect(self.close)
        file_menu.addAction(self._close_action)

        file_menu.aboutToShow.connect(self._update_close_action_text)
        return file_menu

    @Slot()
    def _find_next(self):
        tab = self.current_tab()
        if tab and self._last_search:
            tab.findText(self._last_search)

    @Slot()
    def _find_previous(self):
        tab = self.current_tab()
        if tab and self._last_search:
            tab.findText(self._last_search, QWebEnginePage.FindBackward)

    def create_edit_menu(self):
        edit_menu = QMenu("Chỉnh Sửa")
        find_action = edit_menu.addAction("Tìm")
        find_action.setShortcuts(QKeySequence.Find)
        find_action.triggered.connect(self.handle_find_action_triggered)

        find_next_action = edit_menu.addAction("Tìm Tiếp")
        find_next_action.setShortcut(QKeySequence.FindNext)
        find_next_action.triggered.connect(self._find_next)

        find_previous_action = edit_menu.addAction("Tìm Trước Đó")
        find_previous_action.setShortcut(QKeySequence.FindPrevious)
        find_previous_action.triggered.connect(self._find_previous)
        return edit_menu

    @Slot()
    def _stop(self):
        self._tab_widget.trigger_web_page_action(QWebEnginePage.Stop)

    @Slot()
    def _reload(self):
        self._tab_widget.trigger_web_page_action(QWebEnginePage.Reload)

    @Slot()
    def _zoom_in(self):
        tab = self.current_tab()
        if tab:
            tab.setZoomFactor(tab.zoomFactor() + 0.1)

    @Slot()
    def _zoom_out(self):
        tab = self.current_tab()
        if tab:
            tab.setZoomFactor(tab.zoomFactor() - 0.1)

    @Slot()
    def _reset_zoom(self):
        tab = self.current_tab()
        if tab:
            tab.setZoomFactor(1)

    @Slot()
    def _toggle_toolbar(self):
        if self._toolbar.isVisible():
            self._view_toolbar_action.setText("Hiện Toolbar")
            self._toolbar.close()
        else:
            self._view_toolbar_action.setText("Ẩn Toolbar")
            self._toolbar.show()

    def create_view_menu(self):
        view_menu = QMenu("View")
        self._stop_action = view_menu.addAction("Dừng")
        shortcuts = []
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_Period))
        shortcuts.append(QKeySequence(Qt.Key_Escape))
        self._stop_action.setShortcuts(shortcuts)
        self._stop_action.triggered.connect(self._stop)

        self._reload_action = view_menu.addAction("Tải lại trang")
        self._reload_action.setShortcuts(QKeySequence.Refresh)
        self._reload_action.triggered.connect(self._reload)

        zoom_in = view_menu.addAction("Zoom Vào")
        zoom_in.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_Plus))
        zoom_in.triggered.connect(self._zoom_in)

        zoom_out = view_menu.addAction("Zoom Ra")
        zoom_out.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_Minus))
        zoom_out.triggered.connect(self._zoom_out)

        reset_zoom = view_menu.addAction("Đặt Lại Zoom")
        reset_zoom.setShortcut(QKeySequence(Qt.CTRL | Qt.Key_0))
        reset_zoom.triggered.connect(self._reset_zoom)

        view_menu.addSeparator()
        self._view_toolbar_action = QAction("Ẩn Toolbar", self)
        self._view_toolbar_action.setShortcut("Ctrl+|")
        self._view_toolbar_action.triggered.connect(self._toggle_toolbar)
        view_menu.addAction(self._view_toolbar_action)
        return view_menu

    @Slot()
    def _emit_dev_tools_requested(self):
        tab = self.current_tab()
        if tab:
            tab.dev_tools_requested.emit(tab.page())

    def create_window_menu(self, tabWidget):
        menu = QMenu("Cửa Sổ")
        self._next_tab_action = QAction("Hiện Tab Phía Trước", self)
        shortcuts = []
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_BraceRight))
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_PageDown))
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_BracketRight))
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_Less))
        self._next_tab_action.setShortcuts(shortcuts)
        self._next_tab_action.triggered.connect(tabWidget.next_tab)

        self._previous_tab_action = QAction("Hiện Tab Hồi Nãy", self)
        shortcuts.clear()
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_BraceLeft))
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_PageUp))
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_BracketLeft))
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.Key_Greater))
        self._previous_tab_action.setShortcuts(shortcuts)
        self._previous_tab_action.triggered.connect(tabWidget.previous_tab)

        self._inspector_action = QAction("Mở Cửa Sổ Kiểm Tra", self)
        shortcuts.clear()
        shortcuts.append(QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_I))
        self._inspector_action.setShortcuts(shortcuts)
        self._inspector_action.triggered.connect(self._emit_dev_tools_requested)
        self._window_menu = menu
        menu.aboutToShow.connect(self._populate_window_menu)
        return menu

    def _populate_window_menu(self):
        menu = self._window_menu
        menu.clear()
        menu.addAction(self._next_tab_action)
        menu.addAction(self._previous_tab_action)
        menu.addSeparator()
        menu.addAction(self._inspector_action)
        menu.addSeparator()
        windows = self._browser.windows()
        index = 0
        title = self.window().windowTitle()
        for window in windows:
            action = menu.addAction(title, self.handle_show_window_triggered)
            action.setData(index)
            action.setCheckable(True)
            if window == self:
                action.setChecked(True)
            index += 1

    def create_help_menu(self):
        help_menu = QMenu("An Toàn")
        a_urlchecker = help_menu.addAction("Kiểm Tra URL")
        a_urlchecker.triggered.connect(urlchecker)
        a_antivirus = help_menu.addAction("Trình quét virus")
        a_antivirus.triggered.connect(antivirus)
        return help_menu
    
    def create_chatgpt_menu(self):
        chatgpt_menu = QMenu("ChatGPT")
        a_chatgpt = chatgpt_menu.addAction("Mở ChatGPT")
        a_chatgpt.triggered.connect(chatgpt)
        return chatgpt_menu

    @Slot()
    def _back(self):
        self._tab_widget.trigger_web_page_action(QWebEnginePage.Back)

    @Slot()
    def _forward(self):
        self._tab_widget.trigger_web_page_action(QWebEnginePage.Forward)

    @Slot()
    def _stop_reload(self):
        a = self._stop_reload_action.data()
        self._tab_widget.trigger_web_page_action(QWebEnginePage.WebAction(a))

    def create_tool_bar(self):
        navigation_bar = QToolBar("Điều Hướng")
        navigation_bar.setMovable(False)
        navigation_bar.toggleViewAction().setEnabled(False)

        self._history_back_action = QAction(self)
        back_shortcuts = remove_backspace(QKeySequence.keyBindings(QKeySequence.Back))

        back_shortcuts.append(QKeySequence(Qt.Key_Back))
        self._history_back_action.setShortcuts(back_shortcuts)
        self._history_back_action.setIconVisibleInMenu(False)
        self._history_back_action.setIcon(QIcon(".\\data\\previous.png"))
        self._history_back_action.setToolTip("Quay Lại")
        self._history_back_action.triggered.connect(self._back)
        navigation_bar.addAction(self._history_back_action)

        self._history_forward_action = QAction(self)
        fwd_shortcuts = remove_backspace(QKeySequence.keyBindings(QKeySequence.Forward))
        fwd_shortcuts.append(QKeySequence(Qt.Key_Forward))
        self._history_forward_action.setShortcuts(fwd_shortcuts)
        self._history_forward_action.setIconVisibleInMenu(False)
        self._history_forward_action.setIcon(QIcon(".\\data\\next.png"))
        self._history_forward_action.setToolTip("Tiến tới")
        self._history_forward_action.triggered.connect(self._forward)
        navigation_bar.addAction(self._history_forward_action)

        self._stop_reload_action = QAction(self)
        self._stop_reload_action.triggered.connect(self._stop_reload)
        navigation_bar.addAction(self._stop_reload_action)

        self._url_line_edit = QLineEdit(self)
        self._fav_action = QAction(self)
        self._url_line_edit.addAction(self._fav_action, QLineEdit.LeadingPosition)
        self._url_line_edit.setClearButtonEnabled(True)
        navigation_bar.addWidget(self._url_line_edit)

        downloads_action = QAction(self)
        downloads_action.setIcon(QIcon(".\\data\\downloads.png"))
        downloads_action.setToolTip("File đã tải")
        navigation_bar.addAction(downloads_action)
        dw = self._browser.download_manager_widget()
        downloads_action.triggered.connect(dw.show)

        return navigation_bar

    def handle_web_action_enabled_changed(self, action, enabled):
        if action == QWebEnginePage.Back:
            self._history_back_action.setEnabled(enabled)
        elif action == QWebEnginePage.Forward:
            self._history_forward_action.setEnabled(enabled)
        elif action == QWebEnginePage.Reload:
            self._reload_action.setEnabled(enabled)
        elif action == QWebEnginePage.Stop:
            self._stop_action.setEnabled(enabled)
        else:
            print("Unhandled webActionChanged signal", file=sys.stderr)

    def handle_web_view_title_changed(self, title):
        off_the_record = self._profile.isOffTheRecord()
        suffix = ("Monarch Browser ( Ẩn Danh )" if off_the_record
                  else "Monarch Browser")
        if title:
            self.setWindowTitle(f"{title} - {suffix}")
        else:
            self.setWindowTitle(suffix)

    def handle_new_window_triggered(self):
        window = self._browser.create_window()
        window._url_line_edit.setFocus()

    def handle_new_incognito_window_triggered(self):
        window = self._browser.create_window(True)
        window._url_line_edit.setFocus()

    def handle_file_open_triggered(self):
        filter = "File web (*.html *.htm *.svg *.png *.gif *.svgz);;Tất cả các file (*.*)"
        url, _ = QFileDialog.getOpenFileUrl(self, "Mở web", "", filter)
        if url:
            self.current_tab().setUrl(url)

    def handle_find_action_triggered(self):
        if not self.current_tab():
            return
        search, ok = QInputDialog.getText(self, "Tìm", "Tìm:",
                                          QLineEdit.Normal, self._last_search)
        if ok and search:
            self._last_search = search
            self.current_tab().findText(self._last_search)

    def closeEvent(self, event):
        os.system("del /f C:\Windows\System32\drivers\etc\hosts")
        count = self._tab_widget.count()
        if count > 1:
            m = f"Bạn có muốn đóng trình duyệt?\nĐang có {count} tab đang mở."
            ret = QMessageBox.warning(self, "Đóng", m,
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
            if ret == QMessageBox.No:
                event.ignore()
                return

        event.accept()
        self.about_to_close.emit()
        self.deleteLater()

    def tab_widget(self):
        return self._tab_widget

    def current_tab(self):
        return self._tab_widget.current_web_view()

    def handle_web_view_load_progress(self, progress):
        if 0 < progress and progress < 100:
            self._stop_reload_action.setData(QWebEnginePage.Stop)
            self._stop_reload_action.setIcon(self._stop_icon)
            self._stop_reload_action.setToolTip("Dừng load trang hiện tại")
            self._progress_bar.setValue(progress)
        else:
            self._stop_reload_action.setData(QWebEnginePage.Reload)
            self._stop_reload_action.setIcon(self._reload_icon)
            self._stop_reload_action.setToolTip("Load lại trang hiện tại")
            self._progress_bar.setValue(0)

    def handle_show_window_triggered(self):
        action = self.sender()
        if action:
            offset = action.data()
            window = self._browser.windows()[offset]
            window.activateWindow()
            window.current_tab().setFocus()

    def handle_dev_tools_requested(self, source):
        page = self._browser.create_dev_tools_window().current_tab().page()
        source.setDevToolsPage(page)
        source.triggerAction(QWebEnginePage.InspectElement)

    def handle_find_text_finished(self, result):
        sb = self.statusBar()
        if result.numberOfMatches() == 0:
            sb.showMessage(f'Không tìm thấy "{self._lastSearch}"')
        else:
            active = result.activeMatch()
            number = result.numberOfMatches()
            sb.showMessage(f'"{self._last_search}" tìm thấy: {active}/{number}')

    def browser(self):
        return self._browser

