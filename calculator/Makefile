objects = main.o addition.o subtraction.o multiplication.o division.o

calculator: $(objects)
	cc -o calculator $(objects)

$(objects): %.o:%.c
	cc -c $< -o $@

all: calculator

clean:
	rm -f sample $(objects)

.PHONY: all
.PHONY: clean