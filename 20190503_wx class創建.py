# WxPython使用class創建視窗

import os
import wx
import json


class Config:
    def __init__(self, path):
        # dir_path = os.path.abspath('.')
        # self.path = os.path.join(dir_path, path)
        self.path = path
        self.file = open(self.path, 'r')
        self.data = json.load(self.file)
        self.close()

    def __getitem__(self, index):
        try:
            return self.data[index]
        except Exception as e:
            return False

    def __setitem__(self, index, value) :
        try:
            self.data[index] = value
        except Exception as e:
            return False

    def write(self):
        self.close()
        self.file = open(self.path, 'w')
        
        json.dump(self.data, self.file, sort_keys=False, indent=4, separators=(',', ' : '))
        
        self.close()
        self.file = open(self.path, 'r')

    def close(self):
        self.file.close()


class Choice:
    def __init__(self, parent, choices=[]):
        self.object = wx.Choice(parent, choices=choices)
        self.object.SetSelection(0)

    def SetSelection(self, index):
        self.object.SetSelection(index)

    def GetSelection(self):
        return self.object.GetSelection()

    def GetSelectionString(self):
        return self.object.GetString(self.GetSelection())


class ListBox:
    def __init__(self, parent, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 choices=[], event=None, event_handler=None):
        self.object = wx.ListBox(parent, pos=pos, size=size, choices=choices)

        if event is not None:
            self.object.Bind(event, event_handler)

    def Append(self, data):
        self.object.Append(data)

    def Clear(self):
        self.object.Clear()

    def GetSelectionString(self):
        return self.object.GetString(self.object.GetSelection())


