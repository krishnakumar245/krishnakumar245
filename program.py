import matplotlib.pyplot as plt

# List storing information about disorders
mental_health_info = [
    {
        "code": "F32.x",
        "name": "Major Depressive Disorder",
        "description": "Major Depressive Disorder includes various severity levels ranging from mild to severe, often characterized by a persistent feeling of sadness and loss of interest.",
        "examples": ["Persistent depressive mood", "Fatigue and loss of energy", "Feelings of worthlessness"],
        "prevalence": 7.1  # example prevalence rate in %
    },
    {
        "code": "F41.x",
        "name": "Anxiety Disorders",
        "description": "Anxiety Disorders include generalized anxiety, panic disorder, and other anxiety-related conditions, characterized by excessive worry and fear.",
        "examples": ["Chronic worry", "Panic attacks", "Physical symptoms such as sweating and rapid heartbeat"],
        "prevalence": 19.1  # example prevalence rate in %
    },
    {
        "code": "F43.x",
        "name": "Reaction to Severe Stress (including PTSD)",
        "description": "This category includes conditions like PTSD that develop after experiencing or witnessing traumatic events.",
        "examples": ["Flashbacks", "Nightmares", "Avoidance of reminders of trauma"],
        "prevalence": 3.6  # example prevalence rate in %
    },
    {
        "code": "F90.x",
        "name": "Attention Deficit Hyperactivity Disorder (ADHD)",
        "description": "ADHD affects focus, self-control, and other skills important in daily life, with symptoms starting in childhood and possibly persisting into adulthood.",
        "examples": ["Inattention", "Hyperactivity", "Impulsivity"],
        "prevalence": 4.4  # example prevalence rate in %
    },
    {
        "code": "F60.x",
        "name": "Personality Disorders",
        "description": "Personality Disorders involve enduring patterns of behavior, cognition, and inner experience, deviating from cultural expectations.",
        "examples": ["Dramatic mood swings", "Difficulty in relationships", "Chronic feelings of emptiness"],
        "prevalence": 9.1  # example prevalence rate in %
    },
    {
        "code": "F20.x",
        "name": "Schizophrenia Spectrum Disorders",
        "description": "Schizophrenia and related disorders affect how a person thinks, feels, and acts, often with symptoms of psychosis such as delusions or hallucinations.",
        "examples": ["Hallucinations", "Delusions", "Disorganized thinking"],
        "prevalence": 1.0  # example prevalence rate in %
    }
]

def display_disorder_info(choice):
    """Display information about the disorder based on the selected choice."""
    if 1 <= choice <= len(mental_health_info):
        disorder = mental_health_info[choice - 1]
        print(f"\nCode: {disorder['code']}")
        print(f"Name: {disorder['name']}")
        print(f"Description: {disorder['description']}")
        print("Examples of Symptoms:")
        for symptom in disorder["examples"]:
            print(f" - {symptom}")
    else:
        print("\nInvalid choice. Please select a number from the list.")

def plot_prevalence():
    """Plot a line chart showing the prevalence of mental health disorders."""
    names = [info["name"] for info in mental_health_info]
    prevalence = [info["prevalence"] for info in mental_health_info]

    plt.figure(figsize=(10, 6))
    plt.plot(names, prevalence, marker='o', linestyle='-', color='lightcoral', linewidth=2)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Prevalence (%)')
    plt.title('Prevalence of Mental Health Disorders')
    plt.tight_layout()
    plt.show()

# User Interaction
print("Welcome to the Mental Health Information Program!")
print("Select a disorder from the list below by entering the corresponding number:")

while True:
    print("\nMenu:")
    for idx, disorder in enumerate(mental_health_info, 1):
        print(f"{idx}. {disorder['name']} ({disorder['code']})")
    print("P. Plot prevalence chart")
    print("E. Exit")

    user_input = input("\nEnter your choice: ")
    if user_input.lower() == 'e':
        break
    elif user_input.lower() == 'p':
        plot_prevalence()
    elif user_input.isdigit():
        display_disorder_info(int(user_input))
    else:
        print("\nInvalid input. Please enter a number, 'P' to plot, or 'E' to exit.")
