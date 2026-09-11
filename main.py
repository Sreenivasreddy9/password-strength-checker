import re


def score_password(password: str) -> int:
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    return score


def main() -> None:
    password = input("Enter a password: ")
    score = score_password(password)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"Password strength: {strength} ({score}/6)")


if __name__ == "__main__":
    main()
