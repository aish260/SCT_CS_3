import re

def assess_password_strength(password):
    strength_score = 0
    feedback = []

    
    if len(password) >= 8:
        strength_score += 2
    elif len(password) >= 5:
        strength_score += 1
        feedback.append("Consider using at least 8 characters.")

    
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Add uppercase letters.")

    
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("Include lowercase letters.")

    
    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("Try adding numbers.")

    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("Include special characters for stronger protection.")

    
    if strength_score >= 6:
        verdict = "🟢 Strong"
    elif strength_score >= 4:
        verdict = "🟡 Moderate"
    else:
        verdict = "🔴 Weak"

    return {
        "score": strength_score,
        "verdict": verdict,
        "feedback": feedback
    }


password = input("Enter a password to assess: ")
result = assess_password_strength(password)

print("\nPassword Strength:", result["verdict"])
print("Score:", result["score"])
if result["feedback"]:
    print("Tips to improve your password:")
    for tip in result["feedback"]:
        print("-", tip)
