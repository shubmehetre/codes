import sys
import time
import notify2

def notify_time_up():
    # Initialize the D-Bus connection
    notify2.init("Timer App")

    # Create a notification object
    notification = notify2.Notification("Time's Up!", "Your timer has ended.\
    Stop what you are doing RIGHT NOW ! Take a Break. Do a Mental Revision")
    notification.set_urgency(notify2.URGENCY_CRITICAL)

    # Show the notification
    notification.show()

def start_timer(minutes):
    # Convert minutes to seconds
    seconds = minutes * 60

    # Start the timer
    print(f"Timer started for {minutes} minute(s).")
    time.sleep(seconds)

    # Notify when time is up
    notify_time_up()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python timer.py <minutes>")
        sys.exit(1)

    try:
        # Get the time (in minutes) from the command-line argument
        minutes = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for minutes.")
        sys.exit(1)

    # Start the timer
    start_timer(minutes)

