FROM ghcr.io/huggingface/text-generation-inference:1.3

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD app.py .

ENTRYPOINT python3 -u app.py