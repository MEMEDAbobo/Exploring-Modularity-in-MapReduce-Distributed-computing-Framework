from MAPREDUCE.node import Node
import time

class NodeManager:
    def __init__(self, maxtasks, maxtime, cpucores, numnodes, store):
        self.nodes = [Node(i, maxtasks, maxtime, cpucores, store) for i in range(numnodes)]
        self.max_tasks = maxtasks
        self.preset_time = maxtime
        self.cpu_cores = cpucores
    def start_node(self):
        for node in self.nodes:
            node.start()

    def close(self):
        while any(node.tasks for node in self.get_nodes()):
            time.sleep(1)

        for node in self.get_nodes():
            node.should_stop = True
        for node in self.get_nodes():
            node.join()

    def get_nodes(self):
        return self.nodes
