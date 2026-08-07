
'''
Task1: Print Running Pods names from the given json file pods.json

'''


def running_pods_json():
    from pathlib import Path
    import json

    path = Path('pods.json')

    content = path.read_text()

    pod = json.loads(content)

    for container in pod:
        if container["status"] == "Running":
            print(container["name"])
        
    
'''
Task2: Ab Task 2 ke liye isi code mein Running pods ka total CPU aur memory calculate

'''


def calc_running_mem_cpu():
    from pathlib import Path
    import json
    
    path = Path('pods.json')
    content = path.read_text()
    pods = json.loads(content)
    
    
    con_cpu = 0
    con_mem = 0
    
    for container in pods:
        if container["status"] == "Running":
            con_cpu += container["cpu"]
            con_mem += container["memory"]
            
    print("Total CPU:", con_cpu)
    print("Total Memory:", con_mem)


'''
Task 3 (Highest CPU consuming Running pod)
Nested IF statement Used
'''


def max_cpu_pod():
    from pathlib import Path
    import json
    
    path = Path('pods.json')
    content = path.read_text()
    pods = json.loads(content)
    
    max_cpu = 0
    pod_name = ""
    for container in pods:
        if container["status"] == "Running":
            if container["cpu"] > max_cpu:
                max_cpu = container["cpu"]
                pod_name = container["name"]
            
    print(f'Max CPU consuming POD: {pod_name}')
    
    
    
'''
Task 4: Pod Summary Report

pods.json file ko read karke ek summary dictionary banao.

Dictionary mein ye information honi chahiye:

Total Running Pods
Total CPU of Running Pods
Total Memory of Running Pods
Highest CPU consuming Running Pod

Expected output format:

{
    "total_running_pods": 0,
    "total_cpu": 0,
    "total_memory": 0,
    "highest_cpu_pod": ""
}
'''

def summary_pods():
    import json
    from pathlib import Path
    
    path = Path('pods.json')
    content = path.read_text()
    pods = json.loads(content)
    
    total_cpu = 0
    total_memory = 0
    highest_cpu_pod = ""
    running_pod = 0
    max_running_cpu = 0
    for container in pods:
        if container["status"] == "Running":
            running_pod += 1
            total_cpu += container["cpu"]
            total_memory += container["memory"]
            if container["cpu"] > max_running_cpu:
               max_running_cpu = container["cpu"]
               highest_cpu_pod = container["name"]
    return {
        
    "total_running_pods": running_pod,
    "total_cpu": total_cpu,
    "total_memory": total_memory,
    "highest_cpu_pod": highest_cpu_pod
        
        
        
    }           
            
            

        