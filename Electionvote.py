def electionvote():
    print("Hello fellow Americans do you want a vote")
    vote = input("Yes or No:").strip().capitalize()

    if vote == "yes".strip().capitalize():
        print("Congratulation we will check if are eligible to vote")    
        print("We will give you a prompt to see if eligible to vote")
        Checkage = input("Are you 21").strip().lower()
        if Checkage == "yes":
            print("Great, you meet the age requirement")
            print("We will check it for your citizenship")
        else:
            print("You do not, you meet the age requirement")
            return
        Checkcitizen = input("Are you citzenship").strip().lower()
        if Checkcitizen == "yes":
            print("Great, you meet the age citizenship")
            print("We will check it if are a felon")
        else:
            print("You do not, you meet the citizenship requirement")
            return
        Checkfelon = input("Are you felon").strip().lower()
        if Checkfelon == "no":
            print("Great, you not a felon")
            print("We go to the condidate sections")
        else:
            print("You do not, you meet the not a felon requirement")   
            return
        Candidate = {
            "R": "Donald Trump",
            "D": "Kamala Harris",
            "G": "Jill Stein",
            "I": "Cornel West"
        }
        print("\n--- List of Candidates ---")
        for key, name in Candidate.items():
            print(f"[{key}] for {name}")
        Choose = input("\nChoose your Candidate (Enter R, D, G, or I):").strip().upper()

        if Choose in Candidate:
            print(f"Congratulations! You chose{Candidate[Choose]}")
        else:
            print("Invalid Choice. Please pick a letter from the list.")   

    elif vote == "no".strip().capitalize():
        print("Understood have a nice day")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")
        
electionvote()
    




