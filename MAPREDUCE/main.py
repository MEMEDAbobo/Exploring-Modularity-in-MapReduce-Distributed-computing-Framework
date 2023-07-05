from node_manager import NodeManager
from task_scheduler import TaskScheduler
import time
from data_generator import data_generator
from data_store import MemoryDataStore, FileDataStore
from plot import show_stat_and_plot
data = data_generator(10000,10)
# data = ["a a a a a a aa", "a a a a a aaaaa","aa"]

data_store = MemoryDataStore()


Max_tasks = 4
max_time = 16
Num_nodes = 6000
cpu_cores = 15

node_manager = NodeManager(Max_tasks, max_time, cpu_cores, Num_nodes, data_store)
scheduler = TaskScheduler(node_manager)

start_time = time.time()
scheduler.assign_task_wf(data)
end_time = time.time()
print("Execution time: ", end_time - start_time, "seconds")

show_stat_and_plot(node_manager)
node_manager.start_node()
node_manager.close()

# node1 = node_manager.nodes[1]  # Assuming Node1 is at index 1
# loaded_data = node1.data_store.data
# print("hi",loaded_data)