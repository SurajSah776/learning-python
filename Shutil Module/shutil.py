# Shutil Module
# Shell-Utilities Module

import shutil

# Copy File
shutil.copy('h.html', 'copiedHTML.html')
shutil.copy2('main.py', 'main2.py')

# Copy Directories
shutil.copytree('folder', 'copyedFolder')

# Move File
shutil.move('h.html', '/New/h.txt')

# Remove Directories
shutil.rmtree('folder')
