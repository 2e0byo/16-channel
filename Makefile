.PHONY: all, clean, repl

.mirror/%.lock: firmware/%.py
	touch $@
	pkill mpfshell || echo 'no mpfshell running'
	mpfshell -o ttyUSB0 -n -c put $< $(<F)

all: .mirror/main.lock

.mirror/hal.lock:
.mirror/pca9685.lock:
.mirror/interface.lock: .mirror/hal.lock .mirror/pca9685.lock
.mirror/jsonrpc.lock:
.mirror/main.lock: .mirror/hal.lock .mirror/interface.lock .mirror/jsonrpc.lock

clean:
	rm -f .mirror/*.lock

repl:
	mpfshell -o ttyUSB0 -c repl

