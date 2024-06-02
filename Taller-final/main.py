import sys
from PyQt5.QtWidgets import QApplication
from controlador import Controller


def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
