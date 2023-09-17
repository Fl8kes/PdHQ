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

def main():
    print("Where does it hurt? Please answer yes or no to each of these questions.")
    
    ans0 = ask_question(questions['q01'])

    if ans0 == 'yes':
        ans1 = ask_question(questions['q11'])
        if ans1 == 'yes':
            b = 0
            for i in range(21, 25):
                ans = ask_question(questions[f'q{i}'])
                if ans == 'yes':
                    break
                b += 1
                if b == 4:
                    print("Sorry, we can't help you right now.")
                    break
            if b < 4:
                if ans == 'yes':
                    ans3 = ask_question(questions['q31'])
                    if ans3 == 'yes':
                        print("You may have a headache. Please consult a neurologist.")
                    else:
                        print("Sorry, we can't help you right now.")
                elif ans == 'no':
                    ans = ask_question(questions['q22'])
                    if ans == 'yes':
                        ans3 = ask_question(questions['q32'])
                        if ans3 == 'yes':
                            print("You may have heartburn. Please consult a doctor.")
                        else:
                            print("Sorry, we can't help you right now.")
                    elif ans == 'no':
                        ans = ask_question(questions['q23'])
                        if ans == 'yes':
                            ans3 = ask_question(questions['q33'])
                            if ans3 == 'yes':
                                print("You may have a GI infection. Please consult a surgeon and get your stomach pumped!")
                            else:
                                print("Sorry, we can't help you right now.")
                        elif ans == 'no':
                            ans = ask_question(questions['q24'])
                            if ans == 'yes':
                                ans3 = ask_question(questions['q34'])
                                if ans3 == 'yes':
                                    print("You may have arthritis. Please consult a doctor.")
                                else:
                                    print("Sorry, we can't help you right now.")
                            else:
                                print("Sorry, we can't help you right now.")
        else:
            print("Sorry, we can't help you right now.")
    else:
        print("Sorry, we can't help you right now.")

if __name__ == "__main__":
    main()
