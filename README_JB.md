I took around 8 hours on this take home assignment. This included getting familiar with the codebase, setting up together AI, implementing the solutions as well as debugging.

1. **Improve Client Personality Emulation**  
I have followed this example to set up the KNN few shot learning: https://github.com/stanfordnlp/dspy/blob/main/examples/knn.ipynb It seems to work. k=3 was chosen due to response time increasing with higher k's. It seems that the style changed after the adjustment. There is potential to test this more rigorously, e.g. by setting aside a test set and then comparing embedding distance of the answer with and without using KNN few-shot examples (assumption lower distance for the adjusted model). Another option for evaluating performance would be LLM-as-a-judge and 

2. **Incorporate Context Awareness**  
Conext awareness was incorporated by:
    - Adding time and date to the Chat format
    - Adjusting the signature prompt, to use the time/date information
    - Incorporating a user profile which is inputted by the user before chatting (in real life would be available through the account)
    - Adjusting the signature prompt, to use the user information

3. **Topic Filtering**  
I tried to see if DSPy had any pre-built functionality for this, but didn't find anything and just adjusted the prompt. It seems to work quite well. I couldn't get the chat bot to violate any of the restrictions.

4. **Further Product Enhancements**  
I have enhanced the functionality of saving and loading the chat history for a given user id. This way, the chat bot doesn't need to start from scratch every time a user starts a new chat, but has access to previous messages which can make the feel of the conversation more personal and intimate. 
