from node_manager import NodeManager
from task_scheduler import TaskScheduler
import time
from data_generator import data_generator
from data_store import MemoryDataStore, FileDataStore
from plot import show_stat_and_plot
Max_tasks = 4
max_time = 12
Num_nodes = 800
cpu_cores = 11
task_number = 1000
# task_time_range = 2 - 10
task_time_range = 10

randomseednum=1

data = data_generator(task_number,task_time_range,randomseednum)
# data = ["a a a a a a aa", "a a a a a aaaaa","aa"]
data_store = MemoryDataStore()
node_manager = NodeManager(Max_tasks, max_time, cpu_cores, Num_nodes, data_store)
# node_manager_bf = NodeManager(Max_tasks, max_time, cpu_cores, Num_nodes, data_store)
scheduler = TaskScheduler(node_manager)
# scheduler_bf = TaskScheduler(node_manager_bf)

start_time = time.time()
scheduler.assign_task_nf(data)
end_time = time.time()
Execution_time = end_time - start_time
print("Execution time: ", Execution_time, "seconds")
show_stat_and_plot(node_manager,task_number)
node_manager.start_node()
node_manager.close()

