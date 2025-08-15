import os 
import json 

# 2. Normal workflow
# Manager --> Master JSON () ---> Packets --> retrieve that json ---> return 

"""
Objective: 
This file will iterate over the memories folder, 
visit the json files and 
create a master json files that can act as a navigation guide to where to head for what data
"""


def create_master_json(memories_folder, output_file):

  navigation_list = [] 

  for file in os.listdir(memories_folder):
    file_path = os.path.join(memories_folder, file)
  
    with open(file_path, "r", encoding="utf-8") as f:
      data = json.load(f)

      # Validate required keys
      if all(key in data for key in ["name", "location", "description"]):
          navigation_list.append({
              "name": data["name"],
              "location": data["location"],
              "description": data["description"]
          })
  
  master_path = os.path.join(memories_folder, output_file)
  with open(master_path, "w", encoding="utf-8") as f:
      json.dump({"navigation": navigation_list}, f, indent=4)
    

create_master_json("Memories", "Master_Json.json")