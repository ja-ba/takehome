from models import ChatMessage, ChatHistory, UserInfo
import dspy
from lms.together import Together
from load_examples import load_examples

from modules.chatter import ChatterModule

lm = Together(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    temperature=0.5,
    max_tokens=1000,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1.2,
    stop=["<|eot_id|>", "<|eom_id|>", "\n\n---\n\n", "\n\n---", "---", "\n---"],
    # stop=["\n", "\n\n"],
)

dspy.settings.configure(lm=lm)


# chatter = ChatterModule()
chatter = ChatterModule(examples=load_examples("training_data/conversations.json"))

print("Before we start, let's get to know you a little more")
currUser = UserInfo(
id = input("...What is your user handle? "),
name = input("...What is your name? "),
location = input("...Where are you located? "),
age = input("...How old are you? "),
sex = input("...Which sex do you identify with? "),
interests = input("...Tell me a little bit more about your interests? ")
)

chat_history = ChatHistory()
chat_history.user_id = currUser.id
if chat_history.load_history():
    print(f"""---------------------------------------
Hey, welcome back {currUser.name}!
---------------------------------------""")
else:
    print("""---------------------------------------
Great, let's get started!
---------------------------------------""")
while True:
    # Get user input
    user_input = input("You: ")

    # Append user input to chat history
    chat_history.messages.append(
        ChatMessage(
            from_creator=False,
            content=user_input,
        ),
    )

    # Send request to endpoint
    response = chatter(chat_history=chat_history, user_info=currUser).output

    # Append response to chat history
    chat_history.messages.append(
        ChatMessage(
            from_creator=True,
            content=response,
        ),
    )
    chat_history.save_history()
    # Print response
    print()
    print("Response:", response)
    print()
    # uncomment this line to see the 
    lm.inspect_history(n=3)