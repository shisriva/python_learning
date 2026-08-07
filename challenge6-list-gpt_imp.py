pods = [
    {"name": "api-server", "cpu": 2, "memory": 4096, "status": "Running"},
    {"name": "redis", "cpu": 1, "memory": 1024, "status": "Running"},
    {"name": "worker", "cpu": 4, "memory": 8192, "status": "Pending"},
    {"name": "database", "cpu": 2, "memory": 4096, "status": "Failed"},
    {"name": "llm-inference", "cpu": 4, "memory": 16384, "status": "Running"}
]



'''
🔥 Aaj ka Challenge (Function Task 6)

Ab tak hum functions se ek value ya ek list return kar rahe the.

Ab ek function summary report return karega.

Input:

pods = [
    {"name": "api-server", "cpu": 2, "memory": 4096, "status": "Running"},
    {"name": "redis", "cpu": 1, "memory": 1024, "status": "Running"},
    {"name": "worker", "cpu": 4, "memory": 8192, "status": "Pending"},
    {"name": "database", "cpu": 2, "memory": 4096, "status": "Failed"},
    {"name": "llm-inference", "cpu": 4, "memory": 16384, "status": "Running"}
]
Requirement

Function banao:

def cluster_summary(pods):

Ye function dictionary return kare jisme:

{
    "total_pods": 5,
    "running_pods": 3,
    "total_cpu": 13,
    "total_memory": 33792
}

Aur call:

result = cluster_summary(pods)
print(result)




'''


def cluster_summary(pods):
    total_pods = 0
    running_pods = 0
    total_cpu = 0
    total_memory = 0
    
    for pod in pods:

    # Har pod ke liye
    total_pods += 1

    # Har pod ke liye
    total_cpu += pod["cpu"]

    # Har pod ke liye
    total_memory += pod["memory"]

    # Sirf Running ke liye
    if pod["status"] == "Running":
        running_pods += 1
    

                
    return{
            "total_pods" : total_pods,
            "running_pods" : running_pods,
            "total_cpu": total_cpu,
            "total_memory": total_memory
            
        }
        
result = cluster_summary(pods)
print(result)