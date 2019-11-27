all: clean comp

APP=clib

clean:
	rm -rf ./${APP}

comp:
	gcc -fPIC -shared -o ${APP}.so ${APP}.c
