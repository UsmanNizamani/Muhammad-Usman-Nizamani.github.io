# IP Allow List Updater

This Python script simulates a real-world scenario where a security analyst needs to manage an allow list of IP addresses stored in a text file. The script reads the file, removes IPs found in a separate removal list, and updates the file automatically.

## Features
- Reads and parses an IP allow list
- Removes specified IPs (e.g., blocked, revoked)
- Writes updated list back to the file

## Technologies
- Python 3
- File I/O
- Basic list handling

## How to Run

```bash
python3 update_allow_list.py

