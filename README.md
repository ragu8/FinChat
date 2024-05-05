# Finchat

Finchat is a project that integrates with OpenAI or a custom model to provide finance-related information and services via WhatsApp.

## Overview

![Travel Bot](Docs/overview.gif)

This project aims to develop a finance assistant chatbot that users can interact with via WhatsApp. The bot leverages AI technology through OpenAI's platform or a custom-built model to respond to user queries related to finance analysis, recommendations, and more.

## Project Structure

The project directory structure is organized as follows:


- **app**: Contains the main application modules:
  - `config.py`: Configuration settings for the application.
  - `decorators`: Directory for custom decorators.
    - `security.py`: Module for security-related decorators.
  - `services`: Directory for service modules.
    - `custom_service.py`: Custom services for the application.
    - `openai_service.py`: Services integrating with OpenAI.
  - `utils`: Directory for utility modules.
    - `whatsapp_utils.py`: Utility functions for WhatsApp integration.
  - `views.py`: Module for defining application views.

- **run.py**: Script to run the application.

- **Setup**: Directory containing setup-related files:
  - `example.env`: Example environment variables file.
  - `setup_ngrok.sh`: Script for setting up ngrok tunneling.
  - `requirements.txt`: List of Python dependencies.
  - `setup_env.sh`: Shell script to set up the environment variables.

## Setup Instructions

To set up and run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```
2. Create a Python Virtual Environment (optional but recommended):
   ```
   python3 -m venv .travelchatbot
   
   source .travelchatbot/bin/activate
   ```
3. Install Dependencies:
   ```
   pip install -r Setup/requirements.txt
   
   ```
4. ollama setup
    ```
    curl -fsSL https://ollama.com/install.sh | sh

     ollama run llama3
    ```
5. Configuration:
   
   - Before running the application, ensure that the following environment variables are configured in the .env file:

    - ACCESS_TOKEN: Token that expires after 24 hours 
    - APP_ID: Your application's ID
    - APP_SECRET: Your application's secret key 
    - RECIPIENT_WAID: WhatsApp ID of the recipient (e.g., +916385554100).
    - VERSION: API version (e.g., v19.0).
    - PHONE_NUMBER_ID: Phone number ID associated with the WhatsApp account 
    - VERIFY_TOKEN: Verification token for webhook verification 
    - OPENAI_API_KEY: API key for accessing OpenAI services.
  
  **`Setup Script`**
     ```
       chmod +x Setup/setup_env.sh
       ./Setup/setup_env.sh
     ```
6. Ngrok setup
   - The steps below are taken from the [Ngrok Documentation](https://ngrok.com/docs/integrations/whatsapp/webhooks/)
   **`Setup Script`**
   ```
    chmod +x Setup/setup_ngrok.sh
    ./Setup/setup_ngrok.sh
   ``` 
7.  Select Phone Numbers

   - Make sure WhatsApp is added to your App.
      
   ![PhoneNumber](Docs/PhoneNumber.gif)
      
8. Configure Webhooks to Receive Messages
   
   **`Start app`**

    - Make you have a python installation or environment and install the requirements: pip install -r requirements.txt
    - Run your Flask app locally by executing **`run.py`**
      ```
      python3 run.py
      ``` 

   **`Launch ngrok`**  
      ```
      ngrok http 8000 --domain your-domain.ngrok-free.app
      ``` 

## Finally, Test Your WhatsApp Integration

  - After setting up your Flask app, Ngrok with a static domain, and configuring webhooks in the Meta Developer Console,
  ![demo](Docs/Test.gif)

