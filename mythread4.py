#!/usr/bin/python
#coding:gbk

import threading
import time
import Queue

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        # ��������ɹ���������󷵻�True
        # ��ѡ��timeout��������ʱ��һֱ����ֱ���������
        # ����ʱ�󽫷���False
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s process %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = Queue.Queue(10)       #����һ�����ж�����󳤶�Ϊ10
threads = []
threadID = 1

# �������߳�
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# ������
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# �ȴ��������
while not workQueue.empty():
    pass

# ֪ͨ�߳���ʱ���˳�
exitFlag = 1

# �ȴ������߳����
for t in threads:
    t.join()

print("Exiting Main Thread")









