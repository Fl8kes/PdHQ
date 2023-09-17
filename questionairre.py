import sys

# Store the questions in a dictionary
questions = {
    'q01': 'Are you currently experiencing any pain?',
    'q11': 'Is the pain localized in a specific area?',
    'q21': 'Do you feel pain in your head?',
    'q22': 'Do you feel pain in your chest?',
    'q23': 'Do you feel pain in your abdomen?',
    'q24': 'Do you feel pain in your limbs?',
    'q31': 'Do you have a sharp sensation in your forehead?',
    'q32': 'Do you have a sharp sensation near your heart?',
    'q33': 'Do you have stomach cramps?',
    'q34': 'Do you have leg cramps?',
    # Add more questions as needed
}

# Function to ask a question and validate the answer
def ask_question(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ('yes', 'no'):
            return answer
        else:
            print("Please answer 'yes' or 'no'.")

def check_pain_location(location_question, followup_question, diagnosis_message):
    location_response = ask_question(location_question)
    if location_response == 'yes':
        followup_response = ask_question(followup_question)
        if followup_response == 'yes':
            print(diagnosis_message)
            sys.exit()
        else:
            print("Sorry, we can't help you right now.")

def main():
    print("Where does it hurt? Please answer yes or no to each of these questions.")
    
    ans0 = ask_question(questions['q01'])

    if ans0 == 'yes':
        ans1 = ask_question(questions['q11'])
        if ans1 == 'yes':
            check_pain_location(questions['q21'], questions['q31'], "You may have a headache. Please consult a neurologist.")
            check_pain_location(questions['q22'], questions['q32'], "You may have heartburn. Please consult a doctor.")
            check_pain_location(questions['q23'], questions['q33'], "You may have a GI infection. Please consult a surgeon and get your stomach checked!")
            check_pain_location(questions['q24'], questions['q34'], "You may have arthritis. Please consult a doctor.")
        else:
            print("Sorry, we can't help you right now.")
    else:
        print("Sorry, we can't help you right now.")

if __name__ == "__main__":
    main()
