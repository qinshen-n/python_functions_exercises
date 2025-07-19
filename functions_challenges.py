#############################################################################################################
# Challenge 1 -> A Function to get a float from the user

def get_float(prompt_string: str):
    """A function that gets a float from the user and returns it.

    Arguments:
        - prompt_string: A string that will be shown to the user when they are
          prompted to input the number.

    Returns:
        - A float converted from the user's input
    """
    # pass
    user_input = input(prompt_string)
    return float(user_input)

# number = get_float("Please enter a number: ")
# print(f"The number you entered is {number}")

#############################################################################################################
# Challenge 2 -> A Function to convert miles to km
# NOTE: 1 mile is 1.60934km

def miles_to_km(distance_in_miles: float):
    """A function to convert distance from miles to km

    Arguments:
        - distance_in_miles: A float representing a distance in miles

    Returns
        - a float representing the distance in kilometers
    """
    # pass
    return distance_in_miles * 1.60934

# distance_in_miles = 2.5
# miles_to_km(distance_in_miles)
# print(f"The distance in miles {distance_in_miles} are {miles_to_km(distance_in_miles)} kms")


#############################################################################################################
# Challenge 3 -> A function to calculate the total distance run in a relay

def relay_distance(distance_per_runner: float, number_of_runners: float):
    """A function to calculate the total distance run by a team of runners
    in a relay race.

    Arguments:
        - distance_per_runner: a float representing the amount each runner runs
            (in a relay race, all runners run the same distance!)
        - number_of_runners: a float representing the number of runners in a team

    Returns:
        - A float representing the total distance run.
    """
    # pass
    return distance_per_runner * number_of_runners

# distance_per_runner = 5.5
# number_of_runners = 12
# print(f"The total distance run by a team of runners is {relay_distance(distance_per_runner, number_of_runners)}")

#############################################################################################################
# Challenge 4 (extra tricky)
#
# See if you can write a single function that USES all three of the functions
# you wrote for the above challenges.
def relay_distance_input():
    """A function that asks for a user's inputs for the number of runners and the distance each runner
    will run in a relay race in miles, and then calculate and return the total distance (in km) ran by
    all the runners.

    Arguments: None
        
    Returns:
        - A float representing the total distance run.
    """
    # pass
    user_input_number_runners = input("Please enter the number of runners: ")
    user_input_distance_per_runner_miles = input("Please enter the distance of each runner in miles: ")
    distance_per_runner_km = float(user_input_distance_per_runner_miles) * 1.60934
    return float(user_input_number_runners) * distance_per_runner_km

# print(f"The total distance (in km) ran by all the runners are {relay_distance_input()}")