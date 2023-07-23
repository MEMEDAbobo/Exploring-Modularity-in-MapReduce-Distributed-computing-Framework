import threading
import time
from MAPREDUCE.map_reduce import MapReduce

class Node(threading.Thread):
    def __init__(self, id, maxtasks,maxtime,throughput,store):
        threading.Thread.__init__(self)
        self.node_id = id
        self.tasks = []
        self.should_stop = False
        self.max_tasks = maxtasks
        self.max_time = maxtime
        self.cpu_cores = throughput
        self.lock = threading.Lock()
        self.data_store = store

    def run(self):
        while not self.should_stop:
            task = None
            with self.lock:
                if len(self.tasks) > 0:
                    task = self.tasks.pop(0)

            if task:
                results = MapReduce([task])
                # print("Node", self.node_id, "results:", results)
                self.data_store.save(self.node_id, (results))
                # time.sleep(word_count)
                # print("Node", self.node_id, "finished processing task:", task)
            else:
                time.sleep(1)