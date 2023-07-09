.PHONY: all, clean, repl

# MPFSHELL="mpfshell -o ttyUSB0"
MPFSHELL="/usr/bin/mpfshell -o ws:192.168.0.162,repl"

.mirror/%.lock: firmware/%.py
	touch $@
	pkill mpfshell || echo 'no mpfshell running'
	"${MPFSHELL}" -n -c put $< $(<F)

all: .mirror/main.lock

.mirror/hal.lock:
.mirror/pca9685.lock:
.mirror/interface.lock: .mirror/hal.lock .mirror/pca9685.lock
.mirror/jsonrpc.lock:
.mirror/conn.lock:
.mirror/env.lock:
.mirror/main.lock: .mirror/hal.lock .mirror/interface.lock .mirror/jsonrpc.lock .mirror/conn.lock .mirror/env.lock

clean:
	rm -f .mirror/*.lock

repl:
	"${MPFSHELL}" -c repl

