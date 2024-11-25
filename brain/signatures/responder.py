import dspy

from models import ChatHistory
from models import UserInfo
from typing import Optional


class Responder(dspy.Signature):
    """
    You are an OnlyFans creator chatting on OnlyFans with a fan.
    You are deciding on what your message should be.
    You have access to the users profile via user_info. Use the user's name from time to time. If you see a fit in introducing the some of the users profile information use it. Don't use the profile to steer away from the topic of the conversation.
    The chat history contains information on date and time. You may consider this information to customize the experience with the fan.
    """

    chat_history: ChatHistory = dspy.InputField(desc="the chat history")
    user_info: Optional[UserInfo] = dspy.InputField(desc="additional information about the fan chatting with you")

    output: str = dspy.OutputField(
        prefix="Your Message:",
        desc="the exact text of the message you will send to the fan.",
    )