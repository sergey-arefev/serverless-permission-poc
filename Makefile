DOCKER_REGISTRY=cr.yandex/crp1gs30bam49ookc3cc
CONTAINER_NAME=serverless-permission-poc

build_local:
	docker build -f Dockerfile -t local/$(CONTAINER_NAME):latest ./

run_local:
	docker run -e PORT=9999 -p 9999:9999 --rm local/$(CONTAINER_NAME):latest python3 /agent/launch.py

build_and_push:
	docker build -f Dockerfile -t $(DOCKER_REGISTRY)/$(CONTAINER_NAME):latest ./
	docker push $(DOCKER_REGISTRY)/$(CONTAINER_NAME):latest