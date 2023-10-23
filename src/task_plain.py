import json
from pretty_print import printTask
from llm import query_llm


async def task_plain(websocket, options):
    # Print colored task name
    printTask("plain")

    # Query llm with prompt
    llm_response = await query_llm(prompt=options["prompt"], 
                                   model_name=options["model"])

    # Response with tables attached
    response = {
        "task": "plain",
        "response": llm_response
    }

    # Send response
    await websocket.send(json.dumps(response))
