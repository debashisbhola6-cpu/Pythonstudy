import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class Clock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setFont(QFont("DejaVu Sans", 65, QFont.Bold))

        self.label.setStyleSheet("""
            QLabel {
                color: white;
                background: transparent;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.resize(500, 180)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):
        now = QDateTime.currentDateTime()

        time = now.toString("hh:mm:ss AP")
        day = now.toString("dddd")
        date = now.toString("dd MMMM yyyy")

        self.label.setText(
            f"{time}\n"
            f"{day}\n"
            f"{date}"
        )

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            window = self.windowHandle()
            if window:
                window.startSystemMove()

app = QApplication(sys.argv)

clock = Clock()
clock.show()

sys.exit(app.exec_())
