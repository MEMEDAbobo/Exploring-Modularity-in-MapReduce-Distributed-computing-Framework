# 主程序
from node_manager import NodeManager
from task_scheduler import TaskScheduler
from test import show_stat
import time
from data_generator import data_generator
# data = ["task1 happy join happy", "task2 like hi hi hi hi hi", "task3 like dede", "task4 hello hi",
#         "task5 hi", "task6", "task7 Once upon a time", "task8 in a faraway land there",
#         "task9 was a tiny","task10","task11 kingdom","task12 peaceful prosperous and rich in romance oh",
#         "task13 and tradition nestled in","task14 the heart of","task15 this kingdom was a small village with",
#         "task16 an enchanted castle towering high above the clouds the",
#         "task17 townsfolk of this village lived a simple life but","task18 they","task19 lived",
#         "task20 in fear for","task21 in this castle lived a beast","task22 unlike any other a horrible creature with a",
#         "task23 mean streak two","task24 miles wide the villagers lived in terror of","task25 the",
#         "task26 beast and would not dare to approach the castle"]

data = data_generator(30,5)

Max_tasks = 4
Preset_time = 8
Num_nodes = 30

Node_manager = NodeManager(Max_tasks, Preset_time, Num_nodes)
scheduler = TaskScheduler(Node_manager)

start_time = time.time()
scheduler.assign_task_ff(data)
end_time = time.time()
print("Execution time: ", end_time - start_time, "seconds")

show_stat(Node_manager)
Node_manager.start_node()
Node_manager.close()
