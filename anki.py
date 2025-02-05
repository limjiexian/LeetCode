from datetime import datetime, timedelta
import random

def calculate_next_review(current_interval, ease_factor, grade, status, easy_bonus=1.1, max_interval=365):
    """
    Calculate the next review interval and ease factor based on the grade and status.

    Parameters:
    - current_interval (int): Current interval in days.
    - ease_factor (float): Current ease factor.
    - grade (str): Review grade ("Again", "Hard", "Good", "Easy", "Very Easy").
    - status (str): Current status ("Learning", "Graduated", "Mature", "Relearning").
    - easy_bonus (float): The multiplier for "Easy" grades.
    - max_interval (int): The maximum interval cap.

    Returns:
    - next_interval (int): The calculated next interval in days.
    - next_ease_factor (float): The updated ease factor.
    - next_review_date (datetime): The calculated next review date.
    - next_status (str): The updated status of the card.
    """
    if status == "Learning":
        # Logic for new cards
        if grade == "Again":
            next_interval = 1
            ease_factor = max(1.3, ease_factor - 0.15)
            next_status = "Learning"
        elif grade == "Hard":
            next_interval = 2
            ease_factor = max(1.3, ease_factor - 0.1)
            next_status = "Learning"
        elif grade == "Good":
            next_interval = 3
            next_status = "Learning"
        elif grade == "Easy":
            next_interval = 4
            ease_factor = 2.5
            next_status = "Graduated"
        elif grade == "Very Easy":
            next_interval = 5
            ease_factor = 2.5
            next_status = "Graduated"
        else:
            raise ValueError("Invalid grade for Learning status.")
    
    elif status in ["Graduated", "Mature"]:
        # Logic for graduated/mature cards
        if grade == "Again":
            next_interval = 1  # Reset interval for relearning
            ease_factor = 2.3  # Reset ease factor for relearning
            next_status = "Relearning"
        elif grade == "Hard":
            next_interval = min(round(current_interval * 1.2), max_interval)
            ease_factor = max(1.3, ease_factor - 0.15)
            next_status = status
        elif grade == "Good":
            base_interval = current_interval * ease_factor
            random_factor = random.uniform(0.9, 1.1)  # Add fuzz
            next_interval = min(round(base_interval * random_factor), max_interval)
            next_status = "Mature" if next_interval > 180 else "Graduated"
        elif grade == "Easy":
            base_interval = current_interval * ease_factor
            random_factor = random.uniform(0.9, 1.1)  # Add fuzz
            next_interval = min(round(base_interval * random_factor), max_interval)
            ease_factor = 2.65
            next_status = "Mature" if next_interval > 180 else "Graduated"
        elif grade == "Very Easy":
            base_interval = current_interval * ease_factor * easy_bonus
            random_factor = random.uniform(0.9, 1.1)  # Add fuzz
            next_interval = min(round(base_interval * random_factor), max_interval)
            ease_factor = 2.75
            next_status = "Mature" if next_interval > 180 else "Graduated"
        else:
            raise ValueError("Invalid grade for Graduated/Mature status.")
    
    elif status == "Relearning":
        # Relearning steps logic
        relearn_steps = [1, 2, 4, 7]  # Define relearning steps
        if grade == "Again":
            next_interval = relearn_steps[0]
            next_status = "Relearning"
        elif grade in ["Hard", "Good", "Easy"]:
            # Progress to the next step
            current_step_index = relearn_steps.index(current_interval) if current_interval in relearn_steps else 0
            next_step_index = min(current_step_index + 1, len(relearn_steps) - 1)
            next_interval = relearn_steps[next_step_index]
            next_status = "Graduated" if next_interval == relearn_steps[-1] else "Relearning"
        else:
            raise ValueError("Invalid grade for Relearning status.")
    
    else:
        raise ValueError("Invalid status.")
    
    # Calculate the next review date
    next_review_date = datetime.now() + timedelta(days=next_interval)
    return next_interval, ease_factor, next_review_date, next_status

def get_valid_input(prompt, valid_choices):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_choices:
            return user_input
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    print("\n--- Spaced Repetition System ---")
    
    # Ask the user if this is a brand-new card
    is_new_card = get_valid_input("Is this a brand-new card? (yes/no): ", ["yes", "no", "y", "n"])
    
    if is_new_card in ["yes", "y"]:
        # Default values for a brand-new card
        current_interval = 1  # Default interval
        ease_factor = 2.5  # Default ease factor
        status = "Learning"  # Default status
        print("\nAssuming this is a brand-new card. Default values applied.")
    else:
        # Input for an existing card
        while True:
            try:
                current_interval = int(input("Enter the current interval (days): "))
                ease_factor = float(input("Enter the current ease factor: "))
                status = get_valid_input(
                    "Enter the current status (Learning, Graduated, Mature, Relearning): ",
                    ["Learning", "Graduated", "Mature", "Relearning"]
                )
                break
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")

    # Grade options
    grade_map = {
        "1": "Again",
        "2": "Hard",
        "3": "Good",
        "4": "Easy",
        "5": "Very Easy"
    }

    grade_prompt = "Enter the grade:\n1) Again\n2) Hard\n3) Good\n4) Easy\n5) Very Easy\nYour choice: "
    grade_choice = get_valid_input(grade_prompt, grade_map.keys())
    grade = grade_map[grade_choice]

    # Calculate the next review details
    try:
        next_interval, next_ease_factor, next_review_date, next_status = calculate_next_review(
            current_interval, ease_factor, grade, status
        )

        # Output the results
        print("\n--- Next Review Details ---")
        print(f"Next Interval: {next_interval} days")
        print(f"Updated Ease Factor: {next_ease_factor:.2f}")
        print(f"Next Review Date: {next_review_date.strftime('%Y-%m-%d')}")
        print(f"Updated Status: {next_status}")
    except ValueError as e:
        print(f"Error: {e}")
