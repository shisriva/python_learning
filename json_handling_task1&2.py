'''

Task 1
import json
pods.json naam ki file create karo.
Usme upar wala pods data write karo.

Expected file:

[
    {
        "name": "api-server",
        "cpu": 2,
        "memory": 4096,
        "status": "Running"
    },
    ...
]

'''



from pathlib import Path
import json 

'''
pods = [
    {
        "name": "api-server",
        "cpu": 2,
        "memory": 4096,
        "status": "Running"
    },
    {
        "name": "redis",
        "cpu": 1,
        "memory": 1024,
        "status": "Running"
    },
    {
        "name": "worker",
        "cpu": 4,
        "memory": 8192,
        "status": "Pending"
    }
]

path = Path('pods.json')

content = json.dumps(pods)

path.write_text(content)


'''

'''
Task2: Read Data from already present file

'''


path = Path('pods.json')
content = path.read_text()
pods = json.loads(content)

print(pods)
