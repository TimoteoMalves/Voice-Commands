import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def start_button_clicked():
    print("oba")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Simple Frontend')
start_button = QPushButton('Start', window)
start_button.clicked.connect(start_button_clicked)
start_button.setGeometry(50, 50, 100, 50)
window.show()
sys.exit(app.exec_())
