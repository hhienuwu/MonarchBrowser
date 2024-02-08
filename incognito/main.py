import re
import sys
import ctypes
import random
import qdarkstyle
import stem.process
import tkinter as tk
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from tkinter import messagebox
from PyQt5 import QtWebEngineCore
from PyQt5.QtPrintSupport import *
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *
from adblockparser import AdblockRules
from PyQt5.QtNetwork import QNetworkProxy

ctypes.windll.user32.MessageBoxW( 0,"Monarch Incognito cần một lúc khoảng 30s nhằm đảm bảo sự an toàn cho bạn, hãy đợi xíu nhé!", "Monarch Incognito", 1)

try:
	with open('.\\data\\database.txt', 'r', encoding='utf-8', buffering=124005) as f:
		raw_rules = f.readlines()
		rules = AdblockRules(raw_rules)

	class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
		def interceptRequest(self, info):
			url = info.requestUrl().toString()
			if rules.should_block(url):
				info.block(True)

	class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
		def interceptRequest(self, info):
			url = info.requestUrl().toString()
			if url == "/hook.js":
				info.block(True)
except:
	ctypes.windll.user32.MessageBoxW( 0,"Không tìm thấy file khởi chạy an toàn, xin vui lòng cài lại trình duyệt", "Monarch Antivirus", 1)

class MainWindow(QMainWindow):
	def	__init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args,	**kwargs)
		self.browser = QWebEngineView(self)
		self.browser.setUrl(QUrl("https://duckduckgo.com/duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"))
		self.setCentralWidget(self.browser)
		self.setGeometry(50, 50, 1200, 650)
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage('.\\data\\incognitoicon.png'))))
		self.toolbar = QtWidgets.QToolBar("Thanh Công Cụ")

		user_agent_string = "Monarch Incognito User"

		self.browser.page().profile().setHttpUserAgent(
			user_agent_string
		)

		self.tabs =	QTabWidget()

		self.tabs.setDocumentMode(True)

		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

		self.tabs.currentChanged.connect(self.current_tab_changed)

		self.tabs.setTabsClosable(True)

		self.tabs.tabCloseRequested.connect(self.close_current_tab)

		self.setCentralWidget(self.tabs)

		self.status	= QStatusBar()

		self.setStatusBar(self.status)

		self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)

		self.toolbar.setMovable(False)

		back_btn = QAction("<",	self)

		back_btn.setStatusTip("Quay	lại trang trước.")

		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

		self.toolbar.addAction(back_btn)

		next_btn = QAction(">",	self)
		next_btn.setStatusTip("Tiến tới trang vừa quay lại")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		self.toolbar.addAction(next_btn)

		reload_btn = QAction("Tải lại", self)
		reload_btn.setStatusTip("Tải lại trang")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		self.toolbar.addAction(reload_btn)

		home_btn = QAction("Search", self)
		home_btn.setStatusTip("Tìm kiếm	bằng DuckDuckGo")

		home_btn.triggered.connect(self.navigate_home)
	
		self.toolbar.addAction(home_btn)

		self.urlbar	= QLineEdit()

		self.urlbar.returnPressed.connect(self.navigate_to_url)

		self.toolbar.addWidget(self.urlbar)

		self.add_new_tab(QUrl("https://duckduckgo.com/duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"),'Chào Mừng!')

		self.show()

		self.setWindowTitle("Monarch Incognito")


	def	add_new_tab(self, qurl = None, label ="Blank"):
		if qurl	is None:
			qurl = QUrl("https://duckduckgo.com/duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")

		browser	= QWebEngineView()

		browser.setUrl(qurl)

		i =	self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)

		browser.urlChanged.connect(lambda qurl,	browser	= browser:
								self.update_urlbar(qurl, browser))

		browser.loadFinished.connect(lambda	_, i = i, browser =	browser:
									self.tabs.setTabText(i,	browser.page().title()))

	def	tab_open_doubleclick(self, i):
		if i == -1:
			self.add_new_tab()

	def	current_tab_changed(self, i):

		qurl = self.tabs.currentWidget().url()

		self.update_urlbar(qurl, self.tabs.currentWidget())

		self.update_title(self.tabs.currentWidget())

	def	close_current_tab(self,	i):

		if self.tabs.count() < 2:
			return

		self.tabs.removeTab(i)

	def	update_title(self, browser):

		if browser != self.tabs.currentWidget():
			return
		self.setWindowTitle("Monarch Incognito")

	def	navigate_home(self):

		self.tabs.currentWidget().setUrl(QUrl("https://duckduckgo.com/duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"))

	def	navigate_to_url(self):

		q =	QUrl(self.urlbar.text())

		if q.scheme() == "":
			q.setScheme("https")

		self.tabs.currentWidget().setUrl(q)

	def	update_urlbar(self,	q, browser = None):

		if browser != self.tabs.currentWidget():

			return

		self.urlbar.setText(q.toString())

		self.urlbar.setCursorPosition(0)

try:
	def launch_tor_process():
		SOCKS_PORT = 9050
		CONTROL_PORT = 9051
		TOR_PATH = ".\\Tor\\tor.exe"
		tor_process = stem.process.launch_tor_with_config(
			config={
				'SocksPort': str(SOCKS_PORT),
				'ControlPort': str(CONTROL_PORT),
				'ExitNodes': '',
				'StrictNodes': '1',
				'CookieAuthentication': '1',
				'MaxCircuitDirtiness': '60',
			},
			take_ownership=True,
			init_msg_handler=lambda line: print(line) if re.search(
				'Bootstrapped', line) else False,
			tor_cmd=TOR_PATH
		)

	launch_tor_process()

	PROXY_PORT = 9050
	PROXY_HOST = "127.0.0.1"
	proxy = QNetworkProxy()
	proxy.setType(QNetworkProxy.Socks5Proxy)
	proxy.setHostName(PROXY_HOST)
	proxy.setPort(PROXY_PORT)
	QNetworkProxy.setApplicationProxy(proxy)

except:
	ctypes.windll.user32.MessageBoxW( 0,"Không thể khởi chạy TOR. Vui lòng kiểm tra lại mạng hoặc tải lại phần mềm", "Monarch Incognito", 1)


app = QtWidgets.QApplication([])

app.setStyleSheet(qdarkstyle.load_stylesheet())

interceptor = WebEngineUrlRequestInterceptor()
QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setRequestInterceptor(interceptor)

app.setApplicationName("Monarch Incognito")
 
window = MainWindow()

sys.exit(app.exec_())
