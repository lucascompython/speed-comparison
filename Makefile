

build: 
	@docker build -t lucascompython/speed-comparison .

run-docker:
	@docker run -it lucascompython/speed-comparison

run-native:
	@python3 ./comparison.py -c 25000
