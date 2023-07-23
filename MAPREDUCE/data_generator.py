import random

def data_generator(num,data_len,randomseed):
    words =['A', 'I', 'O', 'On', 'Go', 'No', 'Cat', 'Dog', 'Sun', 'Fish', 'Bird', 'Tree', 'House', 'Mouse', 'Chair', 'Orange', 'Purple', 'Banana', 'Bicycle', 'Sunrise', 'Diamond', 'Mountain', 'Elephant', 'Painting', 'Adventure', 'Building', 'Happiness', 'Friendship', 'Education', 'Beautiful']
    tasks = []
    random.seed(randomseed)
    for i in range(num):
        taskid = "task" + str(i+1)
        task_data = ' '.join(random.choices(words, k=random.randint(1,data_len-1)))
        task = taskid + " " + task_data
        tasks.append(task)
    return tasks
