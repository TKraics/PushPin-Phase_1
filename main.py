import sys
from PySide6 import QtWidgets as Qt
from PySide6 import QtCore, QtGui
from BBoard import BulletinBoard

class MainWindow(Qt.QWidget):
    def __init__(self):
        super().__init__()

        Title = self.text = Qt.QLabel("PushPin",
                              alignment = QtCore.Qt.AlignCenter)
        
        MainLayout = Qt.QHBoxLayout(self)
        Content = Qt.QVBoxLayout(self)

        MainLayout.addWidget(NavBar())
        MainLayout.addLayout(Content)
        Content.addWidget(Title)
        self.bulletin_board = BulletinBoard()
        Content.addWidget(self.bulletin_board)
        self.showMaximized()



class NavBar(Qt.QWidget):
    def __init__(self):
        super().__init__()

        Layout = self.layout = Qt.QVBoxLayout(self)
        Layout.addWidget(Qt.QLabel("Bulletin Board",
                                 alignment = QtCore.Qt.AlignCenter))
        Layout.addWidget(Qt.QLabel("BOMs",
                                 alignment = QtCore.Qt.AlignCenter))
        Layout.addWidget(Qt.QLabel("Message",
                                 alignment = QtCore.Qt.AlignCenter))
        Layout.addWidget(Qt.QLabel("Contracts",
                                 alignment = QtCore.Qt.AlignCenter))
        Layout.addWidget(Qt.QLabel("Marketplace",
                                 alignment = QtCore.Qt.AlignCenter))
        Layout.addWidget(Qt.QLabel("Contact Us",
                                 alignment = QtCore.Qt.AlignCenter))

if __name__ == "__main__":
    app = Qt.QApplication([])

    widget = MainWindow()

    widget.show()

    sys.exit(app.exec())