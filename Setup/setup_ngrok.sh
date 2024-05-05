#!/bin/bash

# Check if script is running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root or with sudo."
    exit 1
fi

# Install Ngrok
echo "Installing Ngrok..."
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update
sudo apt install -y ngrok

# Prompt user for Ngrok authentication token
read -p "Enter your Ngrok authentication token: " NGROK_AUTH_TOKEN

# Configure Ngrok with the provided authentication token
ngrok authtoken "$NGROK_AUTH_TOKEN"



echo "Ngrok setup complete."


 

