import statistics
def show_stat(Node_manager):
    assigned_nodes = [node for node in Node_manager.get_nodes() if node.tasks]
    print(f"{len(assigned_nodes)} nodes have been assigned tasks.")
    task_counts = [len(node.tasks) for node in assigned_nodes]
    core_counts = [(Node_manager.cpu_cores - node.cpu_cores) for node in assigned_nodes]
    time_counts = [sum(len(task.split()) for task in node.tasks) for node in assigned_nodes]
    stdev_task_count = statistics.stdev(task_counts)
    stdev_task_core = statistics.stdev(core_counts)
    stdev_task_time = statistics.stdev(time_counts)
    print("stdev task count per node (only nodes with tasks):", stdev_task_count)
    print("stdev core count per node (only nodes with tasks):", stdev_task_core)
    print("stdev time count per node (only nodes with tasks):", stdev_task_time)