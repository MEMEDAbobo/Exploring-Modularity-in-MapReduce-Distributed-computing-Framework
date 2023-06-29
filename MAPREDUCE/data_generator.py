import random

words = ['hello', 'world', 'test', 'sample', 'data', 'this', 'is', 'a', 'new', 'task']
tasks = []

for i in range(1000):
    task_id = "task" + str(i+1)
    task_data = ' '.join(random.choices(words, k=random.randint(0,10)))
    task = task_id + " " + task_data
    tasks.append(task)

print(tasks)