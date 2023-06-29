import time
class TaskScheduler:
    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.last_assigned_node_index = 0

    def assign_task_bf(self, tasks):
        for task in tasks:
            word_count = len(task.split())
            nodes = self.node_manager.get_nodes()
            best_fit_node = None
            min_space = float('inf')
            min_tasks = float('inf')
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                remaining_space = self.node_manager.preset_time - cur_time
                if word_count <= remaining_space and len(node.tasks) < node.max_tasks:
                    if remaining_space < min_space or (remaining_space == min_space and len(node.tasks) < min_tasks):
                        best_fit_node = node
                        min_space = remaining_space
                        min_tasks = len(node.tasks)
            if best_fit_node is not None:
                with best_fit_node.lock:
                    best_fit_node.tasks.append(task)
                    # print("Assigned task:", task, "to node", best_fit_node.node_id)
            else:
                print("This task", task, "cannot be assigned (oversize or not enough nodes)")


    def assign_task_wf(self, tasks):
        for task in tasks:
            word_count = len(task.split())
            nodes = sorted(self.node_manager.get_nodes(), key=lambda node: self.node_manager.preset_time - sum(
                len(task.split()) for task in node.tasks), reverse=True)
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                with node.lock:
                    if len(node.tasks) < node.max_tasks and cur_time + word_count <= self.node_manager.preset_time:
                        node.tasks.append(task)
                        # print("Assigned task:", task, "to node", node.node_id)
                        break
            else:
                print("this task", task, "can not assign(oversize or not enough nodes)")

    def assign_task_ff(self, tasks):
        for task in tasks:
            word_count = len(task.split())
            nodes = self.node_manager.get_nodes()
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                with node.lock:
                    if len(node.tasks) < node.max_tasks and cur_time + word_count <= self.node_manager.preset_time:
                        node.tasks.append(task)
                        # print("Assigned task:", task, "to node", node.node_id)
                        # assigned = True
                        break
            else:
                print("this task", task, "can not assign(oversize or not enough nodes)")

    def assign_task_nf(self, tasks):
        nodes = self.node_manager.get_nodes()
        node_count = len(nodes)
        for task in tasks:
            word_count = len(task.split())
            for _ in range(node_count):
                node = nodes[self.last_assigned_node_index]
                cur_time = sum(len(task.split()) for task in node.tasks)
                with node.lock:
                    if len(node.tasks) < node.max_tasks and cur_time + word_count <= self.node_manager.preset_time:
                        node.tasks.append(task)
                        # print("Assigned task:", task, "to node", node.node_id)
                        self.last_assigned_node_index = (self.last_assigned_node_index + 1) % node_count
                        break
                self.last_assigned_node_index = (self.last_assigned_node_index + 1) % node_count
            else:
                print("this task", task, "can not assign(oversize or not enough nodes)")

