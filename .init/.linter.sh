#!/bin/bash
cd /home/kavia/workspace/code-generation/code-review-assistant-142574-142583/ai_code_reviewer_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

