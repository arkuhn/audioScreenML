# Add-on development first example
import globalPluginHandler
import tones # We want to hear beeps.
import api 
import ui
import treeInterceptorHandler
import textInfos
import scriptHandler
import time
import datetime
import os
import webbrowser

"""
CONFIGURE THE SAVE DIRECTORY
"""
save_dir = 'c:/nvda-textcopy/' 

months = {
	1: 'January',
	2: 'Februay',
	3: 'March',
	4: 'April',
	5: 'May',
	6: 'June',
	7: 'July',
	8: 'August',
	9: 'September',
	10: 'October',
	11: 'November',
	12: 'December' 
}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_saveClip(self, gesture):
		tones.beep(440, 500) # Beep a standard middle A for 1 second.
		try:
			text = api.getClipData()
		except TypeError:
			text = None
		if not text or not isinstance(text,basestring):
			ui.message("Clipboard has no text")
			return
		else:
			now = datetime.datetime.now()
			timestr = time.strftime("%H%M%S")
			filename = timestr + '.html'
			filepath = save_dir + months[now.month] + '_' + str(now.year) + '/' + str(now.day) + '/'
			if not os.path.exists(filepath):
				os.makedirs(filepath)
			with open(filepath + filename, "w") as text_file:
				text_file.write('<html>')
				text_file.write('<h1> Saved on: ' + months[now.month] + ' ' + str(now.day) + ', ' +  str(now.year) + '</h1>')
				text_file.write('<h2>')
				text_file.write(str(text))
				text_file.write('</h2>')
				text_file.write('</html>')
			webbrowser.open('file://' + (filepath + filename))
				
			

		
	
	__gestures={
		"kb:NVDA+A":"saveClip"
	}