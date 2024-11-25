import dspy

from signatures.responder import Responder
from models import ChatHistory, UserInfo
from typing import Optional

class ResponderModule(dspy.Module):
    def __init__(self):
        super().__init__()
        reasoning = dspy.OutputField(
            prefix="Reasoning: Let's think step by step to decide on our message. We",
        )
        self.prog = dspy.TypedChainOfThought(Responder, reasoning=reasoning)
    
    def forward(
        self,
        chat_history: dict,
        user_info: Optional[UserInfo] = None
    ):
        return self.prog(
            chat_history=ChatHistory.parse_obj(chat_history),
            user_info = UserInfo.parse_obj(user_info) if user_info else None
        )