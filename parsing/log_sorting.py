import re
from pathlib import Path
import sys

SORTED_LOG_FILE_NAME = 'sorted_log_rssi.txt'
LOG_FILE_NAME = 'log_rssi.txt'
LOG_FILE_PATH = Path(__file__).parent/LOG_FILE_NAME
SORTED_LOG_FILE_NAME = Path(__file__).parent/SORTED_LOG_FILE_NAME

try:
	SEARCH_TAG = sys.argv[1]
except IndexError:
	SEARCH_TAG = 'ID'


PATTERN = fr'{SEARCH_TAG} = (-?\d+)'

with open(LOG_FILE_NAME) as f:
	# while True:
	string = f.read()
	parsing_item = re.findall(PATTERN, string)
	# if parsing_item:
	# 	print(parsing_item.group())


print(set(list(map(int, parsing_item))))




# if __name__ == '__main__':
# 	print(LOG_FILE_PATH)