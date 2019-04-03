from threading import Thread, Event

def test_event():
    e = Event()
    def test():
        for i in range(5):
            print('start wait')
            e.wait()
            e.clear()  # 如果不调用clear()，那么标记一直为 True，wait()就不会发生阻塞行为
            print(i)

    Thread(target=test).start()
    return e


e = test_event()