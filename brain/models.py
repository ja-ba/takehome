from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime



class ChatMessage(BaseModel):
    from_creator: bool
    content: str

    def __str__(self):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        role = ("YOU" if self.from_creator else "THE FAN") + " (" + time + "):"
        message = role + ": " + self.content
        return message

class ChatHistory(BaseModel):
    messages: List[ChatMessage] = []

    def __str__(self):
        messages = []
        for i, message in enumerate(self.messages):
            message_str = str(message)
            # if i == len(self.messages) - 1 and not message.from_creator:
            #     message_str = (
            #         "(The fan just sent the following message which your message must respond to): "
            #         + message_str
            #     )
            messages.append(message_str)
        return "\n".join(messages)
    
    def model_dump_json(self, **kwargs):
        return str(self)
    
class UserInfo(BaseModel):
    name: str
    location: str
    age: str
    sex: str
    interests: str
