'''
records = [
    {"model": "llama", "latency_ms": 120, "status": "ok"},
    {"model": "mistral", "latency_ms": 95, "status": "ok"},
    {"model": "llama", "latency_ms": 300, "status": "error"},
    {"model": "qwen", "latency_ms": 80, "status": "ok"},
    {"model": "llama", "latency_ms": 150, "status": "ok"},
    {"model": "mistral", "latency_ms": 105, "status": "ok"},
]
Task: Print the average latency per model, considering only "ok" records.

Expected output (order doesn't matter):

llama average latency: 135.0 ms
mistral average latency: 100.0 ms
qwen average latency: 80.0 ms
(llama: (120+150)/2 = 135, mistral: (95+105)/2 = 100, qwen: 80/1 = 80)

'''




records = [
    {"model": "llama", "latency_ms": 120, "status": "ok"},
    {"model": "mistral", "latency_ms": 95, "status": "ok"},
    {"model": "llama", "latency_ms": 300, "status": "error"},
    {"model": "qwen", "latency_ms": 80, "status": "ok"},
    {"model": "llama", "latency_ms": 150, "status": "ok"},
    {"model": "mistral", "latency_ms": 105, "status": "ok"},
]
totals = {} 
counts = {}


for record in records:
    if record["status"] == "ok":
        model = record["model"]
        latency = record["latency_ms"]


