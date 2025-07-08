from flask import Blueprint, render_template, request
from app.analysis import rule_based_check, extract_text_from_attachment
from app.ml_model import predict_email

# Create a Blueprint for routing
routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def home():
    """
    This is the main route for the application. It handles both GET and POST requests.
    GET: Shows the main page with the form.
    POST: Processes email text or attachment submitted by the user and returns analysis results.
    """
    result = None  # This will hold the final output: "Phishing", "Safe", or an error message

    if request.method == "POST":
        # Get the email text input from the form and strip whitespace
        email_text = request.form.get("email_text", "").strip()
        # Get the uploaded file, if any
        file = request.files.get("attachment")

        # If user entered email text in the text area
        if email_text:
            # Analyze using the machine learning model
            ml_result = predict_email(email_text)
            # Run simple rule-based keyword check
            rule_result = rule_based_check(email_text)

        # If user uploaded a file instead
        elif file and file.filename != "":
            try:
                # Extract readable text from the uploaded file
                file_content = extract_text_from_attachment(file)
                # Analyze the extracted content with ML model
                ml_result = predict_email(file_content)
                # Also check it with rule-based method
                rule_result = rule_based_check(file_content)
            except Exception as e:
                # Handle file read errors 
                print(f"[ERROR] File processing failed: {e}")
                result = "Error analyzing attachment"
                return render_template("index.html", result=result)

        else:
            # If neither text nor file was provided
            result = "Please enter email text or upload a file."
            return render_template("index.html", result=result)

        # Final decision based on both ML and rule-based results
        if ml_result == 1 or rule_result:
            result = "Phishing"
        else:
            result = "Safe"

    # Render the page with the analysis result (if any)
    return render_template("index.html", result=result)
