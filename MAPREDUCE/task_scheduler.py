import time
class TaskScheduler:
    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.last_assigned_node_index = 0

    # 首先考虑剩余时间最少的节点，如果有多个节点具有相同的剩余时间，那么选择具有最少任务的节点
    def assign_task_bf1(self, tasks):
        for task in tasks:
            # Get the required cores for the task
            words = task.split()
            required_cores = len(words[-1])
            word_count = len(task.split())
            nodes = self.node_manager.get_nodes()
            best_fit_node = None
            min_space = float('inf')
            min_cores = float('inf')
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                node_remaining_time = self.node_manager.preset_time - cur_time
                remaining_core_space = node.cpu_cores - required_cores
                # Check if the node has enough cores and time space for the task
                if word_count <= node_remaining_time and len(node.tasks) < node.max_tasks and required_cores <= node.cpu_cores:
                    if (node_remaining_time < min_space or (node_remaining_time == min_space and len(node.tasks) < min_cores)) and remaining_core_space >= 0:
                        best_fit_node = node
                        min_space = node_remaining_time
                        min_cores = len(node.tasks)
            if best_fit_node is not None:
                with best_fit_node.lock:
                    best_fit_node.tasks.append(task)
                    print("Assigned task:", task, "to node", best_fit_node.node_id)
                    # update the cpu_cores of the node
                    best_fit_node.cpu_cores -= required_cores
            else:
                print("This task", task, "cannot be assigned (oversize or not enough cores or nodes)")

    # 剩余时间和剩余核数的乘积，并使用这个值表示剩余空间来寻找最佳的节点
    def assign_task_bf2(self, tasks):
        for task in tasks:
            words = task.split()
            task_cores = len(words[-1])
            task_time = len(task.split())
            nodes = self.node_manager.get_nodes()
            best_fit_node = None
            min_space_product = float('inf')
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                node_remaining_time = self.node_manager.preset_time - cur_time
                remaining_space = node_remaining_time * node.cpu_cores
                if task_time <= node_remaining_time and len(node.tasks) < node.max_tasks and task_cores <= node.cpu_cores and remaining_space < min_space_product:
                    best_fit_node = node
                    min_space_product = remaining_space
            if best_fit_node is not None:
                with best_fit_node.lock:
                    best_fit_node.tasks.append(task)
                    print("Assigned task:", task, "to node", best_fit_node.node_id)
                    best_fit_node.cpu_cores -= task_cores
            else:
                print("This task", task, "cannot be assigned (oversize or not enough cores or nodes)")


    def assign_task_bf3(self, tasks):
        for task in tasks:
            # Get the required cores for the task
            words = task.split()
            task_cores = len(words[-1])
            task_time = len(task.split())
            nodes = self.node_manager.get_nodes()
            best_fit_node = None
            min_space = float('inf')
            min_time = float('inf')
            min_core = float('inf')
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                node_remaining_time = self.node_manager.preset_time - cur_time
                remaining_space = node_remaining_time * node.cpu_cores
                if task_time <= node_remaining_time and len(node.tasks) < node.max_tasks and task_cores <= node.cpu_cores and remaining_space <= min_space:
                    if remaining_space == min_space and (node_remaining_time + node.cpu_cores)>= (min_time+min_core):
                        break
                    best_fit_node = node
                    min_space = remaining_space
                    min_time = node_remaining_time
                    min_core = node.cpu_cores
            if best_fit_node is not None:
                with best_fit_node.lock:
                    best_fit_node.tasks.append(task)
                    print("Assigned task:", task, "to node", best_fit_node.node_id)
                    # update the cpu_cores of the node
                    best_fit_node.cpu_cores -= task_cores
            else:
                print("This task", task, "cannot be assigned (oversize or not enough cores or nodes)")

    def assign_task_wf(self, tasks):
        for task in tasks:
            word_count = len(task.split())
            required_cores = len(task.split()[-1])
            nodes = sorted(self.node_manager.get_nodes(), key=lambda node: (self.node_manager.preset_time - sum(
                len(task.split()) for task in node.tasks)) * node.cpu_cores, reverse=True)
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                remaining_core_space = node.cpu_cores - required_cores
                with node.lock:
                    if len(node.tasks) < node.max_tasks and cur_time + word_count <= self.node_manager.preset_time and required_cores <= node.cpu_cores and remaining_core_space >= 0:
                        node.tasks.append(task)
                        # update the cpu_cores of the node
                        node.cpu_cores -= required_cores
                        break
            else:
                print("this task", task, "can not assign(oversize or not enough cores or nodes)")

    def assign_task_ff(self, tasks):
        for task in tasks:
            # Get the required cores for the task
            words = task.split()
            required_cores = len(words[-1])
            word_count = len(task.split())
            nodes = self.node_manager.get_nodes()
            for node in nodes:
                cur_time = sum(len(task.split()) for task in node.tasks)
                with node.lock:
                    if len(node.tasks) < node.max_tasks and cur_time + word_count <= self.node_manager.preset_time and node.cpu_cores >= required_cores:
                        node.tasks.append(task)
                        print("Assigned task:", task, "to node", node.node_id)
                        # update the cpu_cores of the node
                        node.cpu_cores -= required_cores
                        break
            else:
                print("This task", task, "cannot be assigned (oversize or not enough cores or nodes)")

    def assign_task_nf(self, tasks):
        nodes = self.node_manager.get_nodes()
        node_count = len(nodes)
        for task in tasks:
            words = task.split()
            required_cores = len(words[-1])
            word_count = len(task.split())
            for _ in range(node_count):
                node = nodes[self.last_assigned_node_index]
                cur_time = sum(len(task.split()) for task in node.tasks)
                with node.lock:
                    if len(node.tasks) < node.max_tasks and cur_time + word_count <= self.node_manager.preset_time and node.cpu_cores >= required_cores:
                        node.tasks.append(task)
                        node.cpu_cores -= required_cores
                        # print("Assigned task:", task, "to node", node.node_id)
                        self.last_assigned_node_index = (self.last_assigned_node_index + 1) % node_count
                        break
                self.last_assigned_node_index = (self.last_assigned_node_index + 1) % node_count
            else:
                print("this task", task, "can not assign(oversize or not enough nodes)")

