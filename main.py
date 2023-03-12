from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  