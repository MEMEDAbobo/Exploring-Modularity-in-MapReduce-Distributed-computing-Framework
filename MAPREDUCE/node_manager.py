from MAPREDUCE.node import Node
import time

class NodeManager:
    def __init__(self, max_tasks, preset_time, num_nodes,data_store):
        self.nodes = [Node(i, max_tasks, data_store) for i in range(num_nodes)]
        self.max_tasks = max_tasks
        self.preset_time = preset_time
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