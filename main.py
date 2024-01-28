import sys
from PySide6 import QtWidgets as Qt
<<<<<<< HEAD
from PySide6 import QtCore, QtGui
from BBoard import BulletinBoard
=======
from PySide6 import QtCore
>>>>>>> 514d8c785ac280bbd260e0c8e2a32cbf69e62287

class MainWindow(Qt.QWidget):
    def __init__(self):
        super().__init__()

        Title = self.text = Qt.QLabel("PushPin", alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)


        MainLayout = Qt.QHBoxLayout(self)
        Content = Qt.QVBoxLayout(self)

        self.nav_bar = NavBar()
        MainLayout.addWidget(self.nav_bar, 20)  # Adjusted the stretch factor
        MainLayout.addLayout(Content)
        Content.addWidget(Title)
<<<<<<< HEAD
        self.bulletin_board = BulletinBoard()
        Content.addWidget(self.bulletin_board)
=======

>>>>>>> 514d8c785ac280bbd260e0c8e2a32cbf69e62287
        self.showMaximized()

    def resizeEvent(self, event):
        # Update the width of the NavBar when the main window is resized
        self.nav_bar.update_width(self.width())
        super().resizeEvent(event)

class NavBar(Qt.QWidget):
    def __init__(self):
        super().__init__()
        Layout = self.layout = Qt.QVBoxLayout(self)

<<<<<<< HEAD
=======
        # Placeholder labels for demonstration
        labels = ["Bulletin Board", "BOMs", "Message", "Contracts", "Marketplace", "Contact Us"]
        for label_text in labels:
            Layout.addWidget(Qt.QLabel(label_text, alignment=QtCore.Qt.AlignCenter))

    def update_width(self, width):
        # Update the width of the NavBar dynamically
        self.setFixedWidth(width * 0.2)

>>>>>>> 514d8c785ac280bbd260e0c8e2a32cbf69e62287
if __name__ == "__main__":
    app = Qt.QApplication([])

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())