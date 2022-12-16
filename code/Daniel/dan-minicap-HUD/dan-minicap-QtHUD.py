#---------------------------------
# PDX Code Guild: HB3
# Mini Capstone: Heads-Up Display (HUD) Overlay
# Author: Daniel Smith
# Date: 2022.12.13
#---------------------------------

# HUD Overlay Project
# Idea is to begin with a transparent window,
# then build visible/opaque elements inside of it,
# and format and connect those elements to sensor data on the backend.

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)
# app = QApplication([])

# Create main window
window1 = QMainWindow()
widget1 = QWidget()

window1.setWindowTitle("HUD MainWindow1")
window1.setWindowOpacity(0.4)
# window1.setStyleSheet("background-color: transparent")

widget1.setWindowTitle("HUD Widget1")
widget1.setWindowOpacity(0.7)
# widget1.setStyleSheet("background-color: transparent")

# Create button
button1 = QPushButton()
button1.setText("Push to Exit")
button1.setStyleSheet("background-color: green")
button1.clicked.connect(app.quit) # When pushed/clicked, exit app.

button2 = QPushButton(widget1)
button2.setText("Exit")

# Position the buttons
window1.setCentralWidget(button1)
button2.move(64,32)

# Run the application
widget1.show()
window1.show()
# window1.showFullScreen() # setWindowOpacity() doesn't seem to work on fullscreen...
sys.exit(app.exec())
# app.exec()

### Issues:
### Elements within window are transparent same as window... Possibly use a custom window transparent paint event?
### setWindowOpacity() doesn't seem to work w/ showFullScreen()... Possibly use a custom window transparent paint event?