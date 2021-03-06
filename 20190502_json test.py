import os
import json

# TODO:
# - 讀取資料
# - 寫入資料
# - 能夠hotfix，使系統不需要重啟
# - 方便使用者新增/修改/刪除


class Config:
    def __init__(self, path):
        dir_path = os.path.abspath('.')
        self.path = os.path.join(dir_path, path)
        self.file = open(self.path, 'r')
        self.data = json.load(self.file)
        self.close()

    def __getitem__(self, index):
        try:
            return self.data[index]
        except Exception as e:
            return False

    def __setitem__(self, index, value):
        try:
            self.data[index] = value
        except Exception as e:
            return False

    def write(self):
        self.file = open(self.path, 'w')

        json.dump(self.data,
                  self.file,
                  sort_keys=False,
                  indent=4,
                  separators=(',', ' : '))

        self.close()

    def close(self):
        self.file.close()


def insert(config):
    station_name = "test"
    go_action = [1]
    go_ultrasonic = [2, 3]
    config[station_name] = {
        "go": {
            "action": go_action,
            "ultrasonic": go_ultrasonic
        }
    }


def main():
    print(
        json.loads(
            '[\n    {"id": 2, "args":  [1]},\n    {"id": 14, "args": [0.6]},\n    {"id": "stay"},\n    {"import": "test3"}\n]'
        ))
    test = Config("test.json")
    print(test['a'][0])
    print(test['b'][1])


if __name__ == "__main__":
    main()
