#REFER https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
# If the first argument is "run"...
ifeq (run,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(ARGS):;@:)
endif


build: 
	@docker build -t lucascompython/speed-comparison .

run-docker:
	@docker run -it lucascompython/speed-comparison:latest
#TODO fis this
run-native:
	@python3 ./comparison.py $(ARGS)
