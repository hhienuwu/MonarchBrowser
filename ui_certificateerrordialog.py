import ctypes
try:
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
        QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
        QWidget)

    class Ui_CertificateErrorDialog(object):
        def setupUi(self, CertificateErrorDialog):
            if not CertificateErrorDialog.objectName():
                CertificateErrorDialog.setObjectName(u"Chứng chỉ lỗi")
            CertificateErrorDialog.resize(370, 141)
            self.verticalLayout = QVBoxLayout(CertificateErrorDialog)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.verticalLayout.setContentsMargins(20, -1, 20, -1)
            self.m_iconLabel = QLabel(CertificateErrorDialog)
            self.m_iconLabel.setObjectName(u"m_iconLabel")
            self.m_iconLabel.setAlignment(Qt.AlignCenter)

            self.verticalLayout.addWidget(self.m_iconLabel)

            self.m_errorLabel = QLabel(CertificateErrorDialog)
            self.m_errorLabel.setObjectName(u"m_errorLabel")
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.m_errorLabel.sizePolicy().hasHeightForWidth())
            self.m_errorLabel.setSizePolicy(sizePolicy)
            self.m_errorLabel.setAlignment(Qt.AlignCenter)
            self.m_errorLabel.setWordWrap(True)

            self.verticalLayout.addWidget(self.m_errorLabel)

            self.m_infoLabel = QLabel(CertificateErrorDialog)
            self.m_infoLabel.setObjectName(u"m_infoLabel")
            sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
            sizePolicy1.setHorizontalStretch(0)
            sizePolicy1.setVerticalStretch(0)
            sizePolicy1.setHeightForWidth(self.m_infoLabel.sizePolicy().hasHeightForWidth())
            self.m_infoLabel.setSizePolicy(sizePolicy1)
            self.m_infoLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
            self.m_infoLabel.setWordWrap(True)

            self.verticalLayout.addWidget(self.m_infoLabel)

            self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Expanding)

            self.verticalLayout.addItem(self.verticalSpacer)

            self.buttonBox = QDialogButtonBox(CertificateErrorDialog)
            self.buttonBox.setObjectName(u"buttonBox")
            self.buttonBox.setOrientation(Qt.Horizontal)
            self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)

            self.verticalLayout.addWidget(self.buttonBox)


            self.retranslateUi(CertificateErrorDialog)
            self.buttonBox.accepted.connect(CertificateErrorDialog.accept)
            self.buttonBox.rejected.connect(CertificateErrorDialog.reject)

            QMetaObject.connectSlotsByName(CertificateErrorDialog)

        def retranslateUi(self, CertificateErrorDialog):
            CertificateErrorDialog.setWindowTitle(QCoreApplication.translate("Chứng chỉ lỗi", u"Dialog", None))
            self.m_iconLabel.setText(QCoreApplication.translate("Chứng chỉ lỗi", u"Icon", None))
            self.m_errorLabel.setText(QCoreApplication.translate("Chứng chỉ lỗi", u"Lỗi", None))
            self.m_infoLabel.setText(QCoreApplication.translate("Chứng chỉ lỗi", u"Nếu bạn muốn, bạn có thể truy cập vào trang chứng chỉ lỗi này\n"
    "\n"
    "Bạn có muốn vượt qua chứng chỉ lỗi và tiếp tục ?   ", None))
except:
    ctypes.windll.user32.MessageBoxW( 0,"Không thể khởi chạy ui_certierrordiag, xin vui lòng cài lại trình duyệt", "Monarch Browser", 1)
