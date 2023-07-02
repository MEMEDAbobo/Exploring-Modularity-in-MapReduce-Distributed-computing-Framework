# 主程序
from node_manager import NodeManager
from task_scheduler import TaskScheduler
from test import show_stat
import time
from data_generator import data_generator
from data_store import MemoryDataStore, FileDataStore

data = data_generator(30,5)

data_store = MemoryDataStore()


Max_tasks = 4
Preset_time = 8
Num_nodes = 30

node_manager = NodeManager(Max_tasks, Preset_time, Num_nodes,data_store)
scheduler = TaskScheduler(node_manager)

start_time = time.time()
scheduler.assign_task_ff(data)
end_time = time.time()
print("Execution time: ", end_time - start_time, "seconds")

show_stat(node_manager)
node_manager.start_node()
node_manager.close()

node1 = node_manager.nodes[1]  # Assuming Node1 is at index 1
loaded_data = node1.data_store.data
print("hi",loaded_data)