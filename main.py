import star
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class StarGarage(QtWidgets.QMainWindow):
	
	def __init__(self):
		
		super(StarGarage,self).__init__()
		uic.loadUi('star_garage.ui',self)
		self.intiUI()
		
	def initUI(self):
		
		
	def run(self):
		self.mainwindow.mainloop()
	
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = StarGarage()
	window.show()
	sys.exit(app.exec_())