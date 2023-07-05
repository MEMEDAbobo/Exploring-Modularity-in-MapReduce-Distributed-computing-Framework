from MAPREDUCE.node import Node
import time

class NodeManager:
    def __init__(self, max_tasks, max_time, cpu_cores, num_nodes, data_store):
        self.nodes = [Node(i, max_tasks, max_time, cpu_cores, data_store) for i in range(num_nodes)]
        self.max_tasks = max_tasks
        self.preset_time = max_time
        self.cpu_cores = cpu_cores
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
    #
    # def create_node(self):
    #     node = Node(len(self.nodes), self.max_tasks)
    #     node.start()
    #     self.nodes.append(node)
    #     return node