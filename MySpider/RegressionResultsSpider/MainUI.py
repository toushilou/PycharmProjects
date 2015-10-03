__author__ = 'qyuan'
import sys
import os.path
from PyQt4 import QtGui
from PyQt4 import QtCore

# class contentRulesWindow(QtGui.QWidget):
#     def __init__(self):


class contentWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, parent = None)
        self.resize(600, 500)
        choose_location = QtGui.QPushButton('open', self)
        choose_location.setGeometry(10, 30, 60, 35)
        self.connect(choose_location, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT("OpenFileLocation()"))
        self.setWindowTitle('Content')
        self.setWindowIcon(QtGui.QIcon('./icons/telenav.png'))
    @QtCore.pyqtSlot()
    def OpenFileLocation(self):
        filenames = QtGui.QFileDialog.getOpenFileNames(self, 'Select the report files which you want to compare:', './')
        # nameList = QtCore.QStringList([lambda x: x.split(os.sep)[-1]])
        self.filenames = filenames
        # go_button.setGeometry(10, 400, 60, 35)
        # go_button.show()
        self.fileList = QtGui.QListWidget(parent = self)
        self.resultList = QtGui.QListWidget(parent = self)
        for x in filenames:
            self.fileList.addItem(x.split(os.sep)[-1])

        self.fileList.setGeometry(10,100, 240, 200)
        # fileList.show()

        btn_add = QtGui.QPushButton('->')
        btn_remove = QtGui.QPushButton('<-')
        btn_edit = QtGui.QPushButton('&Edit rules...')
        btn_go = QtGui.QPushButton('&Go')
        btn_close = QtGui.QPushButton('&Close')
        self.connect(btn_add, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT("add()"))
        self.connect(btn_remove, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT("remove()"))

        v_box = QtGui.QVBoxLayout()
        v_box.addWidget(btn_add)
        v_box.addWidget(btn_remove)
        v_box.addWidget(btn_edit)
        v_box.addWidget(btn_go)
        v_box.addStretch(1)
        v_box.addWidget(btn_close)
        h_box = QtGui.QHBoxLayout()
        h_box.addWidget(self.fileList)
        h_box.addLayout(v_box)
        h_box.addWidget(self.resultList)

        box = QtGui.QVBoxLayout()
        box.addLayout(h_box)
        self.setLayout(box)

    @QtCore.pyqtSlot()
    def add(self):
        currentRow = self.fileList.currentRow()
        file = self.fileList.takeItem(currentRow)
        self.resultList.addItem(file)
        self.fileList.takeItem(self.fileList.currentRow())
    @QtCore.pyqtSlot()
    def remove(self):
        currentRow = self.resultList.currentRow()
        file = self.resultList.takeItem(currentRow)
        self.fileList.addItem(file)
        self.resultList.takeItem(self.resultList.currentRow())


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