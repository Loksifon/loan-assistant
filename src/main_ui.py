# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

#основной класс
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(711, 700)
		MainWindow.setMaximumSize(QtCore.QSize(711, 700))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setMinimumSize(QtCore.QSize(711, 700))
		self.centralwidget.setMaximumSize(QtCore.QSize(543, 16777215))
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 713, 551))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(0, 0, 711, 701))
		self.frame.setMinimumSize(QtCore.QSize(711, 543))
		self.frame.setAutoFillBackground(False)
		self.frame.setStyleSheet("background-color: #f4f5f8;")
		self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame.setObjectName("frame")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(190, 20, 341, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.tab_menu = QtWidgets.QTabWidget(self.frame)
		self.tab_menu.setGeometry(QtCore.QRect(0, 60, 711, 641))
		self.tab_menu.setMinimumSize(QtCore.QSize(711, 0))
		self.tab_menu.setObjectName("tab_menu")
		self.tab_credit = QtWidgets.QWidget()
		self.tab_credit.setObjectName("tab_credit")
		self.frame_3 = QtWidgets.QFrame(self.tab_credit)
		self.frame_3.setGeometry(QtCore.QRect(-10, 0, 721, 181))
		self.frame_3.setStyleSheet("background-color: white;")
		self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_3.setObjectName("frame_3")
		#Сумма кредита - поле
		self.credit_sum = QtWidgets.QLineEdit(self.frame_3)
		self.credit_sum.setGeometry(QtCore.QRect(50, 30, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.credit_sum.setFont(font)
		self.credit_sum.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")
		#Кнопки кредита - сумма
		self.credit_sum.setText("")
		self.credit_sum.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.credit_sum.setObjectName("credit_sum")
		self.credit_year = QtWidgets.QLineEdit(self.frame_3)
		self.credit_year.setGeometry(QtCore.QRect(50, 100, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.credit_year.setFont(font)
		self.credit_year.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")

		#Кнопки кредита - годы
		self.credit_year.setText("")
		self.credit_year.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.credit_year.setObjectName("credit_year")
		self.frame_5 = QtWidgets.QFrame(self.frame_3)
		self.frame_5.setGeometry(QtCore.QRect(400, 10, 271, 161))
		self.frame_5.setStyleSheet("border: 2px solid grey;")
		self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_5.setObjectName("frame_5")
		self.label_2 = QtWidgets.QLabel(self.frame_5)
		self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 21))
		self.label_2.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.frame_5)
		self.label_3.setGeometry(QtCore.QRect(140, 20, 71, 21))
		self.label_3.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.frame_5)
		self.label_4.setGeometry(QtCore.QRect(20, 60, 71, 21))
		self.label_4.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_4.setObjectName("label_4")
		self.credit_payment = QtWidgets.QLabel(self.frame_5)
		self.credit_payment.setGeometry(QtCore.QRect(140, 60, 121, 21))
		self.credit_payment.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.credit_payment.setObjectName("credit_payment")
		self.btn_credit = QtWidgets.QPushButton(self.frame_5)
		self.btn_credit.setGeometry(QtCore.QRect(20, 110, 231, 31))
		self.btn_credit.setStyleSheet("border: 1px solid transparent;\n"
"background-color: rgb(3, 155, 229);\n"
"border-radius: 8px;\n"
"color: white;\n"
"font-size: 14px;\n"
"")
		self.btn_credit.setObjectName("btn_credit")
		self.frame_2 = QtWidgets.QFrame(self.tab_credit)
		self.frame_2.setGeometry(QtCore.QRect(0, 190, 711, 431))
		self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_2.setObjectName("frame_2")
		self.credit_banks = QtWidgets.QLabel(self.frame_2)
		self.credit_banks.setGeometry(QtCore.QRect(21, 11, 231, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.credit_banks.setFont(font)
		self.credit_banks.setObjectName("credit_banks")
		self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)
		self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 691, 351))
		self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
		self.scroll_widget_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
		self.scroll_widget_3.setContentsMargins(0, 0, 0, 0)
		self.scroll_widget_3.setObjectName("scroll_widget_3")
		self.scrollArea_3 = QtWidgets.QScrollArea(self.verticalLayoutWidget_3)
		self.scrollArea_3.setWidgetResizable(True)
		self.scrollArea_3.setObjectName("scrollArea_3")
		self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 687, 347))
		self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
		self.frame_31 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
		self.frame_31.setGeometry(QtCore.QRect(0, 0, 691, 351))
		self.frame_31.setStyleSheet("background-color: white;")
		self.frame_31.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_31.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_31.setObjectName("frame_31")
		self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
		self.scroll_widget_3.addWidget(self.scrollArea_3)
		self.tab_menu.addTab(self.tab_credit, "")
		self.tab_deposit = QtWidgets.QWidget()
		self.tab_deposit.setObjectName("tab_deposit")
		self.frame_4 = QtWidgets.QFrame(self.tab_deposit)
		self.frame_4.setGeometry(QtCore.QRect(-10, 0, 721, 201))
		self.frame_4.setStyleSheet("background-color: white;")
		self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_4.setObjectName("frame_4")
		self.deposit_sum = QtWidgets.QLineEdit(self.frame_4)
		self.deposit_sum.setGeometry(QtCore.QRect(50, 30, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.deposit_sum.setFont(font)
		self.deposit_sum.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")
		self.deposit_sum.setText("")
		self.deposit_sum.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.deposit_sum.setObjectName("deposit_sum")
		self.deposit_year = QtWidgets.QLineEdit(self.frame_4)
		self.deposit_year.setGeometry(QtCore.QRect(50, 100, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.deposit_year.setFont(font)
		self.deposit_year.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")
		self.deposit_year.setText("")
		self.deposit_year.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.deposit_year.setObjectName("deposit_year")
		self.frame_6 = QtWidgets.QFrame(self.frame_4)
		self.frame_6.setGeometry(QtCore.QRect(400, 10, 271, 161))
		self.frame_6.setStyleSheet("border: 2px solid grey;")
		self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_6.setObjectName("frame_6")
		self.label_6 = QtWidgets.QLabel(self.frame_6)
		self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 21))
		self.label_6.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self.frame_6)
		self.label_7.setGeometry(QtCore.QRect(140, 20, 71, 21))
		self.label_7.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.frame_6)
		self.label_8.setGeometry(QtCore.QRect(20, 60, 51, 21))
		self.label_8.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_8.setObjectName("label_8")
		self.deposit_payment = QtWidgets.QLabel(self.frame_6)
		self.deposit_payment.setGeometry(QtCore.QRect(140, 60, 121, 21))
		self.deposit_payment.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.deposit_payment.setObjectName("deposit_payment")
		self.btn_deposit = QtWidgets.QPushButton(self.frame_6)
		self.btn_deposit.setGeometry(QtCore.QRect(20, 110, 231, 31))
		self.btn_deposit.setAutoFillBackground(False)
		self.btn_deposit.setStyleSheet("border: 1px solid transparent;\n"
"background-color: rgb(3, 155, 229);\n"
"border-radius: 8px;\n"
"color: white;\n"
"font-size: 14px;\n"
"\n"
"")
		self.btn_deposit.setObjectName("btn_deposit")
		self.frame_27 = QtWidgets.QFrame(self.tab_deposit)
		self.frame_27.setGeometry(QtCore.QRect(0, 190, 711, 431))
		self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_27.setObjectName("frame_27")
		self.deposit_banks = QtWidgets.QLabel(self.frame_27)
		self.deposit_banks.setGeometry(QtCore.QRect(11, 31, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.deposit_banks.setFont(font)
		self.deposit_banks.setObjectName("deposit_banks")
		self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_27)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 691, 341))
		self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
		self.scroll_widget_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
		self.scroll_widget_2.setContentsMargins(0, 0, 0, 0)
		self.scroll_widget_2.setObjectName("scroll_widget_2")
		self.scrollArea_2 = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
		self.scrollArea_2.setWidgetResizable(True)
		self.scrollArea_2.setObjectName("scrollArea_2")
		self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 687, 337))
		self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
		self.frame_30 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
		self.frame_30.setGeometry(QtCore.QRect(-1, -1, 691, 341))
		self.frame_30.setStyleSheet("background-color: white;")
		self.frame_30.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_30.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_30.setObjectName("frame_30")
		self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
		self.scroll_widget_2.addWidget(self.scrollArea_2)
		self.tab_menu.addTab(self.tab_deposit, "")
		self.mortgage = QtWidgets.QWidget()
		self.mortgage.setObjectName("mortgage")
		self.frame_7 = QtWidgets.QFrame(self.mortgage)
		self.frame_7.setGeometry(QtCore.QRect(0, 0, 701, 251))
		self.frame_7.setStyleSheet("background-color: white;")
		self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_7.setObjectName("frame_7")
		self.mortgage_sum = QtWidgets.QLineEdit(self.frame_7)
		self.mortgage_sum.setGeometry(QtCore.QRect(50, 30, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.mortgage_sum.setFont(font)
		self.mortgage_sum.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")
		self.mortgage_sum.setText("")
		self.mortgage_sum.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.mortgage_sum.setObjectName("mortgage_sum")
		self.mortgage_year = QtWidgets.QLineEdit(self.frame_7)
		self.mortgage_year.setGeometry(QtCore.QRect(50, 100, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.mortgage_year.setFont(font)
		self.mortgage_year.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")
		self.mortgage_year.setText("")
		self.mortgage_year.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.mortgage_year.setObjectName("mortgage_year")
		self.frame_8 = QtWidgets.QFrame(self.frame_7)
		self.frame_8.setGeometry(QtCore.QRect(380, 30, 301, 191))
		self.frame_8.setStyleSheet("border: 2px solid grey;")
		self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_8.setObjectName("frame_8")
		self.label_10 = QtWidgets.QLabel(self.frame_8)
		self.label_10.setGeometry(QtCore.QRect(20, 20, 61, 21))
		self.label_10.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(self.frame_8)
		self.label_11.setGeometry(QtCore.QRect(170, 20, 71, 21))
		self.label_11.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(self.frame_8)
		self.label_12.setGeometry(QtCore.QRect(20, 100, 71, 21))
		self.label_12.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_12.setObjectName("label_12")
		self.label_13 = QtWidgets.QLabel(self.frame_8)
		self.label_13.setGeometry(QtCore.QRect(180, 100, 111, 21))
		self.label_13.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_13.setObjectName("label_13")
		self.btn_mortgage = QtWidgets.QPushButton(self.frame_8)
		self.btn_mortgage.setGeometry(QtCore.QRect(40, 140, 231, 31))
		self.btn_mortgage.setStyleSheet("border: 1px solid transparent;\n"
"background-color: rgb(3, 155, 229);\n"
"border-radius: 8px;\n"
"color: white;\n"
"font-size: 14px;\n"
"\n"
"")
		self.btn_mortgage.setObjectName("btn_mortgage")
		self.label_53 = QtWidgets.QLabel(self.frame_8)
		self.label_53.setGeometry(QtCore.QRect(20, 60, 121, 21))
		self.label_53.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.label_53.setObjectName("label_53")
		self.mortgage_sumKredita = QtWidgets.QLabel(self.frame_8)
		self.mortgage_sumKredita.setGeometry(QtCore.QRect(170, 60, 121, 21))
		self.mortgage_sumKredita.setStyleSheet("border:none;\n"
"font-size: 16px;")
		self.mortgage_sumKredita.setObjectName("mortgage_sumKredita")
		self.mortgage_vznos = QtWidgets.QLineEdit(self.frame_7)
		self.mortgage_vznos.setGeometry(QtCore.QRect(50, 170, 261, 41))
		font = QtGui.QFont()
		font.setPointSize(-1)
		self.mortgage_vznos.setFont(font)
		self.mortgage_vznos.setStyleSheet("color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"font-size: 16px;")
		self.mortgage_vznos.setText("")
		self.mortgage_vznos.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.mortgage_vznos.setObjectName("mortgage_vznos")
		self.frame_28 = QtWidgets.QFrame(self.mortgage)
		self.frame_28.setGeometry(QtCore.QRect(0, 250, 711, 371))
		self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_28.setObjectName("frame_28")
		self.mortgage_banks = QtWidgets.QLabel(self.frame_28)
		self.mortgage_banks.setGeometry(QtCore.QRect(10, 30, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.mortgage_banks.setFont(font)
		self.mortgage_banks.setObjectName("mortgage_banks")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_28)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 691, 291))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.scroll_widget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.scroll_widget.setContentsMargins(0, 0, 0, 0)
		self.scroll_widget.setObjectName("scroll_widget")
		self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 687, 287))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.frame_29 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
		self.frame_29.setGeometry(QtCore.QRect(0, 0, 691, 291))
		self.frame_29.setStyleSheet("background-color: white;")
		self.frame_29.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
		self.frame_29.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.frame_29.setObjectName("frame_29")
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.scroll_widget.addWidget(self.scrollArea)
		self.tab_menu.addTab(self.mortgage, "")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.tab_menu.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)



		## to get sum

		self.credit_sum.textChanged.connect(self.getCredit)
		self.credit_year.textChanged.connect(self.getCredit)
		self.credit_sum.setValidator(QtGui.QIntValidator(1,100000000))
		self.credit_year.setValidator(QtGui.QIntValidator(1,10))

		self.deposit_sum.textChanged.connect(self.getDep)
		self.deposit_year.textChanged.connect(self.getDep)
		self.deposit_sum.setValidator(QtGui.QIntValidator(1,100000000))
		self.deposit_year.setValidator(QtGui.QIntValidator(1,10))


		self.mortgage_sum.textChanged.connect(self.getMortgage)
		self.mortgage_year.textChanged.connect(self.getMortgage)
		self.mortgage_vznos.textChanged.connect(self.getMortgage)		
		self.mortgage_sum.setValidator(QtGui.QIntValidator(1,100000000))
		self.mortgage_year.setValidator(QtGui.QIntValidator(1,10))
		self.mortgage_vznos.setValidator(QtGui.QIntValidator(1,100000000))




	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Помощник по кредитованию"))
		self.label.setText(_translate("MainWindow", "Помощник по крдитованию"))
		self.credit_sum.setPlaceholderText(_translate("MainWindow", "Сумма в рублях"))
		self.credit_year.setPlaceholderText(_translate("MainWindow", "Cрок в годах"))
		self.label_2.setText(_translate("MainWindow", "Ставка:"))
		self.label_3.setText(_translate("MainWindow", "От 7.9%"))
		self.label_4.setText(_translate("MainWindow", "Платеж:"))
		self.credit_payment.setText(_translate("MainWindow", "0 ₽"))
		self.btn_credit.setText(_translate("MainWindow", "Подобрать кредит"))
		self.credit_banks.setText(_translate("MainWindow", "Подобрано банков: 0"))
		self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_credit), _translate("MainWindow", "Кредиты"))
		self.deposit_sum.setPlaceholderText(_translate("MainWindow", "Сумма в рублях"))
		self.deposit_year.setPlaceholderText(_translate("MainWindow", "Cрок в месяцах"))
		self.label_6.setText(_translate("MainWindow", "Ставка:"))
		self.label_7.setText(_translate("MainWindow", "До 10%"))
		self.label_8.setText(_translate("MainWindow", "Доход:"))
		self.deposit_payment.setText(_translate("MainWindow", "0 ₽"))
		self.btn_deposit.setText(_translate("MainWindow", "Подобрать вклад"))
		self.deposit_banks.setText(_translate("MainWindow", "Подобрано банков: 0"))
		self.tab_menu.setTabText(self.tab_menu.indexOf(self.tab_deposit), _translate("MainWindow", "Вклады"))
		self.mortgage_sum.setPlaceholderText(_translate("MainWindow", "Сумма в рублях"))
		self.mortgage_year.setPlaceholderText(_translate("MainWindow", "Cрок в годах"))
		self.label_10.setText(_translate("MainWindow", "Ставка:"))
		self.label_11.setText(_translate("MainWindow", "От 4.5%"))
		self.label_12.setText(_translate("MainWindow", "Платеж:"))
		self.label_13.setText(_translate("MainWindow", "0 ₽"))
		self.btn_mortgage.setText(_translate("MainWindow", "Подобрать ипотеку"))
		self.label_53.setText(_translate("MainWindow", "Сумма кредита:"))
		self.mortgage_sumKredita.setText(_translate("MainWindow", "10000000 ₽"))
		self.mortgage_vznos.setPlaceholderText(_translate("MainWindow", "Первоначальный взнос в рублях"))
		self.mortgage_banks.setText(_translate("MainWindow", "Подобрано банков: 0"))
		self.tab_menu.setTabText(self.tab_menu.indexOf(self.mortgage), _translate("MainWindow", "Ипотека"))


	
	def getCredit(self):
		try:
			summa = float(self.credit_sum.text())
			year = float(self.credit_year.text())
			stavka = float(7.9)
			# тут формла потом делаешь сет на лейбл с ценой ?
			month = year * 12
			r = stavka / 1200
			monthPayment = summa * ((r * ((1 + r) ** month))/(((1+r)**month) - 1))
			self.credit_payment.setText(str(int(monthPayment)) + " ₽")


			print(summa, year, monthPayment)
			return print(summa, year)
			
			
		except ValueError as e:
			pass
	


	def depFormula(self,stavka,summa,day):
		result = summa + ((summa * stavka * day)/(100*365))
		return result

	def getDep(self):
		try:
			summa = float(self.deposit_sum.text())
			month = float(self.deposit_year.text())
			day = month * 30
			if month < 6 and month > 0:
				stavka = float(10)
				self.label_7.setText(f"До {stavka}%")
				self.deposit_payment.setText(str(int(self.depFormula(stavka,summa,day)-summa)) + " ₽")
			elif month < 9:
				stavka = float(9)
				self.label_7.setText(f"До {stavka}%")
				self.deposit_payment.setText(str(int(self.depFormula(stavka,summa,day)-summa)) + " ₽")
			elif month < 24:
				stavka = float(8.5)
				self.label_7.setText(f"До {stavka}%")
				self.deposit_payment.setText(str(int(self.depFormula(stavka,summa,day)-summa)) + " ₽")
			elif month < 36:
				stavka = float(9.1)
				self.label_7.setText(f"До {stavka}%")
				self.deposit_payment.setText(str(int(self.depFormula(stavka,summa,day)-summa)) + " ₽")

			elif month < 48:
				stavka = float(10.1)
				self.label_7.setText(f"До {stavka}%")
				self.deposit_payment.setText(str(int(self.depFormula(stavka,summa,day)-summa)) + " ₽")

			else:
				stavka = float(9.25)
				self.label_7.setText(f"До {stavka}%")
				self.deposit_payment.setText(str(int(self.depFormula(stavka,summa,day)-summa)) + " ₽")
			# тут формла потом делаешь сет на лейбл с ценой ?
			print(summa, month)
			return print(summa, month)
			
		except ValueError as e:
			pass


	def getMortgage(self):
		try:
			summa = float(self.mortgage_sum.text())
			year = float(self.mortgage_year.text())
			vznos = float(self.mortgage_vznos.text())
			stavka = float(4.5)
			month = year * 12
			
			newSumma = summa - vznos
			self.mortgage_sumKredita.setText(f"{int(newSumma)} ₽")
			r = stavka / 1200
			monthPayment = newSumma * ((r * ((1 + r) ** month))/(((1+r)**month) - 1))
			self.label_13.setText(str(int(monthPayment)) + " ₽")
			print(summa, year,vznos)
			return print(summa, year,vznos)
			
		except ValueError as e:
			pass