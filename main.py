from PyQt5.QtWidgets import QApplication
import sys
import contract
import time

def main():
    app = QApplication([])
    contract.contract(app)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()