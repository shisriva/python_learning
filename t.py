pods = [
    {"name": "api-server", "cpu": 2, "memory": 4096, "status": "Running"},
    {"name": "gpu-trainer", "cpu": 8, "memory": 32768, "status": "Pending"},
    {"name": "redis", "cpu": 1, "memory": 1024, "status": "Running"},
    {"name": "llm-inference", "cpu": 4, "memory": 16384, "status": "Running"},
    {"name": "mlflow", "cpu": 2, "memory": 2048, "status": "Failed"},
]

'''
Task1:

Print only the pod names that are Running.

Expected Output:

api-server
redis
llm-inference


for i in pods:
    if i["status"] == "Running": 
        print(i["name"])
'''

'''

Task2: Calculate the total CPU used by Running pods.

Expected Output

Total Running CPU = 7


counter = 0
for i  in pods:
    if i["status"] == "Running":
        counter = counter + i["cpu"]
print(counter)

'''

'''

Task3:

    Find the pod using the maximum memory.

Expected Output

gpu-trainer
32768


max_memory = 0
pod_name = ""
for pod in pods:
    if pod["memory"] > max_memory:
        max_memory = pod["memory"]
        pod_name = pod["name"]

print(max_memory)
print(pod_name)


'''


'''

Ek nayi list running_pods banao jisme sirf Running status wale pods hon.

[
 {'name': 'api-server', 'status': 'Running', 'cpu': 2, 'memory': 4096},
 {'name': 'redis', 'status': 'Running', 'cpu': 1, 'memory': 2048},
 {'name': 'llm-inference', 'status': 'Running', 'cpu': 8, 'memory': 16384}
]
app = []
for pod in pods:
    if pod["status"] == "Running":
        app.append(pod)
        pass
print(app)

'''

