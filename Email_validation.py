def validate_email(email):
    # Basic length and starting character check
    if len(email) < 6:
        return "wrong email 1"  # Too short
    if not email[0].isalpha():
        return "wrong email 2"  # Must start with a letter
    
    # Check single '@', not at start/end
    if email.count('@') != 1 or email.startswith('@') or email.endswith('@'):
        return "wrong email 3"

    local, domain = email.split('@')

    # Domain must contain a period not at edges
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return "wrong email 4 (domain format)"

    # Disallow spaces
    if any(ch.isspace() for ch in email):
        return "wrong email 5 (contains space)"

    # Allowed characters in local and domain
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._@")
    if any(ch not in allowed for ch in email):
        return "wrong email 6 (invalid character)"

    return "valid email"

# Usage
email = input("Enter your Email: ")
print(validate_email(email))
