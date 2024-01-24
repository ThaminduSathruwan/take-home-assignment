from datetime import datetime, timedelta

class FreeTimeSlotScheduler:
    def __init__(self, events):
        self.events = events
        
    def sort_events(self):
        self.events.sort(key=lambda x: x['start']['dateTime'])
        
    def calculate_free_time_slots(self):
        self.sort_events()
        free_time_slots = []
        
        start_of_day = datetime.strptime(self.events[0]['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z').replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = datetime.strptime(self.events[-1]['end']['dateTime'], '%Y-%m-%dT%H:%M:%S%z').replace(hour=23, minute=59, second=59, microsecond=0)
        
        current_time = datetime.strptime(self.events[0]['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
        end_time = datetime.strptime(self.events[-1]['end']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
        
        if current_time > start_of_day:
            free_time_slots.append({'start': start_of_day, 'end': current_time})
        
        for event in self.events:
            start_time = datetime.strptime(event['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
            if start_time > current_time:
                free_time_slots.append({'start': current_time, 'end': start_time})
            current_time = datetime.strptime(event['end']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
            
        if end_time < end_of_day:
            free_time_slots.append({'start': end_time, 'end': end_of_day})
            
        return free_time_slots
    
    def get_free_time_slots(self):
        free_time_slots = self.calculate_free_time_slots()
        time_slots = {}
        
        for time_slot in free_time_slots:
            temp_start_date = time_slot['start'].strftime('%Y-%m-%d')
            temp_end_date = time_slot['end'].strftime('%Y-%m-%d')
            start_time = time_slot['start'].strftime('%H:%M:%S')
            end_time = time_slot['end'].strftime('%H:%M:%S')
            if temp_start_date == temp_end_date:
                if temp_start_date in time_slots:
                    time_slots[temp_start_date].append({'start_time': start_time, 'end_time': end_time})
                else:
                    time_slots[temp_start_date] = [{'start_time': start_time, 'end_time': end_time}]        
            else:
                while temp_start_date != temp_end_date:
                    if temp_start_date in time_slots:
                        time_slots[temp_start_date].append({'start_time': start_time, 'end_time': '23:59:59'})
                    else:
                        time_slots[temp_start_date] = [{'start_time': start_time, 'end_time': '23:59:59'}]
                    temp_start_date = (datetime.strptime(temp_start_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
                    start_time = '00:00:00'
                
                time_slots[temp_start_date] = [{'start_time': start_time, 'end_time': end_time}]
                    
        return time_slots

        

        
