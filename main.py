import clipboard
import keyboard
import os
import time
import urllib.parse
import subprocess
from art import *


class GoogleZri:
    GOOGLE_URL = 'https://www.google.com/search?q='
    hotkey = ''

    def registerHotKey(self, hotkey):
        self.hotkey = hotkey
        keyboard.add_hotkey(self.hotkey, self.hotKeyCallback)

    def hotKeyCallback(self):
        selectedText = subprocess.getoutput('xclip -o')
        selectedText = urllib.parse.quote_plus(selectedText)
        os.system(
            'sudo -u $(logname) google-chrome -new-tab --no-sandbox https://www.google.com/search?q=' + selectedText + " &")

    def listen(self):
        tprint('GoogleZri')
        print('Press ' + self.hotkey + ' to Google any selected text.')
        keyboard.wait()


gz = GoogleZri()
gz.registerHotKey('ctrl+f2')
gz.listen()
