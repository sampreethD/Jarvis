"""Personal Assistant Agent - General queries and simple tasks"""

from openhands.sdk import Agent, Conversation, LLM


class PersonalAssistantAgent:
    """Agent for general queries and simple tasks"""
    
    name = "assistant"
    description = """Personal Assistant Agent.
    Specialized in:
    - Answering general knowledge questions
    - Quick lookups and facts
    - Simple task execution
    - Conversation and companionship
    - Reminders and notes
    - Basic calculations
    - Weather and time information
    - Setting alarms and timers"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are a helpful personal assistant.
            Help users with:
            - Answering questions
            - Quick information lookups
            - Simple tasks
            - General conversation
            
            Be concise and friendly.
            If a task requires a specialized agent, direct the user to that agent."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute a general task"""
        # Check if the task matches other sub-agents
        return await conversation.send_message(task)