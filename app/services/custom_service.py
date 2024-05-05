import ollama


conversation_history = []

def generate_response(message_body):
    global conversation_history
    

    conversation_history.append({'role': 'user', 'content': message_body})
    

    response = ollama.chat(model='approlabs', messages=conversation_history)
    

    conversation_history.append({'role': 'assistant', 'content': response['message']['content']})
    
    return response['message']['content']

