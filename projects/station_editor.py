# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class StationEditor
###########################################################################

class StationEditor ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"站點劇本編輯器", pos = wx.DefaultPosition, size = wx.Size( 500,331 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )

		all_layout = wx.BoxSizer( wx.HORIZONTAL )

		station_layout = wx.BoxSizer( wx.VERTICAL )

		self.station_text = wx.StaticText( self, wx.ID_ANY, u"站點列表", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.station_text.Wrap( -1 )

		self.station_text.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		station_layout.Add( self.station_text, 0, wx.ALL, 5 )

		listChoices = []
		self.list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,220 ), listChoices, 0 )
		station_layout.Add( self.list, 0, 0, 5 )

		button_layout = wx.BoxSizer( wx.HORIZONTAL )

		self.add = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		self.add.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.add.SetForegroundColour( wx.Colour( 0, 189, 0 ) )

		button_layout.Add( self.add, 0, 0, 5 )

		self.delete = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		self.delete.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.delete.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		button_layout.Add( self.delete, 0, 0, 5 )


		station_layout.Add( button_layout, 0, 0, 5 )


		all_layout.Add( station_layout, 1, wx.EXPAND, 5 )

		setting_layout = wx.BoxSizer( wx.VERTICAL )

		self.type_text = wx.StaticText( self, wx.ID_ANY, u"類型", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.type_text.Wrap( -1 )

		self.type_text.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		setting_layout.Add( self.type_text, 0, wx.ALL, 5 )

		type_choiceChoices = [ u"去程點", u"回程點", u"雙向點" ]
		self.type_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, type_choiceChoices, 0 )
		self.type_choice.SetSelection( 0 )
		setting_layout.Add( self.type_choice, 0, wx.ALL, 5 )

		self.laser_text = wx.StaticText( self, wx.ID_ANY, u"雷射", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.laser_text.Wrap( -1 )

		self.laser_text.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		setting_layout.Add( self.laser_text, 0, wx.ALL, 5 )

		laser_choiceChoices = [ u"開", u"關" ]
		self.laser_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, laser_choiceChoices, 0 )
		self.laser_choice.SetSelection( 0 )
		setting_layout.Add( self.laser_choice, 0, wx.ALL, 5 )

		self.ultrasonic_text = wx.StaticText( self, wx.ID_ANY, u"超聲波", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ultrasonic_text.Wrap( -1 )

		self.ultrasonic_text.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		setting_layout.Add( self.ultrasonic_text, 0, wx.ALL, 5 )

		ultrasonic_layout = wx.GridSizer( 4, 2, 0, 0 )

		self.checkBox0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkBox0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		ultrasonic_layout.Add( self.checkBox0, 0, wx.ALL, 5 )

		self.checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.checkBox4, 0, wx.ALL, 5 )

		self.checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.checkBox1, 0, wx.ALL, 5 )

		self.checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.checkBox6, 0, wx.ALL, 5 )

		self.checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.checkBox3, 0, wx.ALL, 5 )

		self.checkBox7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		ultrasonic_layout.Add( self.checkBox7, 0, wx.ALL, 5 )


		setting_layout.Add( ultrasonic_layout, 1, 0, 5 )


		all_layout.Add( setting_layout, 1, wx.EXPAND, 5 )

		action_layout = wx.BoxSizer( wx.VERTICAL )

		self.action = wx.StaticText( self, wx.ID_ANY, u"動作", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.action.Wrap( -1 )

		self.action.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		action_layout.Add( self.action, 0, wx.ALL, 5 )

		action_listChoices = []
		self.action_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,220 ), action_listChoices, 0 )
		action_layout.Add( self.action_list, 0, 0, 5 )

		button_layout1 = wx.BoxSizer( wx.HORIZONTAL )

		self.add1 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		self.add1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.add1.SetForegroundColour( wx.Colour( 0, 189, 0 ) )

		button_layout1.Add( self.add1, 0, 0, 5 )

		self.delete1 = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		self.delete1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.delete1.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		button_layout1.Add( self.delete1, 0, 0, 5 )


		action_layout.Add( button_layout1, 1, wx.EXPAND, 5 )


		all_layout.Add( action_layout, 1, wx.EXPAND, 5 )


		self.SetSizer( all_layout )
		self.Layout()
		self.menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.load_menuitem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"開啟檔案..."+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.load_menuitem )

		self.save_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"儲存"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.save_menuItem )

		self.file_menu.AppendSeparator()

		self.exit_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"結束", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.exit_menuItem )

		self.menubar.Append( self.file_menu, u"檔案(F)" )

		self.help_menu = wx.Menu()
		self.about_menuItem = wx.MenuItem( self.help_menu, wx.ID_ANY, u"關於", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.about_menuItem )

		self.menubar.Append( self.help_menu, u"說明(H)" )

		self.SetMenuBar( self.menubar )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

app = wx.App()
frame = StationEditor(None)
frame.Show()
app.MainLoop()