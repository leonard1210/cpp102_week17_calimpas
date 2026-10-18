def get_initial_readings():
    """Return the initial list of temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True if text represents a valid whole number (including negatives)."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def display_readings(readings):
    """Display all current readings with their position numbers."""
    print("CURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings, lowest, highest):
    """Prompt for a new reading, validate it, and append if valid."""
    text = input("Enter new reading: ")
    print()  # Blank line to match expected spacing
    
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        value = int(text)
        if value < lowest or value > highest:
            print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
        else:
            readings.append(value)
            print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL classification for a given reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings, warning_limit, critical_limit):
    """Display the classification of every reading in the list."""
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Calculate and return the sum of all readings using a loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Calculate and return the average of all readings."""
    if len(readings) == 0:
        return 0.0
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Find and return the smallest reading using a loop."""
    if len(readings) == 0:
        return 0
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Find and return the largest reading using a loop."""
    if len(readings) == 0:
        return 0
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Count and return how many readings fall under a specific category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Determine overall system status based on warning and critical counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings, warning_limit, critical_limit):
    """Display numerical calculations, category distributions, and overall status."""
    total_readings = len(readings)
    if total_readings == 0:
        print("No readings available to generate summary.")
        return

    total = compute_total(readings)
    avg = compute_average(readings)
    min_val = find_minimum(readings)
    max_val = find_maximum(readings)

    normal_cnt = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning_cnt = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical_cnt = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    normal_pct = (normal_cnt / total_readings) * 100
    warning_pct = (warning_cnt / total_readings) * 100
    critical_pct = (critical_cnt / total_readings) * 100

    overall_status = determine_overall_status(warning_cnt, critical_cnt)

    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {total_readings}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {avg:.2f} °C")
    print(f"Minimum temperature : {min_val} °C")
    print(f"Maximum temperature : {max_val} °C")
    print()
    print(f"NORMAL   : {normal_cnt} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_cnt} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_cnt} ({critical_pct:.2f}%)")
    print()
    print(f"Overall Status: {overall_status}")


def display_menu():
    """Display the main system menu options."""
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()


def main():
    """Control main application execution and user interaction menu loop."""
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("Enter choice: ")
        print()  # Blank line to match expected spacing

        if choice == "1":
            display_readings(readings)
            print()
        elif choice == "2":
            add_reading(readings, 0, 100)
            print()
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
            print()
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
            print()
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            print()


main()
