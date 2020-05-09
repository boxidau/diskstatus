#!/usr/bin/env python3

import sys
import os
import re
import subprocess
from tabulate import tabulate


DISK_INVENTORY_FILE = os.path.expanduser("~/.config/disk_inventory")


def run_command(cmd):
  return subprocess.run(cmd, stdout=subprocess.PIPE)


def get_disk_inventory():
  disk_info = {}
  with open(DISK_INVENTORY_FILE, "r") as inv_file:
    lines = inv_file.readlines()
  for line in lines[1:]:
    pos, size, brand, serial = line.split(",")
    disk_info[serial.strip()] = {
      "position": int(pos.strip()),
      "size": int(size.strip()),
      "brand": brand.strip(),
      "serial": serial.strip()
    }
  return disk_info


def get_active_disks():
  disk_info = {}
  result = run_command(["lsblk", "--list", "-o", "TYPE,NAME,SERIAL,WWN"]).stdout.decode()
  for line in result.split("\n"):
    line_parts = re.sub(' +', ' ', line).split(" ")
    if line_parts[0] != "disk":
      continue
    disk_info[line_parts[2]] = {
      "name": line_parts[1],
      "serial": line_parts[2],
      "wwn": line_parts[3] if line_parts[3] else ""
    }
  return disk_info


def main():
  disk_inventory = get_disk_inventory()
  active_disks = get_active_disks()

  table_data = []
  
  columns = ["position", "name", "status", "size", "brand", "serial", "wwn"]
  
  for serial,disk in disk_inventory.items():
    merged_info = disk
    merged_info["status"] = "MISSING"
    
    if serial in active_disks:
      merged_info["status"] = "OK"
      merged_info.update(active_disks[serial])

    row = []
    for column in columns:
      if column in merged_info:
        row.append(merged_info[column])
      else:
        row.append("")
  
    table_data.append(row)

  print(tabulate(
    table_data,
    headers=columns,
  ))
  
if __name__ == "__main__":
  main()

