pods = [
    {"name": "api-server", "cpu": 2, "memory": 4096, "status": "Running"},
    {"name": "redis", "cpu": 1, "memory": 1024, "status": "Running"},
    {"name": "worker", "cpu": 4, "memory": 8192, "status": "Pending"},
    {"name": "database", "cpu": 2, "memory": 4096, "status": "Failed"},
    {"name": "llm-inference", "cpu": 4, "memory": 16384, "status": "Running"}
]


'''
Input:

pods = [
    {"name": "api-server", "cpu": 2, "memory": 4096, "status": "Running"},
    {"name": "redis", "cpu": 1, "memory": 1024, "status": "Running"},
    {"name": "worker", "cpu": 4, "memory": 8192, "status": "Pending"},
    {"name": "database", "cpu": 2, "memory": 4096, "status": "Failed"},
    {"name": "llm-inference", "cpu": 4, "memory": 16384, "status": "Running"}
]
Task1: Requirement

Ek function banao:

def total_cpu(pods):

Jo total CPU return kare.

Expected output:

13

'''


def total_cpu(pods):
    sum_cpu = 0
    for pod in pods:
        sum_cpu += pod["cpu"]
    return sum_cpu
result = total_cpu(pods)
print(result)





'''
Task2: Requirement:

Ek function banao:

def running_pods_count(pods):

Jo sirf Running status wale pods ka count return kare.

Expected output:

3

'''


def running_pods_count(pods):
    running_pods = 0
    for pod in pods:
        if pod["status"] == "Running":
            running_pods += 1
    return running_pods
result = running_pods_count(pods)
print(result)
            



'''
Function Task 3: Highest CPU Pod

Ab ye karo:

def highest_cpu_pod(pods):

Requirement:

Highest CPU wale pod ka name return karo
Sirf function ke andar logic likhna hai

Expected:

worker
'''
def highest_cpu_pod(pods):
    max_cpu = 0
    max_cpu_pod = ""
    for pod in pods:
        if pod["cpu"] > max_cpu:
            max_cpu = pod["cpu"]
            max_cpu_pod = pod["name"]
    return max_cpu_pod
result = highest_cpu_pod(pods)
print(result)
            
'''
Task4: Ek function banao:

def highest_memory_pod(pods):

Jo highest memory wale pod ki details dictionary ke form mein return kare.

Expected output:

{
    "name": "llm-inference",
    "memory": 16384,
    "status": "Running"
}
'''

'''

My Attempt:

def highest_memory_pod(pods):
    highest_mem = 0
    pod_name = ""
    pod_status = ""
    for pod in pods:
        if highest_mem > pod["memory"]:
            highest_mem = pod["memory"]
            pod_name = pod["name"]
            pod_status = pod["status"]
            
    return highest_mem
    return pod_name
    return pod_status

print(f'"name:" {pod_name}')
print(f'"memory:" {highest_mem}')
print(f'"status:" {pod_status}')
print()

result = highest_memory_pod(pods)
print(result)

'''

#Correct Version from GPT:


def highest_memory_pod(pods):
    highest_mem = 0
    pod_name = ""
    pod_status = ""

    for pod in pods:
        if pod["memory"] > highest_mem:
            highest_mem = pod["memory"]
            pod_name = pod["name"]
            pod_status = pod["status"]

    return {
        "name": pod_name,
        "memory": highest_mem,
        "status": pod_status
    }


result = highest_memory_pod(pods)
print(result)




'''
Ek function banao:

def filter_pods_by_status(pods, status):

Jo given status ke hisaab se pods ki list return kare.


'''
 
def filter_pods_by_status(pods, status):
    running_pod = []
    for pod in pods:
        if pod["status"] == status:
            running_pod.append(pod)
    return running_pod
        
result = filter_pods_by_status(pods, "Running")
print(result)

