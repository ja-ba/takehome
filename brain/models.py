from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import os

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
    user_id: Optional[str] = None

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
    
    def save_history(self) -> bool:
        if self.user_id:
            with open(f'chat_histories/{self.user_id}.json', 'w') as f:
                json.dump([{"from_creator": s.from_creator, "content": s.content} for s in self.messages], f)
            return True
        else:
            return False

    def load_history(self):
        if self.user_id and os.path.exists(f'chat_histories/{self.user_id}.json'):
            with open(f'chat_histories/{self.user_id}.json', 'r') as f:
                self.messages = [ChatMessage(**m) for m in json.load(f)]
            return True
        else:
            return False
    
class UserInfo(BaseModel):
    id : str
    name: str
    location: str
    age: str
    sex: str
    interests: str
