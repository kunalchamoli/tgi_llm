docker build -t potassium .

volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run
docker run --gpus all --shm-size 1g -p 8080:80 -p 8000:8000 -v $volume:/data potassium