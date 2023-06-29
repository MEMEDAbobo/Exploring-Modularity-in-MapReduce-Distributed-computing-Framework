import statistics
def show_stat(Node_manager):
    assigned_nodes = [node for node in Node_manager.get_nodes() if node.tasks]
    print(f"{len(assigned_nodes)} nodes have been assigned tasks.")
    task_counts = [len(node.tasks) for node in Node_manager.get_nodes() if len(node.tasks) > 0]
    stdev_task_count = statistics.stdev(task_counts)
    print("stdev task count per node (only nodes with tasks):", stdev_task_count)