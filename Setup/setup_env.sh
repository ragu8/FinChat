#!/bin/bash

# Define the list of environment variables to configure
ENV_VARS=(
    "ACCESS_TOKEN"
    "RECIPIENT_WAID"
    "VERSION"
    "PHONE_NUMBER_ID"
    "VERIFY_TOKEN"
    "OPENAI_API_KEY"
)

# Function to prompt user for input and store the value in the .env file
prompt_and_store() {
    local var_name="$1"
    read -p "Enter value for '$var_name': " var_value
    echo "$var_name=\"$var_value\"" >> .env
}

# Check if .env file already exists
if [ -f .env ]; then
    echo ".env file already exists. Please delete it before running this setup."
    exit 1
fi

# Iterate over each environment variable and prompt the user for input
for var in "${ENV_VARS[@]}"; do
    prompt_and_store "$var"
done

echo "Environment variables configured in .env file."
exit 0

