
def log_fitness_activities(activities, durations):
    if len(activities) != len(durations):
        print("Error: Length of activities list does not match length of durations list.")
        return
    
    fitness_log = {}  # Initialize an empty dictionary to store activity-duration pairs
    
    # Loop through activities and durations to populate the fitness_log dictionary
    for i in range(len(activities)):
        activity = activities[i]
        duration = durations[i]
        fitness_log[activity] = duration
    
    return fitness_log

# Example usage:
activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]

fitness_log = log_fitness_activities(activities, durations)
print("Fitness Log:")
for activity, duration in fitness_log.items():
    print(f"{activity}: {duration} minutes")



def estimate_calories_burned(activity, duration):
    calories_per_minute = {
        'Dancing': 7,
        'Swimming': 10,
        'Biking': 8,
        # Add more activities and their respective calories burned per minute here
    }

    if activity in calories_per_minute:
        calories_per_minute_activity = calories_per_minute[activity]
        calories_burned = calories_per_minute_activity * duration
        return calories_burned
    else:
        print(" not found in database.")
        return None

activity = 'Swimming'
duration = 20  

calories_burned = estimate_calories_burned(activity, duration)
if calories_burned is not None:
    print(f"Estimated calories burned from {activity} for {duration} minutes: {calories_burned} calories")
    
def daily_activity_summary(activities):
    # Define a dictionary with calorie burn rates per minute for various activities
    calorie_burn_rate = {
        'dancing': 10,
        'biking': 8,
        'swimming': 10,
       
    }
    
    total_calories = 0

    summary = {}
    
    # Loop through the list of activities
    for activity, duration in activities:
        if activity in calorie_burn_rate:
            calories = calorie_burn_rate[activity] * duration
            total_calories += calories
            summary[activity] = summary.get(activity, 0) + calories
    summary['total'] = total_calories
    return summary
activities = [('biking', 30), ('dancing', 60), ('swimming', 45)]
print(daily_activity_summary(activities))  # Output: {'running': 300, 'cycling': 480, 'swimming': 315, 'total': 1095}


