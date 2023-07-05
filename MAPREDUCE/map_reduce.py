def MapFunction(data):
    cur_results = []
    words = data.split()
    for word in words:
        cur_results.append((word, 1))
    return cur_results
def ReduceFunction(key, values):
    result = sum(values)
    return (key, result)

def MapReduce(data):
    cur_results = []
    for sentence in data:
        cur_results.extend(MapFunction(sentence))

    FinalResults = []
    key_values = {}
    for key, value in cur_results:
        if key not in key_values:
            key_values[key] = []
        key_values[key].append(value)

    for key, values in key_values.items():
        FinalResults.append(ReduceFunction(key, values))

    return FinalResults