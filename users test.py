"""
user_service.py

Synthetic test file for the AI code review pipeline.
Contains DELIBERATE bugs, security issues, and style violations,
each tagged with an ISSUE-<n> comment so they can be matched
against user_service_ground_truth.json for detection-rate scoring.
dshwgdsjwgduwd
DO NOT use this file's patterns as reference for real code.
"""
//test
import sqlite3
import os
import hashlib

API_KEY = "sk-live-4f9a2b7c1e6d8f3a0b5c9d2e7f1a4b6c"  # ISSUE-1: hardcoded secret


def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # ISSUE-2: SQL injection via string formatting instead of parameterized query
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchone()


def run_backup(filename):
    # ISSUE-3: command injection — filename is passed straight to the shell
    os.system("tar -czf backup.tar.gz " + filename)


def hash_password(password):
    # ISSUE-4: weak hashing algorithm for passwords (MD5, no salt)
    return hashlib.md5(password.encode()).hexdigest()


def add_item(items=[]):  # ISSUE-5: mutable default argument
    items.append("new_item")
    return items
//test

def get_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)  # ISSUE-6: division by zero if numbers is empty


def get_last_n(items, n):
    # ISSUE-7: off-by-one — should be items[-n:] or range adjusted;
    # this silently drops the final element
    result = []
    for i in range(len(items) - n, len(items) - 1):
        result.append(items[i])
    return result


def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:  # ISSUE-8: bare except swallows all errors, including KeyboardInterrupt
        return None


def calculate_discount(price, userInput):
    # ISSUE-9: eval() on user-controlled input — arbitrary code execution
    discount = eval(userInput)
    return price - discount


def process_payment(amount, account_id):
    # ISSUE-10: no validation that amount is positive/non-zero before charging
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",
        (amount, account_id),
    )
    conn.commit()


import json  # ISSUE-11 (style): import not at top of file, and unused
