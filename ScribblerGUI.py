'''download and import wxPython'''

try:
	import wx
except ImportError:
	raise ImportError, "The wxPython module is required to run this program."

class scribbler_wx(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.Show(True)
		sizer = wx.GridBagSizer()

		self.entry = wx.TextCtrl(self, -1, value=u"Enter text")
		sizer.add(self.entry, (0,0) (1,1), wx.EXPAND)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

		button = wx.Button(self, -1, label = "Process")
		sizer.add(button, (0,1))
		self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)
		
		self.label = wx.StaticText(self, -1, label=u"Output here")
		self.label.SetBackgroundColour(wx.BLACK)
		self.label.SetForegroundColour(wx.WHITE)
		sizer.Add(self.label,(1,0),(1,2),wx.EXPAND)
		
		sizer.AddGrowableCol(0)
		self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y)
		self.SetSizerAndFit(sizer)
		self.entry.setFocus()
		self.entry.SetSelection(-1,-1)

	def OnButtonClick(self,event):
		self.label.SetLabel(self.entry.GetValue() + "button clicked")
		self.entry.setFocus()
		self.entry.SetSelection(-1,-1)

	def OnPressEnter(self,event):
		self.label.SetLabel(self.entry.GetValue() + "pressed enter")
		self.entry.setFocus()
		self.entry.SetSelection(-1,-1)


if __name__ == "__main__":
	app = wx.App()
	frame = simpleapp_wx(None, -1, 'Scribbler Bot')
	app.MainLoop()
