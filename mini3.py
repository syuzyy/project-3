import time

def countdown_timer(total_seconds):
    while total_seconds > 0:
        # Calculate hours, minutes, and seconds separately
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Display the formatted time on a new line
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        # Pause for one second
        time.sleep(1)

        # Decrement the remaining time
        total_seconds -= 1

    print("Time's up!")

def get_user_input():

    input_time = input("Insert time to countdown (h:m:s or m:s) ")                 # User input for the countdown time

    try:

        if ':' in input_time:                                                 # Check if hours are provided
            h, m, s = map(int, input_time.split(":"))
            total_seconds = h * 3600 + m * 60 + s
        else:
            m, s = map(int, input_time.split(":"))
            total_seconds = m * 60 + s

        return total_seconds
    except ValueError:
        print("Invalid input. Please enter time in the format (h:m:s or m:s).")     # Handle invalid input
        return get_user_input()

if __name__ == "__main__":
    countdown_time = get_user_input()
    countdown_timer(countdown_time)
