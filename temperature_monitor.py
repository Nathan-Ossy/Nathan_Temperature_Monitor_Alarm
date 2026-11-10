# Temperature Monitor and Alarm Checker
# Reads 5 machine temperatures, shows the highest, lowest and average,
# warns about unsafe readings, and (my own twist) shows operator action
# prompts for BOTH the highest reading (hot spots) and the average (overall trend),
# based on how far each is above the safe limit the user sets.

import math  # used to reject invalid values such as "nan" and "inf"

NUMBER_OF_READINGS = 5   # how many temperature readings to collect
ZONE_WIDTH = 10          # each danger zone is 10 degrees wide
ABSOLUTE_ZERO = -273.15  # no temperature in Celsius can be lower than this


def get_number(message):
    """Keep asking until the user types a valid temperature, then return it."""
    while True:
        text = input(message)
        try:
            # Convert the typed text into a decimal number
            value = float(text)
        except ValueError:
            # The user typed letters or symbols instead of a number
            print("Invalid input. Please type a number, for example 75.5")
            continue

        # float() accepts "nan" and "inf", so check for those separately
        if not math.isfinite(value):
            print("Invalid input. Please type a real number.")
        elif value < ABSOLUTE_ZERO:
            print("That is below absolute zero (-273.15 C). Try again.")
        else:
            return value


def format_temperature(celsius):
    """Return a temperature as text in both Celsius and Fahrenheit."""
    # Fahrenheit = Celsius x 9/5 + 32
    fahrenheit = celsius * 9 / 5 + 32
    return f"{celsius:.1f} C ({fahrenheit:.1f} F)"


def get_zone_prompt(temperature, safe_limit):
    """Return the zone name and a short operator prompt for a temperature."""
    # How many degrees the temperature is above the safe limit
    excess = temperature - safe_limit

    if excess <= 0:
        return "SAFE", "Temperature is within the safe limit. No action needed."
    elif excess < ZONE_WIDTH:
        return "ALERT ZONE", (
            "Reduce the workload by 50%. "
            "Keep the cooling fans at maximum."
        )
    elif excess < 2 * ZONE_WIDTH:
        return "CRITICAL WARNING ZONE", (
            "Start a controlled shutdown. "
            "Stop operations and power off the machine."
        )
    elif excess < 3 * ZONE_WIDTH:
        return "EMERGENCY ZONE", (
            "Evacuate the area. "
            "Check the temperature from a distance with an infrared thermometer. "
            "Do not touch the machine or open any caps."
        )
    else:
        return "CATASTROPHIC DANGER ZONE", (
            "Cut the main breaker power. "
            "Keep fire extinguishers ready. "
            "Do not approach until the machine has been idle for several hours."
        )


def show_zone_report(label, temperature, safe_limit):
    """Print the zone status and operator action for one temperature."""
    zone, prompt = get_zone_prompt(temperature, safe_limit)
    print(f"\n{label}: {format_temperature(temperature)}")
    print(f"Status: {zone}")
    print(f"Action: {prompt}")


def main():
    """Run the temperature monitor."""
    print("=== Temperature Monitor and Alarm Checker ===")

    # Let the user set the safe limit (my own twist)
    safe_limit = get_number("Enter the safe temperature limit (C): ")

    # Collect the readings in a list using a loop
    readings = []
    for number in range(1, NUMBER_OF_READINGS + 1):
        reading = get_number(f"Enter reading {number} (C): ")
        readings.append(reading)

    # Work out the highest, lowest and average
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    print("\n--- Results ---")
    print(f"Readings (C): {readings}")
    print(f"Highest: {format_temperature(highest)}")
    print(f"Lowest: {format_temperature(lowest)}")
    print(f"Average: {format_temperature(average)}")
    print(f"Safe limit: {format_temperature(safe_limit)}")

    # Warn about every reading that is above the safe limit
    print("\n--- Reading check ---")
    unsafe_count = 0
    for number, reading in enumerate(readings, start=1):
        if reading > safe_limit:
            print(f"WARNING: Reading {number} is {format_temperature(reading)}, above the safe limit!")
            unsafe_count += 1

    if unsafe_count == 0:
        print("All readings are within the safe limit.")

    # Show operator prompts for both the highest reading and the average (my own twist)
    # The highest reading catches dangerous hot spots that an average can hide
    # The average shows the overall heating trend and ignores one-off sensor errors
    print("\n--- Operator prompts ---")
    show_zone_report("Hot spot check (highest reading)", highest, safe_limit)
    show_zone_report("Overall trend (average)", average, safe_limit)


# Start the program only when this file is run directly
if __name__ == "__main__":
    main()
