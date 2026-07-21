'''
Given this list of model-serving records:

records = [
    {"model": "llama", "latency_ms": 120, "status": "ok"},
    {"model": "mistral", "latency_ms": 95, "status": "ok"},
    {"model": "llama", "latency_ms": 300, "status": "error"},
    {"model": "qwen", "latency_ms": 80, "status": "ok"},
]
Write a program that:

Loops through the records.
Prints only records whose status is "ok".
Prints them in this format:

llama responded in 120 ms
mistral responded in 95 ms
qwen responded in 80 ms

'''


records = [
    {"model": "llama", "latency_ms": 120, "status": "ok"},
    {"model": "mistral", "latency_ms": 95, "status": "ok"},
    {"model": "llama", "latency_ms": 300, "status": "error"},
    {"model": "qwen", "latency_ms": 80, "status": "ok"},
]

for i in records:
    if i["status"] == "ok":
        print(f'{i["model"]} responded in {i["latency_ms"]} ms')
