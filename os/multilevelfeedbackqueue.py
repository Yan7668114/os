"""
假設
A 進程是交互式進程，需要頻繁的與使用者互動，因此需要較高的優先級。
B 進程是 CPU 密集型進程，需要大量的 CPU 資源，因此需要較低的優先級。
C 進程是 IO 密集型進程，需要大量的 IO 資源，因此需要較低的優先級。

根據多級反饋佇列（Multilevel Feedback Queue）的調度算法，可以將這 3 個進程分成 2 個佇列：
高優先級佇列：包含 A 進程。
低優先級佇列：包含 B 進程和 C 進程。

在這個例子中，A 進程會優先獲得 CPU 資源，並且可以頻繁的與使用者互動。B 進程和 C 進程會在 A 進程完成後獲得 CPU 資源。
"""
import time

class Process:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.start_time = None
        self.end_time = None

    def run(self):
        print(f"{self.name} 開始執行")
        self.start_time = time.time()
        time.sleep(self.priority)
        self.end_time = time.time()
        print(f"{self.name} 執行結束")

def main():
    # 初始化進程
    processes = [
        Process("A", 1),
        Process("B", 2),
        Process("C", 3),
    ]

    # 啟動調度器
    scheduler = Scheduler()
    scheduler.start(processes)

class Scheduler:
    def __init__(self):
        self.processes = []

    def start(self, processes):
        self.processes = processes
        while True:
            # 檢查是否有進程可以調度
            if self.processes:
                # 選擇優先級最高的進程
                process = self.processes.pop(0)
                # 調度進程
                process.run()
            else:
                # 沒有進程可以調度，等待下一個進程
                time.sleep(1)

if __name__ == "__main__":
    main()
