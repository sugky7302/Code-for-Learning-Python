#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: lingyue.wkl
#desc: use to read ini
#---------------------
#2012-02-18 created
#2012-09-02 changed for class support
#---------------------
import sys,os,time
import configparser

class Config :
    def __init__(self, path) :
        # 讀取路徑
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(dir_path, path)

        self.file = configparser.ConfigParser()
        self.file.read(self.path)

    def __getitem__(self, section) :
        try:
            return self.file[section]
        except Exception as e:
            return None

    def __setitem__(self, section, option) :
        if type(option) == type({}) :
            self.file[section] = option
            self.write()

    def get(self, section, option):
        result = ""
        try:
            result = self.file.get(section, option)
        except Exception as e:
            result = "None"
        return result

    def set(self, section, option, value) :
        try:
            # 搜尋section有沒有重複
            sections = self.file.sections()
            has_section = False
            for sec in sections :
                if section == sec :
                    has_section = True
                    break

            # 沒有搜尋到就新建section
            if has_section == False :
                self.file.add_section(section)

            self.file.set(section, option, value)
            self.write()
        except Exception as e:
            return False
            
        return True
    
    def write(self) :
        self.file.write(open(self.path, 'w'))

def main() :
    test = Config('test1.ini') # 這樣寫的話，ini要跟程式放在同層
    print(test.get('a', 'b'))
    print(test['a']['k'])
    
    # 會自動寫入
    test.set("a", "k", "2") # NOTE: 值要是字串
    test.set("b", "c", "A")
    test['w'] = {"a" : "b", "www" : "111"}
    
    # 不會自動寫入，要使用write()
    test['b']['q'] = "4"
    test['w']['a'] = "ggg"
    test.write()

if __name__ == "__main__":
    main()