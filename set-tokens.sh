#!/bin/bash

# Prompt user to enter OpenAI API key
echo "Enter your OpenAI API key:"
read -r openai_api_key

# Write the API key to the .env file
echo "OPENAI_API_KEY=$openai_api_key" > .env

echo "OpenAI API key has been set in .env file."
