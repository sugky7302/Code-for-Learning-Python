import sys
import threading


# NOTE: 2020-03-27
#   必須要繼承object才能使用單例模式
#   必須要在同一個python執行器下
#   目前測試沒加鎖也沒有網路上所說的，不支援多線程的問題，再多注意
#   單例模式的另一個做法是在類別下面生成一個實例，其他文件就import那個實例
class R(object):
    # _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(R, "_instance"):
            # with R._instance_lock:
            # if not hasattr(R, "_instance"):
            R._instance = object.__new__(cls, *args, **kwargs)
        return R._instance

    def __init__(self):
        import time
        time.sleep(2)


# NOTE: 可以利用模組化，將文件指定為實例
sys.modules[__name__] = R()
# 其他文件: import 20190529_class dict test -> 只會import該實例


def task(arg):
    obj = R()
    print(obj)


for i in range(20):
    t = threading.Thread(
        target=task, args=[
            i,
        ])
    t.start()
