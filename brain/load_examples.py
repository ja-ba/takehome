from dspy import Example
from typing import List
from models import ChatHistory, ChatMessage
import json

def load_examples(path: str) -> List[Example]:
    with open(path) as f:
        train_data = json.load(f)


    trainset = []
    for elem in train_data:
        hist = ChatHistory()
        for msg in elem["chat_history"]["messages"]:
            hist.messages.append(ChatMessage(**msg))

        trainset.append(
            Example(
                chat_history=hist,
                output=elem["output"],
            ).with_inputs("chat_history")
        )

    return trainset