import sys
from PySide6 import QtWidgets as Qt
from PySide6 import QtCore, QtGui

class BulletinBoard(Qt.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: black; color: white;")  # Set background color for the entire widget
        
        main_layout = Qt.QHBoxLayout(self)

        # Create the first column layout
        column1_layout = Qt.QVBoxLayout()

        # Add buttons to the first column
        button1 = Qt.QPushButton("Button 1A")
        button2 = Qt.QPushButton("Button 2A")
        column1_layout.addWidget(button1)
        column1_layout.addWidget(button2)

        # Create the second column layout
        column2_layout = Qt.QVBoxLayout()

        # Add buttons to the second column
        button3 = Qt.QPushButton("Button 1B")
        button4 = Qt.QPushButton("Button 2B")
        column2_layout.addWidget(button3)
        column2_layout.addWidget(button4)

        # Add the two column layouts to the main layout
        main_layout.addLayout(column1_layout)
        main_layout.addLayout(column2_layout)