class StaticText:
    def __init__(self, parent, label="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, font_size=12, style=0):
        self.object = wx.StaticText(parent, label=label, pos=pos, 
                                    size=size, style=style)
        self.object.Wrap(-1)
        self.object.SetFont(wx.Font(font_size, wx.FONTFAMILY_DEFAULT,
                                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                                    False, wx.EmptyString))


class Button:
    def __init__(self, parent, label="", pos=(0, 0), size=(5, 5),
                 font_size=12, color=(0, 0, 0), event_handler=None):
        self.object = wx.Button(parent, wx.ID_ANY, label=label, pos=pos,
                                size=size)
        self.object.SetFont(wx.Font(font_size, wx.FONTFAMILY_DEFAULT,
                                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                                    False, wx.EmptyString))
        self.object.SetForegroundColour(wx.Colour(*color))

        if event_handler is not None:
            self.object.Bind(wx.EVT_BUTTON, event_handler)


#             此為要繼承的父類
class StationEditor(wx.Frame):
    # 這是不用傳參的建構方法
    # def __init__(self) :
    #     wx.Frame.__init__(self, None)

    def __init__(self, *args, **kwargs):
        # 要調用父類的建構函數才能創建視窗
        # 或是使用super(StationEditor, self).__init__(*args, **kwargs)
        wx.Frame.__init__(self, *args, **kwargs)

        self.SetBackgroundColour(wx.Colour(255, 128, 0))

        self.file = ""

        self.all_layout = wx.BoxSizer()
        self.create_station_list()

        self.create_menu_bar()

        self.setting_layout = wx.BoxSizer(wx.VERTICAL)
        self.create_setting_list()
        
        self.collide_layout = wx.BoxSizer(wx.VERTICAL)
        self.create_laser_list()
        self.create_ultrasonic_option()

        self.create_action_list()

        self.collide_layout1 = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(self.all_layout)
        self.Layout()

    def create_station_list(self):
        self.station_layout = wx.BoxSizer(wx.VERTICAL)

        station_text = StaticText(self, label="站點列表", font_size=14,
                                  style=wx.EXPAND | wx.ALIGN_LEFT)
        self.station_layout.Add(station_text.object, 2, wx.EXPAND, 0)

        self.list_choice = ListBox(self, size=(140, 220))
        self.station_layout.Add(self.list_choice.object, 1, wx.EXPAND, 15)

        self.button_layout = wx.BoxSizer()
        add_button = Button(self, label="+", size=(20, 20), color=(0, 189, 0))
        self.button_layout.Add(add_button.object, 0, 0, 5)

        delete_button = Button(self, label="-", size=(20, 20), color=(255, 0, 0))
        self.button_layout.Add(delete_button.object, 0, 0, 5)

        self.station_layout.Add(self.button_layout, 0, 0, 5)
        self.all_layout.Add(self.station_layout, 1, wx.EXPAND, 15)

    def menu_data(self):
        # 格式：選單數據目前是(標籤, (項目))，其中項目的組成為：標籤、描述文字、事件處理器、可選的kind
        # 標籤長度為2，項目的長度為3或4
        # 如果只有一個項目，不管加多少括號，python都視為一個單括號的元組
        return [
            ("檔案(F)", (  # 一級選單
                    ("開啟檔案...\tCtrl+O", "開啟json檔案", self.on_load),  # 二級選單
                    ("儲存\tCtrl+S", "儲存json檔案", self.on_save),
                    ("", "", ""),
                    ("結束", "關閉視窗", self.on_exit))),
            ("說明(H)", (("關於", "顯示程式相關資訊", self.on_about)))
        ]

    def create_menu_bar(self):
        # 創建選單條
        menu_bar = wx.MenuBar()
        
        # 讀取選單層級架構
        for menu in self.menu_data():
            menu_label = menu[0]
            menu_items = menu[1]
            menu_bar.Append(self.create_menu(menu_items), menu_label)

        self.SetMenuBar(menu_bar)
    
    def create_menu(self, menu_items):
        menu = wx.Menu()
        
        # 只有單一項目就直接創建
        if type(menu_items[0]) == str:
            self.create_menu_item(menu, *menu_items)
            return menu

        for item in menu_items:
            # 檢查長度，如果內含子選單，item長度會為2
            if len(item) == 2:
                label = item[0]

                # 遞迴創建
                sub_menu = self.create_menu(item[1])
                menu.AppendSubMenu(sub_menu, label)
            else:
                self.create_menu_item(menu, *item)

        return menu

    def create_menu_item(self, menu, label, status, event_handler,
                         kind=wx.ITEM_NORMAL):
        # 處理分隔符
        if not label:
            menu.AppendSeparator()
            return 

        menu_item = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, event_handler, menu_item)

    def on_save(self, event):
        print("unwritten")

    def on_load(self, event):
        file_wildcard = "json files(*.json)|*.json|All files(*.*)|*.*"
        dialog = wx.FileDialog(self, "Open json file...",
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
                               wildcard=file_wildcard)

        if dialog.ShowModal() == wx.ID_OK:
            self.file = Config(dialog.GetPath())
            
            # 清空站點列表
            self.list_choice.Clear()

            # 讀取站點
            for station_name in self.file.data:
                self.list_choice.Append(station_name)

        dialog.Destroy()

    def on_exit(self, event):
        self.Close(True)

    def on_about(self, event):
        title = "站點劇本編輯器"
        msg = "版本: 1.0.0"
        wx.MessageBox(title + "\n\n\n" + msg,
                      caption="站點劇本編輯器",
                      style=wx.OK | wx.ICON_INFORMATION)

    def create_setting_list(self):
        type_text = StaticText(self, label="類型")
        self.setting_layout.Add(type_text.object, 0, wx.ALL, 5)

        self.type_list = Choice(self, choices=["去程點", "回程點", "雙向點"])
        self.setting_layout.Add(self.type_list.object, 0, wx.ALL, 5)

        route_text = StaticText(self, label="路線")
        self.setting_layout.Add(route_text.object, 0, wx.ALL, 5)

        self.route_list = Choice(self, choices=["去程", "回程"])
        self.setting_layout.Add(self.route_list.object, 0, wx.ALL, 5)

        load_route_button = Button(self, label="讀取", size=(50, 30),
                                   event_handler=self.on_load_route)
        self.setting_layout.Add(load_route_button.object, 0, wx.ALL, 5)

        self.all_layout.Add(self.setting_layout, 1, wx.EXPAND, 5)

    def on_load_route(self, event):
        index = ""
        try:
            station = self.list_choice.GetSelectionString()
        except Exception as e:
            return

        # 確認route_list是選哪一個
        if self.route_list.GetSelection() == 0:
            index = "go"
        else:
            index = "back"

        # 讀取雷射，有讀到表示有雷射，沒讀到表示沒有雷射
        try:
            laser = self.file[station][index]["laser"]
            self.laser_list.SetSelection(0)
        except Exception as e:
            self.laser_list.SetSelection(1)

        # 清空超聲波的記號
        for box in self.ultrasonic_box:
            box.SetValue(False)

        # 讀取超聲波，有讀到才去設定checkbox
        try:
            ultrasonic = self.file[station][index]["ultrasonic"]
            for i in ultrasonic:
                self.ultrasonic_box[i].SetValue(True)
        except Exception as e:
            pass

        # 讀取動作列表
        self.action_choice.Clear()
        action_order = self.file[station][index]["action"]
        print(type(action_order))
        for action in action_order:
            self.action_choice.Append(str(action))

    def create_laser_list(self):
        laser_text = StaticText(self, label="雷射")
        self.collide_layout.Add(laser_text.object, 0, wx.ALL, 5)

        self.laser_list = Choice(self, choices=["無", "開", "關"])
        self.collide_layout.Add(self.laser_list.object, 0, wx.ALL, 5)

    def create_ultrasonic_option(self):
        ultrasonic_text = StaticText(self, label="超聲波")
        self.collide_layout.Add(ultrasonic_text.object, 0, wx.ALL, 5)

        self.ultrasonic_layout = wx.GridSizer(4, 2, 0, 0)

        self.ultrasonic_box = []
        for i in range(8):
            check_box = wx.CheckBox(self, label=str(i))
            check_box.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),
                                      wx.FONTFAMILY_DEFAULT,
                                      wx.FONTSTYLE_NORMAL,
                                      wx.FONTWEIGHT_NORMAL,
                                      False,
                                      wx.EmptyString))
            self.ultrasonic_box.append(check_box)
            self.ultrasonic_layout.Add(check_box, 0, wx.ALL, 5)

        self.collide_layout.Add(self.ultrasonic_layout, 1, 0, 5)
        self.all_layout.Add(self.collide_layout, 1, wx.EXPAND, 5)

    def create_action_list(self):
        self.action_layout = wx.BoxSizer(wx.VERTICAL)

        action_text = StaticText(self, label="動作", font_size=14)
        self.action_layout.Add(action_text.object, 0, wx.ALL, 5)

        self.action_choice = ListBox(self, size=(140, 220))
        self.action_layout.Add(self.action_choice.object, 0, 0, 5)

        self.button_layout1 = wx.BoxSizer()
        add_button = Button(self, label="+", size=(20, 20), color=(0, 189, 0))
        self.button_layout1.Add(add_button.object, 0, 0, 5)

        delete_button = Button(self, label="-", size=(20, 20), color=(255, 0, 0))
        self.button_layout1.Add(delete_button.object, 0, 0, 5)

        up_button = Button(self, label="↑", size=(20, 20))
        self.button_layout1.Add(up_button.object, 0, 0, 5)

        down_button = Button(self, label="↓", size=(20, 20))
        self.button_layout1.Add(down_button.object, 0, 0, 5)

        self.action_layout.Add(self.button_layout1, 0, 0, 5)
        self.all_layout.Add(self.action_layout, 1, wx.EXPAND, 5)


if __name__ == "__main__":
    app = wx.App()
    frame = StationEditor(None, title="站點劇本編輯器", size=(500, 331))
    frame.Show()
    app.MainLoop()