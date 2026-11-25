"""Count open items in a fictional support queue."""
import csv
import sys

with open(sys.argv[1], encoding="utf-8", newline="") as source:
    tickets = list(csv.DictReader(source))
print("Open items:", sum(ticket["status"] == "open" for ticket in tickets))
