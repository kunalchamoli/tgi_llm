# tgi-demo
A demo of high throughput llm serving with TGM

# What this is

Source for building a docker container containing:

### TGI server
A single TGI server runs per container.
It is ran via `text-generation-launcher` CLI, in a process spawned by the potassium server.

### Potassium Server
A single Potassium server runs per container, and its job is to proxy calls to TGI

It is necessary to integrate with Banana, to track concurrent jobs.

Multiple http workers may be spawned using the `experimental_num_workers=10` argument.

# To use

From a GPU machine with Docker and [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed, run:

```bash
bash build_and_run.sh
```

This will build the docker container from the Dockerfile, and run it with the necessary ports exposed.

Call it with a post request in the example client.py

```bash
python3 client.py
```