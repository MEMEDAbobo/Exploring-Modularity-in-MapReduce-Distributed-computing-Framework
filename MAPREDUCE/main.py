# 主程序
from node_manager import NodeManager
from task_scheduler import TaskScheduler
from test import show_stat

data = ["task1 happy join happy", "task2 like hi hi hi hi hi", "task3 like dede", "task4 hello hi",
        "task5 hi", "task6", "task7 Once upon a time", "task8 in a faraway land there",
        "task9 was a tiny","task11 kingdom"," task12 peaceful prosperous and rich in romance oh",
        "task13 and tradition nestled in","task14 the heart of","task15 this kingdom was a small village with",
        "task16 an enchanted castle towering high above the clouds the",
        "task17 townsfolk of this village lived a simple life but","task18 they","task19 lived",
        "task20 in fear for","task21 in this castle lived a beast","task22 unlike any other a horrible creature with a",
        "task23 mean streak two","task24 miles wide the villagers lived in terror of","task25 the",
        "task26 beast and would not dare to approach the castle"]

Max_tasks = 3
Preset_time = 12
Num_nodes = 26

Node_manager = NodeManager(Max_tasks, Preset_time, Num_nodes)
scheduler = TaskScheduler(Node_manager)
scheduler.assign_task_bf(data)
show_stat(Node_manager)
Node_manager.start_node()
Node_manager.close()
