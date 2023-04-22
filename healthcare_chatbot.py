import openai
import gradio as gr
import webbrowser

openai.api_key = "XXXX"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Welcome to our healthcare chatbot. prompt Ask a healthcare-related question or make a healthcare-related statement. This chatbot can help you with topics such as symptoms, diagnosis, treatment options, prevention, and precautions. You can also ask about booking an appointment with a doctor or specialist."

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


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>HEALTHCARE CHATBOT</center></h1>
                    <p>Developed by MSK TEAM</p>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True,share=True)
