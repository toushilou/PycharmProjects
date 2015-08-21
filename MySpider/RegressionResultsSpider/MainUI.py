__author__ = 'qyuan'
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class contentWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, parent = None)
        self.resize(400, 300)
        self.setWindowTitle('Content')
        self.setWindowIcon(QtGui.QIcon('./icons/telenav.png'))

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(400, 300)
        self.setWindowTitle('Regression Analyst')
        self.setWindowIcon(QtGui.QIcon('./icons/telenav.png'))
        check_content = QtGui.QPushButton('Content', self)
        check_content.setGeometry(10, 30, 60, 35)
        # exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(QtGui.qApp.quit)
        self.statusBar().showMessage('Ready')
        self.connect(check_content, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT("newWindow()"))
        self.center()
        # menubar = self.menuBar()
        # file = menubar.addMenu('&File')
        # file.addAction(exitAction)
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
        (screen.height() - size.height()) / 2)
    @QtCore.pyqtSlot()
    def newWindow(self):
        self.cw = contentWindow()
        self.cw.show()

app = QtGui.QApplication(sys.argv)
qb = MainWindow()
qb.show()
sys.exit(app.exec_())