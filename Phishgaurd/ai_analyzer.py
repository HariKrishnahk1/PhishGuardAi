import re

def analyze_message(text):

    text_lower = text.lower()

    risk_score = 0
    reasons = []

    # Suspicious keywords
    keywords = [
        "urgent", "verify", "account blocked",
        "click link", "update kyc",
        "bank alert", "win prize",
        "free", "otp", "password"
    ]

    for word in keywords:
        if word in text_lower:
            risk_score += 10
            reasons.append(f"Contains suspicious keyword: {word}")

    # Detect URLs
    urls = re.findall(r'https?://\S+|www\.\S+', text_lower)

    if urls:
        risk_score += 20
        reasons.append("Contains external link")

        shorteners = ["bit.ly", "tinyurl", "goo.gl"]
        for url in urls:
            if any(s in url for s in shorteners):
                risk_score += 20
                reasons.append("Uses shortened URL")

    # OTP request detection
    if "otp" in text_lower:
        risk_score += 20
        reasons.append("Requests OTP information")

    # Decide risk level
    if risk_score >= 60:
        level = "HIGH"
    elif risk_score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    result = f"""
Risk Level: {level}
Risk Score: {risk_score}/100

Reasons:
- """ + "\n- ".join(reasons if reasons else ["No major threats detected"])

    return result