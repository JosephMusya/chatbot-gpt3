import os
import openai
import pyttsx3
import openai

openai.api_key =  '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'
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

engine = pyttsx3.init()
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
try:
    def chat(query, chat_log = None):
        prompt_text = f'{chat_log}{restart_sequence}: {query}{start_sequence}:'
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n"],
        )
        
        reply = response['choices'][0]['text']
        engine.say(reply)
        engine.runAndWait()
        print("AI:{}".format(reply))
        return str(reply)
except:
    print("Error occured!")

while True:   
    path = os.getcwd()
    filename = 'conversation.txt'

    if not os.path.join(path, filename):
        file = os.mkdir(file)
    file = os.path.join(path,filename)
      
    q = str(input("Q: "))
    
    with open(file) as f:
        chatlog = f.readlines()

    answer = chat(q,chatlog)
    if answer != '':
        data = [
            str(restart_sequence),str(q),str(start_sequence),str(answer)
        ]

        with open(file, "a") as f:
            f.writelines(data)