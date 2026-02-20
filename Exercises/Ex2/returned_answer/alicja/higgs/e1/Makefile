# Compiler 
CXX = g++

# Compiler class
CXXFLAGS = -Wall -g

# Target executable
TARGET = ex2

# For delating the target
TARGET_DEL = ex2.exe

# Source file
SRCS = ex2.cpp

# Object file
OBJC = $(SRCS:.cpp=.o)

# Default rule to build and run the executable
all: $(TARGET)

# rule to link object files into the target executable
$(TARGET): $(OBJC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJC)

# Rule to compile .cpp files into o. files
%.o:%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean rule to remove generated files
clean:
	del $(TARGET_DEL) $(OBJC)


