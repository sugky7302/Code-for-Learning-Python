import os, json

# TODO:
# - 讀取資料
# - 寫入資料
# - 能夠hotfix，使系統不需要重啟
# - 方便使用者新增/修改/刪除
class Config :
    def __init__(self, path) :
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(dir_path, path)
        self.file = open(self.path, 'r')
        self.data = json.load(self.file)

    def __getitem__(self, index) :
        return self.data[index]

    def __setitem__(self, index, value) :
        self.data[index] = value

    def write(self) :
        self.close()
        self.file = open(self.path, 'w')
        
        json.dump(self.data, self.file, sort_keys = False, indent = 4, separators = (',', ':'))
        
        self.close()
        self.file = open(self.path, 'r')

    def close(self) :
        self.file.close()

def main() :
    test = Config("test.json")
    print(test["a"])
    test["a"] = 2
    print(test["a"])
    test["c"][0][0] = "kk"
    test["b"] = "hello"
    test.write()
    print(test["b"])

if __name__ == "__main__" :
    main()