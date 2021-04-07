import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import win32gui
import win32con

INTERVAL_MS = 50


class MainWindow(QMainWindow):
    def __init__(self, hwnd):
        super().__init__()

        self.setWindowTitle('Valheim AutoClick')
        self.setFixedSize(300, 180)
        cw = QWidget()

        self.hwnd = hwnd

        self.up = 200
        self.down = 200
        self.elapsed = 0
        self.timeout = 0
        self.lbutton_up = True
        self.foreground = False

        self.timer = QTimer()
        self.timer.setInterval(INTERVAL_MS)
        self.timer.timeout.connect(self.tick)

        label_up = QLabel('UP interval (ms)')
        self.edit_up = QLineEdit(str(self.up))
        self.edit_up.setValidator(QIntValidator())
        self.edit_up.textChanged.connect(self.up_changed)

        label_down = QLabel('DOWN interval (ms)')
        self.edit_down = QLineEdit(str(self.down))
        self.edit_down.setValidator(QIntValidator())
        self.edit_down.textChanged.connect(self.down_changed)

        font = QFont()
        font.setPointSize(20)
        font.setBold(True)

        self.btn = QPushButton('toggle', cw)
        self.btn.setFixedSize(150, 150)
        self.btn.setCheckable(True)
        self.btn.setFont(font)
        self.btn.setStyleSheet(
            "QPushButton { background-color: red; }"
            "QPushButton:checked { background-color: green; border: none; }"
        )
        self.btn.toggled.connect(self.on_toggle)
        self.on_toggle(False)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(label_up, alignment=Qt.AlignBottom)
        vbox.addWidget(self.edit_up, alignment=Qt.AlignTop)
        vbox.addWidget(label_down, alignment=Qt.AlignBottom)
        vbox.addWidget(self.edit_down, alignment=Qt.AlignTop)
        hbox.addLayout(vbox)
        hbox.addWidget(self.btn)
        cw.setLayout(hbox)
        self.setCentralWidget(cw)

    def update_startable(self):
        self.btn.setEnabled(self.up >= 50 and self.down >= 50)

    def up_changed(self):
        try:
            self.up = int(self.edit_up.text())
        except:
            if self.edit_up.text() == '':
                self.up = 0
            else:
                self.edit_up.setText(str(self.up))

        self.update_startable()

    def down_changed(self):
        try:
            self.down = int(self.edit_down.text())
        except:
            if self.edit_down.text() == '':
                self.down = 0
            else:
                self.edit_down.setText(str(self.down))
        self.update_startable()

    def reset(self):
        self.elapsed = 0
        self.timeout = 0
        self.lbutton_up = True
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, 0)

    def on_toggle(self, state):
        self.edit_down.setDisabled(state)
        self.edit_up.setDisabled(state)

        if state:
            self.btn.setText("ON")
            self.timer.start()

        else:
            self.btn.setText("OFF")
            self.timer.stop()
            self.reset()

    def tick(self):
        if self.hwnd == win32gui.GetForegroundWindow():
            if not self.foreground:
                self.reset()
            self.foreground = True
            return

        self.foreground = False

        self.elapsed += INTERVAL_MS
        if self.elapsed < self.timeout:
            return

        if self.lbutton_up:
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
            self.timeout = self.down
        else:
            win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, 0)
            self.timeout = self.up

        self.lbutton_up = not self.lbutton_up
        self.elapsed = 0


def main():
    app = QApplication(sys.argv)

    hwnd = win32gui.FindWindow(None, 'Valheim')
    if hwnd is None:
        error_dialog = QErrorMessage()
        error_dialog.showMessage('Launch Valheim first!')
        sys.exit(app.exec_())

    ex = MainWindow(hwnd)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
