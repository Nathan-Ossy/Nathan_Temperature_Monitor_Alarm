# Temperature Monitor and Alarm Checker

## What it does

This Python program reads five machine temperatures in Celsius and shows the highest, lowest and average, with each value also given in Fahrenheit. It warns the operator about every reading above a safe limit that the operator sets. It then shows a short action prompt based on how far the temperature is above that limit.

## How to run it

Install Python 3, then run:

```
python temperature_monitor.py
```

Type the safe limit first, then the five readings. If you type something that is not a number, the program asks again.

## Sample output

```
=== Temperature Monitor and Alarm Checker ===
Enter the safe temperature limit (C): 80
Enter reading 1 (C): 60
Enter reading 2 (C): 90
Enter reading 3 (C): 80
Enter reading 4 (C): 130
Enter reading 5 (C): djr
Invalid input. Please type a number, for example 75.5
Enter reading 5 (C): 60

--- Results ---
Readings (C): [60.0, 90.0, 80.0, 130.0, 60.0]
Highest: 130.0 C (266.0 F)
Lowest: 60.0 C (140.0 F)
Average: 84.0 C (183.2 F)
Safe limit: 80.0 C (176.0 F)

--- Reading check ---
WARNING: Reading 2 is 90.0 C (194.0 F), above the safe limit!
WARNING: Reading 4 is 130.0 C (266.0 F), above the safe limit!

--- Operator prompts ---

Hot spot check (highest reading): 130.0 C (266.0 F)
Status: CATASTROPHIC DANGER ZONE
Action: Cut the main breaker power. Keep fire extinguishers ready. Do not approach until the machine has been idle for several hours.

Overall trend (average): 84.0 C (183.2 F)
Status: ALERT ZONE
Action: Reduce the workload by 50%. Keep the cooling fans at maximum.
```

## My own twist

1. **Adjustable safe limit:** the operator types the safe limit for the machine, so the program works for machines with different limits.
2. **Danger zones with operator prompts:** the zones start at the safe limit and each is 10 degrees wide. Each zone shows a short action for the operator:
   - **Alert Zone** (0 to 10 degrees above the limit): reduce the workload by 50% and keep the cooling fans at maximum.
   - **Critical Warning Zone** (10 to 20 degrees above): start a controlled shutdown.
   - **Emergency Zone** (20 to 30 degrees above): evacuate and check the temperature from a distance.
   - **Catastrophic Danger Zone** (more than 30 degrees above): cut the main breaker power and keep fire extinguishers ready.
3. **Two prompts, not one:** the program gives a prompt for the highest reading and another for the average. The highest reading catches dangerous hot spots, and the average shows the overall heating trend.
4. **Celsius and Fahrenheit:** every temperature is shown in both units.
5. **Input checking:** letters, blank entries and impossible temperatures (below -273.15 C) are rejected, and the program asks again.

## What I learned

1. The average temperature avoids false alarms but can hide danger. For example, readings of 70, 70, 70, 70 and 120 with a safe limit of 80 give an average of exactly 80, which looks safe even though one part of the machine is at 120 C. The highest reading catches danger like this, but one faulty sensor can cause a false alarm. Real monitoring systems usually base the alarm on the highest reading and use the average only to watch the trend, so I show both.
2. User input cannot be trusted. My first version crashed when I typed a letter, so I used `try/except` inside a `while` loop to keep asking until the input is valid.
3. Breaking the program into small functions (`get_number`, `format_temperature`, `get_zone_prompt` and `show_zone_report`) made it easier to test and change, for example when I added Fahrenheit.

## Author

Osigbemhe Nathan Oluwaseyi, ND1 Mechatronics Engineering, YabaTech.
