'''
Task 7 — Safe Pod Report

Ek function banao:

def safe_pod_report():

Function ko:

pods.json file read karni hai.
JSON ko Python object mein convert karna hai.

File missing ho toh:

ERROR: pods.json not found

print karo.

JSON invalid/corrupt ho toh:

ERROR: Invalid JSON

print karo.

Sab kuch sahi ho toh total pods count return karo.

Expected:

total = safe_pod_report()
print(total)

Output:

4

'''

'''

My Solution

def safe_pod_report():
    import json
    from pathlib import Path
    #pods.json file ka path/location path variable mein store karo.
    path = Path('pods.json')
    #path jis file ko point kar raha hai, us file ka poora text read karke content variable mein store karo.
    
    
    
    try:
        content = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
    #content mein jo JSON text/string hai, usko Python object (list/dictionary) mein convert karke pods mein store karo.
        pods = json.loads(content)
        
        total_count = 0
        for pod in pods:
            if pod["cpu"] >= 0:
                total_count += 1
        return total_count
                
            
    
total = safe_pod_report()
print(total)


'''

'''
Completed Solution by ChatGPT
'''
def safe_pod_report():
    import json
    from pathlib import Path

    path = Path("pods.json")

    try:
        content = path.read_text()
        pods = json.loads(content)

    except FileNotFoundError:
        print(f"ERROR: {path} not found")

    except json.JSONDecodeError:
        print("ERROR: Invalid JSON")

    else:
        return len(pods)


total = safe_pod_report()
print(total)