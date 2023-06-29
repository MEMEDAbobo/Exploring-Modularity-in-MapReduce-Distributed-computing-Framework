import threading
import time
from MAPREDUCE.map_reduce import MapReduce

class Node(threading.Thread):
    def __init__(self, node_id, max_tasks):
        threading.Thread.__init__(self)
        self.node_id = node_id
        self.tasks = []
        self.should_stop = False
        self.max_tasks = max_tasks
        self.lock = threading.Lock()

    def run(self):
        while not self.should_stop:
            task = None
            with self.lock:
                if len(self.tasks) > 0:
                    task = self.tasks.pop(0)

            if task:
                results, word_count = MapReduce([task])
                # print("Node", self.node_id, "results:", results)
                # time.sleep(word_count)
                # print("Node", self.node_id, "finished processing task:", task)
            else:
                time.sleep(1)