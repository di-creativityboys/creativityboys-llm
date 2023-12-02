#!/usr/bin/env python3

import asyncio
import websockets
import json
import os
from dotenv import load_dotenv
from pretty_print import printSucces, printTask, printWarning
from task_plain import task_plain

load_dotenv()

HOST = os.getenv('WS_HOST') #localhost
PORT = os.getenv('WS_PORT')

async def handler(websocket):
    async for message in websocket:
        event = json.loads(message)

        task = event["task"]

        try:
            if task == "plain":
                await task_plain(websocket, event["options"])
            """if task == "query_data":
                await query_data(websocket, event["query"])
            if task == "som_mapsize":
                await som_mapsize(websocket, event["lattice"])
            if task == "som_train":
                await som_train(websocket, event["options"])
            if task == "boundaries_train":
                await boundaries_train(websocket, event["selection"])"""

        except Exception as e:
            printWarning(task)
            printWarning(str(e))
            await send_message(websocket, task, str(e))

async def send_message(websocket, body):
    printTask("message")

    response = {
        "task": "message",
        "body": body,
    }

    await websocket.send(json.dumps(response))

async def main():
    async with websockets.serve(handler, HOST, PORT):
        printSucces(f"Serving WebSocket on {HOST} at port {PORT}")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    printTask("LLM websocket service is starting")
    asyncio.run(main())