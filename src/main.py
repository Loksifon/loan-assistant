from PyQt6 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	app.exec()

