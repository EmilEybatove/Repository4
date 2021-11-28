import sys
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = list(cur.execute(f"""SELECT * FROM info""").fetchall())
        con.close()
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
