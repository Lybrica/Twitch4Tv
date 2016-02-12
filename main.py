import os
import subprocess
from Tools.scripts.treesync import raw_input

url = "http://www.twitch.tv/" + raw_input("Enter stream: ")
cmd = 'livestreamer ' + url + 'best'


subprocess.call(['runas', '/user:Administrator', cmd])