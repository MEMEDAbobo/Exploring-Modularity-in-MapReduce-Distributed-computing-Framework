from node_manager import NodeManager
from task_scheduler import TaskScheduler
import time
from data_generator import data_generator
from data_store import MemoryDataStore
from plot import show_stat_and_plot
max_tasks = 4
throughput = 20
max_time = 22
num_nodes = 5000
task_number = 10000
# task core range = 1-9
# task time range = 2 - 10
task_time_range = 14
task_count_list = []
task_core_list = []
task_time_list = []
node_used_list = []
Execution_time_list = []
# unsign_num_list = []
for i in range(10):
    data = data_generator(task_number, task_time_range,i)
    data_store = MemoryDataStore()
    node_manager = NodeManager(max_tasks, max_time, throughput, num_nodes, data_store)
    scheduler = TaskScheduler(node_manager)
    starttime = time.time()
    scheduler.assign_task_ff(data)
    endtime = time.time()
    Execution_time = endtime - starttime
    stdev_taskcount, stdev_taskcore, stdev_tasktime,node_used = show_stat_and_plot(node_manager, task_number)
    node_manager.start_node()
    node_manager.close()
    task_count_list.append(stdev_taskcount)
    task_core_list.append(stdev_taskcore)
    task_time_list.append(stdev_tasktime)
    node_used_list.append(node_used)
    Execution_time_list.append(Execution_time)
    # unsign_num_list.append(unsign)
print("Max tasks =",max_tasks,"throughput =",throughput,"max time =",max_time,"nodes number =",num_nodes,"tasks number =",task_number,"tasks time range =",task_time_range)
print("\n", "stdev of nodes' tasks number", task_count_list, "\n", "stdev of nodes' processing unit used",task_core_list, "\n", "stdev of nodes' words number", task_time_list, "\n", "node used", node_used_list, "\n", "Fit execution time ", Execution_time_list)