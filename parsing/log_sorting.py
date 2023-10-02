import re
from pathlib import Path
import sys


try:
	SEARCH_TAG = sys.argv[1]
except IndexError:
	SEARCH_TAG = 'ID'


SORTED_LOG_FILE_NAME = f'sorted_log_rssi_{SEARCH_TAG}.txt'
LOG_FILE_NAME = 'log_rssi.txt'
LOG_FILE_PATH = Path(__file__).parent/LOG_FILE_NAME
SORTED_LOG_FILE_NAME = Path(__file__).parent/SORTED_LOG_FILE_NAME


PATTERN = fr'.*{SEARCH_TAG} = (-?\d+)'

with open(LOG_FILE_NAME) as f:
	string = 'placeholder'
	items_list = []
	while string:
		string = f.readline()
		parsing_item = re.match(PATTERN, string)
		if parsing_item:
			items_list.append(parsing_item.group(1))



print(items_list)
