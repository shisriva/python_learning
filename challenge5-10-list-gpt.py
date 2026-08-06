pods = [
    {"name": "api-server", "cpu": 2, "memory": 4096, "status": "Running"},
    {"name": "redis", "cpu": 1, "memory": 1024, "status": "Running"},
    {"name": "worker", "cpu": 4, "memory": 8192, "status": "Pending"},
    {"name": "database", "cpu": 2, "memory": 4096, "status": "Failed"},
    {"name": "llm-inference", "cpu": 4, "memory": 16384, "status": "Running"}
]

'''
Task 5: Total CPU aur Memory calculate karo

Expected Output:

Total CPU = 13
Total Memory = 33792 MB


count = 0
count1 = 0
for pod in pods:
    count = count + pod["cpu"]
    count1 = count1 + pod["memory"]
print(f'Total CPU = {count}')
print(f'Total Memory = {count1}')
'''

'''

Task 6: Sirf Running Pods ka CPU total

Expected Output:

Running CPU = 7

Sirf "status" == "Running" wale pods ka CPU add karna hai.

cpu_running = 0

for pod in pods:
    if pod["status"] == "Running":
        cpu_running = cpu_running + pod["cpu"]
print(f'Running CPU = {cpu_running}')

'''

'''

Highest CPU wala pod find karo.

Expected output:

Highest CPU Pod = worker
CPU = 4


pod_name = ""
cpu_high = 0
for pod in pods:
    if pod["cpu"] > cpu_high:
        cpu_high = pod["cpu"]
        pod_name = pod["name"]
print(f'CPU: {cpu_high}')
print(f'Highest CPU Pod: {pod_name}')
'''
'''

Sirf sabhi pod names ki list banao.

Expected output:

['api-server', 'redis', 'worker', 'database', 'llm-inference']

pod_name = []
for pod in pods:
    pod_name.append(pod["name"])
print(pod_name)

'''
'''

Count Failed Pods

fail_pod = 0
for pod in pods:
    if pod["status"] == "Failed":
        fail_pod += 1

print(f'Failed Pods = {fail_pod}')
'''

'''

-------------------------
 Pod Name : api-server
 CPU : 2
 Memory : 4096
 Status: Running
-------------------------
 Pod Name : redis
 CPU : 1
 Memory : 1024
 Status: Running
-------------------------
 Pod Name : llm-inference
 CPU : 4
 Memory : 16384
 Status: Running

 my version, correct:

for pod in pods:
    if pod["status"] == "Running":
        print(f'------------------------- \n Pod Name : {pod["name"]} \n CPU : {pod["cpu"]} \n Memory :  {pod["memory"]} \n Status: {pod["status"]}')

Improvised Version from GPT

for pod in pods:
    if pod["status"] == "Running":
        print("-------------------------")
        print(f"Pod Name : {pod['name']}")
        print(f"CPU      : {pod['cpu']}")
        print(f"Memory   : {pod['memory']}")
        print(f"Status   : {pod['status']}")
        print()


'''
