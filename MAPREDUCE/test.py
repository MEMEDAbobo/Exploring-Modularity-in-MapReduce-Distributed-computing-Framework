from node_manager import NodeManager
from task_scheduler import TaskScheduler
import time
from data_generator import data_generator
from data_store import MemoryDataStore
from plot import show_stat_and_plot
Max_tasks = 4
cpu_cores = 20
max_time = 22
Num_nodes = 500
task_number = 1000
# task core range = 1-9
# task time range = 2 - 10
task_time_range = 10
task_count_list = []
task_core_list = []
task_time_list = []
node_used_list = []
Execution_time_list = []
for i in range(100):
    data = data_generator(task_number, task_time_range,i)
    data_store = MemoryDataStore()
    node_manager = NodeManager(Max_tasks, max_time, cpu_cores, Num_nodes, data_store)
    scheduler = TaskScheduler(node_manager)
    start_time = time.time()
    scheduler.assign_task_nf(data)
    end_time = time.time()
    Execution_time = end_time - start_time
    stdev_task_count, stdev_task_core, stdev_task_time,node_used = show_stat_and_plot(node_manager, task_number)
    node_manager.start_node()
    node_manager.close()
    task_count_list.append(stdev_task_count)
    task_core_list.append(stdev_task_core)
    task_time_list.append(stdev_task_time)
    node_used_list.append(node_used)
    Execution_time_list.append(Execution_time)
print("Max_tasks =",Max_tasks,"cpu_cores =",cpu_cores,"max_time =",max_time,"Num_nodes =",Num_nodes,"task_number =",task_number,"task_time_range =",task_time_range)
print("\n", "task owned stdev", task_count_list, "\n", "cores used stdev",task_core_list, "\n", "time used stdev", task_time_list, "\n", "node used", node_used_list, "\n", "execution time ", Execution_time_list)