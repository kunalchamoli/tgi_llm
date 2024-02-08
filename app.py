import subprocess
import requests
import time
from potassium import Potassium, Request, Response

# spawn shell process to start the server
cmd = "text-generation-launcher --model-id google/flan-t5-small"
process = subprocess.Popen(cmd, shell=True)

app = Potassium("server", experimental_num_workers=10)

@app.init
def init():
    # wait for TGI server to be available
    while True:
        try:
            requests.get("http://127.0.0.1:80")
            break
        except Exception as e:
            time.sleep(1)
    return {}

@app.handler(route="/generate")
def handler(context: dict, request: Request) -> Response:
    # forward request to TGI server
    data = request.json

    response = requests.post(
        'http://127.0.0.1:80/generate', 
        headers={
            "Content-Type": "application/json",
        }, 
        json=data
    )

    return Response(
        json = response.json(), 
        status=200
    )

if __name__ == "__main__":
    app.serve()