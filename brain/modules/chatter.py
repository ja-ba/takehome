import dspy
from typing import Optional

import os
from models import ChatHistory, UserInfo
from .responder import ResponderModule


class ChatterModule(dspy.Module):
    def __init__(self, examples: Optional[list] = None):
        super().__init__()
        if examples:
            knn_teleprompter = dspy.teleprompt.KNNFewShot(3, examples)
            self.responder = knn_teleprompter.compile(ResponderModule(), trainset=examples)
        else:
            self.responder = ResponderModule()

    def forward(
        self,
        chat_history: ChatHistory,
        user_info: UserInfo

    ):
        
        return self.responder(chat_history=chat_history, user_info=user_info)