# This is where we install
BIN=/Users/pf98/work/bin

# This is the source directory
DIR=/Users/pf98/work/code/cal2014/gcaltimetracker

default:
	# by default, this Makefile does nothing, for safety

install:
	ln -s $(DIR)/atp.py $(BIN)/atp.py
	ln -s $(DIR)/gcalcli_count.py $(BIN)/gcalcli_count.py
	ln -s $(DIR)/how_much_did_i_work.sh $(BIN)/how_much_did_i_work.sh
	ln -s $(DIR)/how_much_did_i_work_per_week.sh $(BIN)/how_much_did_i_work_per_week.sh
	ln -s $(DIR)/how_much_will_i_work.sh $(BIN)/how_much_will_i_work.sh
	ln -s $(DIR)/todo_backlog.sh $(BIN)/todo_backlog.sh
	chmod +x $(BIN)/

clean-install:
	rm -f $(BIN)/atp.py
	rm -f $(BIN)/gcalcli_count.py
	rm -f $(BIN)/how_much_did_i_work.sh
	rm -f $(BIN)/how_much_did_i_work_per_week.sh
	rm -f $(BIN)/how_much_will_i_work.sh
	rm -f $(BIN)/todo_backlog.sh
