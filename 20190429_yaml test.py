import os
import yaml

# TODO:
# - 讀取資料進python
# - 能夠hotfix，並且獲得最新的資料
class Config :
    def __init__(self, path) :
        # 讀取路徑
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(dir_path, path)

        self.file = open(self.path)
        self.data = yaml.load(self.file)

    def __getitem__(self, index) :
        return self.data[index]

def main() :
    test = Config('test.yml')
    print(test.data)
    print(test['test'][0])
    print(type(test.data))
    print(type(test['test']))

if __name__ == "__main__":
    main()