#---------------------------------
# PDX Code Guild: HB3
# Mini Capstone: Heads-Up Display (HUD) Overlay
# Author: Daniel Smith
# Date: 2022.12.13
#---------------------------------

# HUD Overlay Project
# Idea is to begin with a transparent window,
# then build visible/opaque elements inside of it,
# and connect those elements to sensor data on the backend.

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)

# Create main window
window1 =  QMainWindow()

window1.setWindowOpacity(0.3)
window1.setWindowTitle("First HUD MainWindow")

# Create button
button1 = QPushButton()
button1.setText("Press Me to Close Window")
button1.clicked.connect(app.quit) # When clicked, close app.

# Center the button
window1.setCentralWidget(button1)

# Run the application
window1.show()
# window1.showFullScreen() # setWindowOpacity() doesn't seem to work on fullscreen...
sys.exit(app.exec())
# app.exec()

### Issues:
### Elements within window are transparent same as window... Possibly use a custom window transparent paint event?
### setWindowOpacity() doesn't seem to work w/ showFullScreen()... Possibly use a custom window transparent paint event?