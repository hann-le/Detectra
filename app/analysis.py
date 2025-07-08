from app.ml_model import predict_phishing

def rule_based_check(email_text):
    """
    This function performs a basic rule-based phishing detection.
    It checks if the email text contains any known suspicious phrases.
    If a phrase is found, it returns True, indicating possible phishing.
    Otherwise, it returns False.
    """
    phishing_indicators = ["free money", "urgent action", "verify your account", "click here"]
    email_text_lower = email_text.lower()
    for phrase in phishing_indicators:
        if phrase in email_text_lower:
            return True
    return False

def analyze_email_text(email_text):
    """
    This function uses a machine learning model to analyze email text.
    It calls the predict_phishing function to return whether the email
    is phishing or safe based on the model's prediction.
    """
    return predict_phishing(email_text)

def analyze_email_attachment(file_storage):
    """
    This function analyzes the content of an uploaded email attachment.
    It tries to read the file as UTF-8 text and sends the content to the
    phishing detection model. If the file can't be read, it returns an error message.
    """
    try:
        content = file_storage.read().decode('utf-8', errors='ignore')  # Safely read and decode file
        return predict_phishing(content)
    except Exception as e:
        print(f"Error reading file: {e}")
        return "Error analyzing file"

def extract_text_from_attachment(file_storage):
    """
    This helper function extracts and returns the raw text content from an uploaded file.
    It decodes the file using UTF-8 and ignores any decoding errors.
    This function can be used for previewing or preprocessing the file before analysis.
    """
    content = file_storage.read().decode('utf-8', errors='ignore')
    return content
