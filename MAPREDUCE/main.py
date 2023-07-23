from node_manager import NodeManager
from task_scheduler import TaskScheduler
import time
from data_generator import data_generator
from data_store import MemoryDataStore, FileDataStore
from plot import show_stat_and_plot
Max_tasks = 4
max_time = 22
Num_nodes = 5000
cpu_cores = 14
task_number = 10000
# max task core = 9
# task_time_range = 2 - 10
task_time_range = 10

randomseednum=0

data = data_generator(task_number,task_time_range,randomseednum)
data_store = MemoryDataStore()
node_manager = NodeManager(Max_tasks, max_time, cpu_cores, Num_nodes, data_store)
scheduler = TaskScheduler(node_manager)

starttime = time.time()
scheduler.assign_task_wf(data)
endtime = time.time()
Execution_time = endtime - starttime
print("Fit execution time = ", Execution_time, "s")
show_stat_and_plot(node_manager,task_number)
node_manager.start_node()
node_manager.close()

