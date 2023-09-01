all: codeRunner run clean

codeRunner:
	g++ -Wall App.cpp -lm -o App

run:
	./App
	@echo ""

clean:
	rm -f *.exe
