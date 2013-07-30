#------------------------------------Close All But This----------------------
# Author: Avinash Agrawal 
# Email : avinash8526@gmail.com
# Version : 1.0
#----------------------------------------------------------------------------
import sublime, sublime_plugin

class cabtCommand(sublime_plugin.WindowCommand):
	pjr = lambda self,x:x.id()	
	def run(self):
		print "hello"
		allviews = self.window.views()
		cview = self.window.active_view()
		name = self.pjr(cview)
		self.tabbandkaro(name,allviews)		
	 
	def tabbandkaro(self,name,allviews):		
		for t,v in enumerate(allviews):
			if v.id() != name:
				self.window.focus_view(v)
				self.window.run_command('close_file')
			

				