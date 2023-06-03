SRC_DIR := src
TEST_DIR := src
PYTHON := python3
TEST_FILES := $(wildcard $(TEST_DIR)/*.txt)

.PHONY: all run-tests test-suite run-all

all: test-suite

run-tests:
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs1.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs2.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs3.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs4.txt
	$(PYTHON) $(SRC_DIR)/main.py $(TEST_DIR)/cs5.txt

test-suite:
	$(foreach file, $(TEST_FILES), $(PYTHON) $(SRC_DIR)/main.py $(file);)
