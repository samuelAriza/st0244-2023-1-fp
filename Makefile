# The source directory where the Python files are located
# Change this if your source files are in a different directory
SRC_DIR := src

# The test directory where the test files are located
# Change this if your test files are in a different directory
TEST_DIR := src

# The Python executable to be used
PYTHON := python3

# Get a list of all the test files in the test directory
TEST_FILES := $(wildcard $(TEST_DIR)/*.txt)

# Declare the phony targets (targets that are not actual files)
.PHONY: all run-tests test-suite run-all

# Default target that runs the test-suite target
all: test-suite

# Target to run individual tests one by one
run-tests:
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs1.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs2.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs3.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs4.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs5.txt

# Target to run the entire test suite
test-suite:
    # Loop over each test file and run the main.py script on it
	$(foreach file, $(TEST_FILES), $(PYTHON) $(SRC_DIR)/main.py $(file);)
