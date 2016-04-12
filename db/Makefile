db:
	docker build -t "openroads-db:base" .

test-db: db
	docker build -t "openroads-db:test" extensions/test/

clean:
	docker ps -a | grep openroads-db | awk '{print $1}' | xargs docker rm && \
	docker images | grep 'openroads-db' | awk '{print $1":"$2}' | xargs docker rmi
