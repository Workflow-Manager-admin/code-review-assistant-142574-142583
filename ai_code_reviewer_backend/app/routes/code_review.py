from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify
from marshmallow import Schema, fields

blp = Blueprint(
    "CodeReview",
    "code_review",
    url_prefix="/review",
    description="Endpoints for AI-powered code review operations"
)

# PUBLIC_INTERFACE
class CodeSubmissionSchema(Schema):
    """Schema for code submission data."""
    language = fields.Str(required=True, description="Programming language of the submitted code", example="python")
    code = fields.Str(required=True, description="The code to be reviewed", example='print("Hello, World!")')

# PUBLIC_INTERFACE
class CodeReviewFeedbackSchema(Schema):
    """Schema for returned AI-powered review feedback."""
    feedback = fields.Str(required=True, description="AI review comments and suggestions")
    issues = fields.List(fields.Str(), required=False, description="List of detected issues or improvements")

# PUBLIC_INTERFACE
def call_third_party_ai_service(code: str, language: str) -> dict:
    """
    Integrate with a third-party AI service for code review. Uses API KEY from .env.

    Args:
        code (str): Submitted code for review.
        language (str): Programming language of the code.

    Returns:
        dict: AI review feedback object.
    """
    # Example: Placeholder for real external call; replace with requests to an AI API.
    # ai_api_key = os.getenv("AI_API_KEY")
    # Here, you would use `ai_api_key` to make authenticated requests to the real AI service.
    #
    # Example:
    # import requests
    # headers = {"Authorization": f"Bearer {ai_api_key}"}
    # payload = {"code": code, "language": language}
    # response = requests.post(os.getenv("AI_REVIEW_ENDPOINT_URL"), json=payload, headers=headers)
    # return response.json()
    return {
        "feedback": f"AI review for {language}: (Pretend this is smart feedback from the AI model.)",
        "issues": [
            "Issue example: Variable is not used.",
            "Suggestion: Add docstrings to your functions."
        ]
    }

@blp.route("/", methods=["POST"])
class CodeReviewResource(MethodView):
    """
    PUBLIC_INTERFACE
    POST /review/ 

    Accepts code submissions and returns AI-powered code review feedback.
    """
    @blp.arguments(CodeSubmissionSchema, location="json")
    @blp.response(200, CodeReviewFeedbackSchema, description="AI-generated code review feedback")
    def post(self, submission_data):
        """
        Submit code for review.

        Args:
            submission_data (CodeSubmissionSchema): The code and language info.

        Returns:
            CodeReviewFeedbackSchema: AI-generated review and suggestions.
        """
        code = submission_data.get("code")
        language = submission_data.get("language")

        if not code or not language:
            return jsonify({
                "feedback": "",
                "issues": ["Missing code or language parameter."]
            }), 400

        # Call to AI Service (Replace with real integration)
        result = call_third_party_ai_service(code, language)
        return result
