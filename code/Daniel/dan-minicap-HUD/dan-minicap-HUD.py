#---------------------------------
# PDX Code Guild: HB3
# Mini Capstone: Heads-Up Display (HUD) Overlay
# Author: Daniel Smith
# Date: 2022.12.13
#---------------------------------

# HUD Overlay Project
# Idea is to start with a transparent window,
# then build visible elements inside of it,
# and connect those elements to sensor data on the backend.

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)

# Create main window
window =  QMainWindow()

window.setWindowOpacity(0.3)
window.setWindowTitle("Our first MainWindow App!")

# Create button
button = QPushButton()
button.setText("Press Me")
button.clicked.connect(app.quit) # When clicked, close app.

# Center the button
window.setCentralWidget(button)

# Run the application
window.show()
# window.showFullScreen() # setWindowOpacity() doesn't seem to work on fullscreen...
sys.exit(app.exec())
# app.exec()

### Issues:
### Elements within window are transparent same as window... Possibly use a custom window transparent paint event?
### setWindowOpacity() doesn't seem to work w/ showFullScreen()... Possibly use a custom window transparent paint event?