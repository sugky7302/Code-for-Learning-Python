# WxPython基礎指令

import wx


def write(event):
    print("button1 pressed...")


class Button:
    def __init__(self, parent, label="None", pos=(0, 0),
                 size=(5, 5), event=None):
        self.object = wx.Button(parent, -1, label=label, pos=pos, size=size)
        
        if event is not None:
            self.object.Bind(wx.EVT_BUTTON, event)


# 創建一個應用程式對象
app = wx.App()

# 創建一個視窗或框架對象
# wx.Frame(Parent, ID, title, pos(視窗位置), Size(視窗大小), Style(視窗右上角要添加的按鈕))
frame = wx.Frame(None, -1, title="測試", pos=(400, 120), size=(500, 335))

# 新增控件
background = wx.Panel(frame)
background.SetBackgroundColour("Red")

# 搜尋框
search_box = wx.TextCtrl(background, -1, value="Enter Name?",
                         pos=(5, 5), size=(210, 25))

# 按鈕
button1 = Button(background, label="search", pos=(225, 5),
                 size=(80, 25), event=write)

button2 = wx.Button(background, -1, label="button", pos=(315, 5), size=(80, 25))

# 文字框(橫豎都有拉條可以移動)
text_area = wx.TextCtrl(background, -1, pos=(5, 35), size=(390, 260),
                        style=wx.TE_MULTILINE | wx.HSCROLL)

# 靜態文字
static_text = wx.StaticText(background, -1, label="test", pos=(5, 35))

# Txt.SetFont(wx.Font(Size, Family(70-76), Style(90, 93, 94), Weight(90-92)))
static_text.SetFont(wx.Font(20, 71, 90, 91))

# 選擇框
# 兩者差別在combo box可以在框體內輸入文字，choice不行
ch = wx.Choice(background, -1, pos=(25, 95),
               choices=['Africa', 'America', 'Asia', 'Europe'])
combo_box = wx.ComboBox(background, -1, pos=(25, 135),
                        choices=['Africa', 'America', 'Asia', 'Europe'])

# 搜尋框佈局
search_layout = wx.BoxSizer()
search_layout.Add(search_box, proportion=1, flag=wx.EXPAND)
search_layout.Add(button1.object, proportion=0, flag=wx.LEFT, border=5)
search_layout.Add(button2, proportion=0, flag=wx.LEFT, border=5)

# 全部佈局
all_layout = wx.BoxSizer(wx.VERTICAL)
all_layout.Add(search_layout, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
all_layout.Add(text_area, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

# 設定佈局
# 如果只設定搜尋框佈局，文字框會被搜尋框覆蓋
background.SetSizer(all_layout)

# 顯示視窗
frame.Show()

# 執行
# 這是一個無限循環，之後的動作必須等到視窗關閉才會執行
app.MainLoop()

print("Done")