'''

Task 8 — Safe Pod Resource Report

pods.json read karke Running pods ka resource summary return karo.

Function:

def safe_resource_report():
Requirements
pods.json read karo.
JSON parse karo.

Agar file missing:

ERROR: pods.json not found

Agar JSON invalid:

ERROR: Invalid JSON
Sirf Running pods process karo.
Calculate karo:
total_running_pods
total_cpu
total_memory
Result ko dictionary ke form mein return karo.

Expected structure:

{
    "total_running_pods": 3,
    "total_cpu": 9,
    "total_memory": 18432
}
Bonus 🔥

Agar kisi pod mein "cpu" ya "memory" key missing ho, toh:

ERROR: Invalid pod data

print karo.



'''




def safe_resource_report():
    import json
    from pathlib import Path
    
    path = Path('pods.json')
    
    try:
        
        content = path.read_text()
        pods = json.loads(content)
        
    except FileNotFoundError:
        print(f'ERROR: {path} not found')
        
    except json.JSONDecodeError:
        print(f'ERROR: Invalid JSON')
        
    else:
        total_running = 0
        total_running_cpu = 0
        total_running_mem = 0
        for pod in pods:
            if pod["status"] == "Running":
                total_running += 1
                total_running_cpu += pod["cpu"]
                total_running_mem += pod["memory"]
        return{
        
        "total_running_pods" : total_running,
        "total_cpu" : total_running_cpu,
        "total_memory" : total_running_mem
              }
        
'''
Task 9 — Safe Resource Report File

Ab safe_resource_report() ke returned dictionary ko ek JSON file mein save karo.

Requirements
safe_resource_report() call karo.
Uska returned dictionary ek variable mein store karo.
resource_report.json naam ki file create karo.
Dictionary ko JSON format mein convert karo.
File mein write karo.
JSON readable hona chahiye (indent=4).

Expected resource_report.json:

{
    "total_running_pods": 3,
    "total_cpu": 9,
    "total_memory": 18432
}
'''    
        
result = safe_resource_report()

path = Path('resource_report.json')

# Json ko python object mein convert kar raha hai
content = json.dumps(result, indent=4)

# Path mein ja kar uss file mein write kar raha hai
path.write_text(content)


