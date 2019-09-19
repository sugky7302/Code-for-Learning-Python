# Paste by https://blog.csdn.net/wanghaoxi3000/article/details/70880753
# encoding: UTF-8
# 系统模块
import threading
from Queue import Queue, Empty


class EventManager:
    def __init__(self):
        """初始化事件管理器"""

        # 事件对象列表
        self.__event_queue = Queue()

        # 事件管理器开关
        self.__active = False

        # 事件处理线程
        self.__thread = threading.Thread(target=self.__run)

        # 这里的__handlers是一个字典，用来保存对应的事件的响应函数
        # 其中每个键对应的值是一个列表，列表中保存了对该事件监听的响应函数，一对多
        self.__handlers = {}

    def __run(self):
        """引擎运行"""

        while self.__active:
            try:
                # 获取事件的阻塞时间设为1秒
                event = self.__event_queue.get(block=True, timeout=1)
                self.__event_process(event)
            except Empty:
                pass

    def __event_process(self, event):
        """处理事件"""

        # 检查是否存在对该事件进行监听的处理函数
        if event.type_ in self.__handlers:
            # 若存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.type_]:
                handler(event)

    def start(self):
        """启动"""

        # 将事件管理器设为启动
        self.__active = True
        
        # 启动事件处理线程
        self.__thread.start()

    def stop(self):
        """停止"""

        # 将事件管理器设为停止
        self.__active = False

        # 等待事件处理线程退出
        self.__thread.join()

    def add_event_listener(self, type_, handler):
        """绑定事件和监听器处理函数"""

        # 尝试获取该事件类型对应的处理函数列表，若无则创建
        try:
            handler_list = self.__handlers[type_]
        except KeyError:
            handler_list = []

        self.__handlers[type_] = handler_list

        # 若要注册的处理器不在该事件的处理器列表中，则注册该事件
        if handler not in handler_list:
            handler_list.append(handler)

    def remove_event_listener(self, type_, handler):
        """移除监听器的处理函数"""
        # 读者自己试着实现
        pass

    def send_event(self, event):
        """发送事件，向事件队列中存入事件"""

        self.__event_queue.put(event)


class Event:
    """事件对象"""
    def __init__(self, type_=None):
        self.type_ = type_  # 事件类型
        self.dict = {}  # 字典用于保存具体的事件数据
