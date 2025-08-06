from collections import namedtuple

# Define Event namedtuple
Event = namedtuple('Event', ['date', 'type', 'machine', 'user'])

def main():
    events = [
        Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
        Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
        Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
        Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
        Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
        Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
    ]

    users = current_users(events)
    print(users)  # optional: for debugging
    generate_report(users)

# Helper function to get the date from the event
def get_event_date(event):
    return event.date

# Build dictionary of current users per machine
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].discard(event.user)  # discard avoids KeyError if user not found
    return machines

# Print a report of users still logged in per machine
def generate_report(machines):
    for machine, users in machines.items():
        if users:  # Only report machines with users
            user_list = ", ".join(users)
            print(f"{machine}: {user_list}")

if __name__ == "__main__":
    main()
