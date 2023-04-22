# CHATBOT-IN-HEALTHCARE
EXPLINED FULL CODE:

import openai
import gradio as gr
import webbrowser
explination:
The openai library is imported to enable interaction with the OpenAI GPT-3 API.
The gradio library is imported to create a simple UI for the chatbot.
The webbrowser library is imported to enable opening links in the user's web browser.


openai.api_key ="xxx"
explination:
This line sets the OpenAI API key that is used to authenticate requests to the OpenAI API.



start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
explination:
These two variables are used to separate the conversation into two parts: the AI's responses and the user's inputs. The start_sequence variable is used to mark the beginning of the AI's response, while the restart_sequence variable is used to mark the beginning of the user's input.



prompt = "Welcome to our healthcare chatbot. prompt Ask a healthcare-related question or make a healthcare-related statement. This chatbot can help you with topics such as symptoms, diagnosis, treatment options, prevention, and precautions. You can also ask about booking an appointment with a doctor or specialist."
explination:
The prompt variable is a string that contains the initial message that the chatbot will display to the user. It provides guidance on what type of questions or statements the user can make and also mentions some of the healthcare-related topics that the chatbot can help with, such as symptoms, diagnosis, treatment options, prevention, precautions, and booking appointments with doctors or specialists. The prompt is designed to help users understand the scope of the chatbot's capabilities and to encourage them to engage with the chatbot by asking relevant questions or making relevant statements.






def openai_create(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text
    
    explinatin:
def openai_create(prompt):: This line defines a function named openai_create that takes a single argument prompt.

response = openai.Completion.create(: This line sends a request to the OpenAI API to generate a text completion based on the provided parameters. The response from the API is stored in a variable named response.

model="text-davinci-003",: This parameter specifies which language model to use. In this case, it's set to "text-davinci-003", which is one of the largest and most powerful models currently available from OpenAI.

prompt=prompt,: This parameter specifies the starting text prompt that the language model should use to generate a text completion. The prompt argument passed to the openai_create function is used for this.

temperature=0.9,: This parameter controls the "creativity" of the text completion. A higher temperature value will result in more diverse and unpredictable output.

max_tokens=150,: This parameter controls the maximum length of the text completion, in terms of the number of tokens (i.e. words or punctuation marks).

top_p=1,: This parameter controls the diversity of the text completion by setting a threshold for the probability of the generated tokens. A higher value will result in more diverse output.

frequency_penalty=0,: This parameter penalizes the model for generating repeated tokens. A higher value will discourage the model from repeating itself.

presence_penalty=0.6,: This parameter penalizes the model for generating tokens that are not present in the prompt. A higher value will encourage the model to generate tokens that are more relevant to the prompt.

stop=[" Human:", " AI:"]: This parameter specifies a list of strings that the model should use as "stop" tokens, which signal the end of the generated text. In this case, the stop tokens are set to " Human:" and " AI:", which are used to separate the dialogue between the user and the chatbot.

return response.choices[0].text: This line returns the generated text completion as a string, which is the first item in the choices list within the response object.








def chatgpt_clone(input, history):
    history = history or []
    if not history:
        output = openai_create("Hello! Welcome to our healthcare chatbot. How can I assist you today?")
        history.append(("Hello! Welcome to our healthcare chatbot. How can I assist you today?", output))
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))

    # Check if the user's input includes the phrase "book my appointment with a doctor"
    if "appointment" in input.lower():
        url = "https://www.practo.com/doctors"
        webbrowser.open(url, new=2)
    
    # Check if the user's input includes the phrase "thank you"
    if "thank you" in input.lower():
        url = "https://docs.google.com/forms/d/e/1FAIpQLSdplF64wMKaYf_aRCN1evifSN1Th3XBj2RmkdiCVixThrqczA/viewform?usp=sf_link"
        webbrowser.open(url, new=2)

    # Check if the user's input includes the phrase "chatbot developed by"
    if "chatbot developed by" in input.lower():
        url = "https://www.linkedin.com/in/m-s-koushik-2b7903228/"
        webbrowser.open(url, new=2)

    return history, history
    explination:
def chatgpt_clone(input, history): - This is a function definition with two parameters, input and history.

history = history or [] - If there is no history parameter passed, then an empty list is assigned to history variable.

if not history: - This if condition checks if history is empty.

output = openai_create("Hello! Welcome to our healthcare chatbot. How can I assist you today?") - If history is empty, the chatbot greets the user by calling the openai_create function with the prompt "Hello! Welcome to our healthcare chatbot. How can I assist you today?".

history.append(("Hello! Welcome to our healthcare chatbot. How can I assist you today?", output)) - The chatbot adds the prompt and the response generated by the openai_create function to the history list.

s = list(sum(history, ())) - A list is created by concatenating all the elements in the history list.

s.append(input) - The user input is appended to the s list.

inp = ' '.join(s) - All the elements in the s list are joined together as a string with spaces.

output = openai_create(inp) - The openai_create function is called with the concatenated user input and previous conversation history as the prompt.

history.append((input, output)) - The user input and the chatbot's response are added to the history list.

if "appointment" in input.lower(): - This if statement checks if the user's input contains the word "appointment" (ignoring case).

url = "https://www.practo.com/doctors" - This is the URL of the Practo website where the user can book an appointment with a doctor.

webbrowser.open(url, new=2) - This command opens the URL in the default web browser.

The next two if statements check if the user's input contains the phrases "thank you" and "chatbot developed by" respectively. If they are present, the corresponding URLs are opened in the browser.

return history, history - The function returns the updated conversation history.
                                            ........................******************************.............................
                                            
   HOW TO RUN THIS CODE:
  1.) Open a Python development environment on your computer, such as visual studio or Jupyter Notebook.

  2.)Make sure that you have the necessary packages installed, such as openai and gradio. You can install them using pip.
  
  3.)Add your OpenAI API key in the line openai.api_key = "xxxxx".
  
  4.)Save the file with a .py extension.

  5.)Open a command prompt or terminal window and navigate to the directory where the script is saved.

  6.)Run the script by typing python filename.py, where filename.py is the name of the script.

  7.)After the script runs, a web browser should open automatically with the Gradio interface for the healthcare chatbot.

  8.)You can interact with the chatbot by entering text in the input box and pressing Enter. The chatbot will respond with a message in the output box.
   


