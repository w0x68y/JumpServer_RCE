import asyncio
import re
 
import websockets
import json
 
url = "/ws/ops/tasks/log/"
 
async def main_logic(t):
    print("#######start ws")
    async with websockets.connect(t) as client:
        await client.send(json.dumps({"task":"/opt/jumpserver/logs/gunicorn"}))
        while True:
            ret = json.loads(await client.recv())
            print(ret["message"], end="")
 
if __name__ == "__main__":
    host = "http://192.168.111.162:8080"
    target = host.replace("https://", "wss://").replace("http://", "ws://") + url
    print("target: %s" % (target,))
    asyncio.get_event_loop().run_until_complete(main_logic(target))