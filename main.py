import re
import sys
import ctypes
import random
import qdarkstyle
import stem.process
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtNetwork import QNetworkProxy
from PyQt5.QtWidgets import*
from PyQt5 import QtWebEngineCore
from PyQt5.QtPrintSupport import *
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *
from adblockparser import AdblockRules




ctypes.windll.user32.MessageBoxW( 0,"Monarch Incognito cần một lúc khoảng 30s nhằm đảm bảo sự an toàn cho bạn, hãy đợi xíu nhé!", "Monarch Incognito", 1)

with open('.\\data\\database.txt', 'r', encoding='utf-8', buffering=124005) as f:
    raw_rules = f.readlines()
    rules = AdblockRules(raw_rules)

class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if rules.should_block(url):
            info.block(True)


class MainWindow(QMainWindow):
	def	__init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args,	**kwargs)
		self.browser = QWebEngineView(self)
		self.browser.setUrl(QUrl("https://duckduckgo.com/duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion"))
		self.setCentralWidget(self.browser)
		self.setGeometry(50, 50, 1200, 650)
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(QtGui.QImage('.\\data\\incognitoicon.png'))))
		self.toolbar = QtWidgets.QToolBar("Thanh Công Cụ")

		agent_list = ["Mozilla/5.0 (Linux; Android 4.2.2; QMV7B Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.0.3; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36","Mozilla/5.0 (iPad; U; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4","Mozilla/5.0 (Linux; Android 5.0.1; VS985 4G Build/LRX21Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H143 Safari/600.1.4","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020b Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36","Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0","Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0","Instagram/140490268 CFNetwork/1121.2.2 Darwin/19.2.0","Instagram/114853457 CFNetwork/1107.1 Darwin/19.0.0","Instagram/58745335 CFNetwork/811.4.18 Darwin/16.5.0","Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36 Instagram 313.0.0.0.42 Android (33/13; 480dpi; 1080x2176; samsung; SM-G991B; o1s; exynos2100; pt_BR; 547447643)","Mozilla/5.0 (Linux; Android 13; CRT-NX1 Build/HONORCRT-N31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36 Instagram 313.0.0.0.42 Android (33/13; 480dpi; 1080x2173; HONOR; CRT-NX1; HNCRT-M2; mt6833; en_MY; 547447561)","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_32.5.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US isDarkMode/1 WKWebView/1 RevealType/Dialog BytedanceWebview/d8a21c6 FalconTag/","Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_99.9.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/ru Region/CA RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/","Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.45(0x18002d24) NetType/4G Language/zh_CN","Mozilla/5.0 (Linux; Android 4.4.2; SM-T310 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; Nexus 10 Build/LMY48I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36","Mozilla/5.0 (X11; CrOS x86_64 7077.123.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; QMV7A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53","Mozilla/5.0 (Linux; Android 5.0; SAMSUNG-SM-N900A Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.4; XT1080 Build/SU6-7.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12F69 Safari/600.1.4","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"]

		user_agent_string = random.choice(agent_list)

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


app = QtWidgets.QApplication([])

app.setStyleSheet(qdarkstyle.load_stylesheet())

interceptor = WebEngineUrlRequestInterceptor()
QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setRequestInterceptor(interceptor)

app.setApplicationName("Monarch Incognito")
 
window = MainWindow()

sys.exit(app.exec_())
