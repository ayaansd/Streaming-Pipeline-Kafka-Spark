
import time, json, random, sys
from datetime import datetime

def gen_event(i):
    return {
        "event_id": i,
        "ts": datetime.utcnow().isoformat(),
        "type": random.choice(["view","apply","save"]),
        "job_id": random.randint(1000, 9999),
    }

for i in range(20):
    e = gen_event(i)
    print(json.dumps(e))
    time.sleep(0.2)
print("✅ mock stream done")
