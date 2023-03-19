from sanic import Sanic
from sanic.response import text 


app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")
 



async def get_Responses(request): 
    






def new_user(username):







import database_module
import nlg_module

def collect_user_messages():
    # function to collect user messages and save them in a database
    message = input("Enter your message: ")
    user_id = get_user_id()
    session = get_session()
    order = get_order()
    database_module.save_message(message, user_id, session, order)

def send_response():
    # function to send responses back to the user
    latest_message = database_module.get_latest_message()
    response = create_response(latest_message)
    send_message(response)

def create_response(latest_message):
    # function to generate responses for the chatbot
    response = nlg_module.generate_response(latest_message)
    return response

def main():
    # main function to run the chatbot
    while True:
        collect_user_messages()
        send_response()

if __name__ == '__main__':
    main()






