import matplotlib.pyplot as plt
import numpy as np
import statistics

def show_stat_and_plot(Node_manager,task_number):
    assigned_nodes = [node for node in Node_manager.get_nodes() if node.tasks]
    node_ids = [node.node_id for node in assigned_nodes]
    task_counts = [len(node.tasks) for node in assigned_nodes]
    cpu_cores_used = [(Node_manager.cpu_cores - node.cpu_cores) for node in assigned_nodes]
    task_times = [sum(len(task.split()) for task in node.tasks) for node in assigned_nodes]
    size = len(assigned_nodes)//40
    stdev_task_count = statistics.stdev(task_counts)
    stdev_task_core = statistics.stdev(cpu_cores_used)
    stdev_task_time = statistics.stdev(task_times)

    print(f"{len(assigned_nodes)} nodes have been assigned tasks.")
    print("stdev task count per node (only nodes with tasks):", stdev_task_count)
    print("stdev core count per node (only nodes with tasks):", stdev_task_core)
    print("stdev time count per node (only nodes with tasks):", stdev_task_time)

    node_ids = node_ids[::size]
    task_counts = [statistics.mean(task_counts[i:i + size])/Node_manager.max_tasks * 100 for i in range(0, len(task_counts), size)]
    cpu_cores_used = [statistics.mean(cpu_cores_used[i:i + size])/Node_manager.cpu_cores * 100 for i in range(0, len(cpu_cores_used), size)]
    task_times = [statistics.mean(task_times[i:i + size])/Node_manager.preset_time * 100 for i in range(0, len(task_times), size)]

    r1 = np.arange(len(node_ids))

    # max_tasks_line = [Node_manager.max_tasks] * len(node_ids)
    # preset_time_line = [Node_manager.preset_time] * len(node_ids)
    # cpu_cores_line = [Node_manager.cpu_cores] * len(node_ids)

    nomal_line = [100] * len(node_ids)

    # plt.plot(r1, preset_time_line, color='g', linestyle='dashed', label='Max words storage per node')
    # plt.plot(r1, cpu_cores_line, color='r', linestyle='dashed', label='Max through put per node')
    # plt.plot(r1, max_tasks_line, color='b', linestyle='dashed', label='Max Tasks per node')

    # plt.plot(r1, nomal_line, color='y', linestyle='dashed', label='maximum capacity of each dimension of node after standardization"')
    plt.plot(r1, nomal_line, color='y', linestyle='dashed')

    plt.plot(r1, task_times, color='g', marker='o', label='Node words space utilization rate')
    plt.plot(r1, cpu_cores_used, color='r', marker='o', label='Node processing unit space utilization rate')
    plt.plot(r1, task_counts, color='b', marker='o', label='Node tasks space utilization rate')

    plt.xlabel('Node (aggregated)', fontweight='bold', fontsize=15)
    plt.ylabel('%', fontweight='bold', fontsize=15)
    plt.xticks([r for r in range(len(node_ids))], [str(i) for i in node_ids])

    plt.legend()
    plt.show()
    return stdev_task_count,stdev_task_core,stdev_task_time,len(assigned_nodes)



