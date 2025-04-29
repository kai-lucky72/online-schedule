import asyncio
import websockets
import json
import subprocess

async def handler(websocket, path):
    async for message in websocket:
        schedule = json.loads(message)
        on_time = schedule['onTime']
        off_time = schedule['offTime']
        
        # Use mosquitto_pub to send schedule to MQTT
        # Adjust your MQTT topic and broker address accordingly
        mqtt_command = f"mosquitto_pub -h localhost -t 'light/schedule' -m '{on_time},{off_time}'"
        subprocess.run(mqtt_command, shell=True)
        print(f"Schedule received: ON at {on_time}, OFF at {off_time}")

start_server = websockets.serve(handler, 'localhost', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
