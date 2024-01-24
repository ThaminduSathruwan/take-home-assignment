import json
from freeTimeSlotScheduler import FreeTimeSlotScheduler

def read_json_file(file_name):
    with open(file_name, "r") as f:
        return json.load(f)
    
def write_json_file(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def main():
    events = read_json_file("events.json")
    
    free_time_slot_scheduler = FreeTimeSlotScheduler(events)
    free_time_slots = free_time_slot_scheduler.get_free_time_slots()
    print(json.dumps(free_time_slots, indent=4))
    
    write_json_file("output.json", free_time_slots)
    
if __name__ == "__main__":
    main()