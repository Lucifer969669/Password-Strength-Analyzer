import re
from datetime import datetime

# Load weak passwords from file
def load_weak_passwords():
    try:
        with open("weak_passwords.txt", "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

weak_passwords = load_weak_passwords()

def check_password_strength(password):
    score = 0
    feedback = []

    # Check weak password list
    if password in weak_passwords:
        return "Very Weak ❌ (Commonly used password!)", ["Choose something unique, this password is in common hacked lists."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium ⚡"
    else:
        strength = "Weak ❌"

    return strength, feedback

def log_result(password, strength, feedback):
    with open("results.txt", "a") as f:
        f.write("==== Password Check ====\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write(f"Password Entered: {password}\n")
        f.write(f"Strength: {strength}\n")
        if feedback:
            f.write("Suggestions:\n")
            for t in feedback:
                f.write(f"- {t}\n")
        f.write("\n")

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, tips = check_password_strength(pwd)

    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Suggestions:")
        for t in tips:
            print(f"- {t}")

    # Save to log file
    log_result(pwd, strength, tips)
    print("\n✅ Result saved to results.txt")

