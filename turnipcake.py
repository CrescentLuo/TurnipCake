import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Hello, Raspberry Pi!")
    window.setGeometry(100, 100, 280, 80)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
