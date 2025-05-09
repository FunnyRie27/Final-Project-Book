from functions import *

def main():
    application = QApplication([])
    window = Functions()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()