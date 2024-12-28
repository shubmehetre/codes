# Compiler and flags
CC = gcc
CFLAGS = -Wall -g

# Object files
OBJS = main.o basics.o

# Target executable
TARGET = output

# Build the executable
$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

# Compile each source file into an object file
main.o: main.c basics.h
	$(CC) -c main.c -o main.o

basics.o: basics.c basics.h
	$(CC) -c basics.c -o basics.o

# Clean up build files
clean:
	rm -f $(OBJS) $(TARGET)

