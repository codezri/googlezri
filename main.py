import clipboard
import keyboard
import os
import time
import urllib.parse
import subprocess


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
            'google-chrome -new-tab --no-sandbox https://www.google.com/search?q=' + selectedText)

    def listen(self):
        print('Listening to ' + self.hotkey)
        keyboard.wait()


gz = GoogleZri()
gz.registerHotKey('alt+g')
gz.listen()