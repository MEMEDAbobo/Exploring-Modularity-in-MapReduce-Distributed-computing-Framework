import random

def data_generator(num,data_len):
    words =['A', 'I', 'O', 'On', 'Go', 'No', 'Cat', 'Dog', 'Sun', 'Fish', 'Bird', 'Tree', 'House', 'Mouse', 'Chair', 'Orange', 'Purple', 'Banana', 'Bicycle', 'Sunrise', 'Diamond', 'Mountain', 'Elephant', 'Painting', 'Adventure', 'Building', 'Happiness', 'Friendship', 'Education', 'Beautiful']
    tasks = []
    # max_length = max(len(word) for word in words)
    # print(max_length)
    random.seed(3)
    for i in range(num):
        task_id = "task" + str(i+1)
        task_data = ' '.join(random.choices(words, k=random.randint(0,data_len)))
        task = task_id + " " + task_data
        tasks.append(task)
    return tasks
