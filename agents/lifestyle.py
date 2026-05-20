"""Lifestyle Agent - Manages personal life, health, productivity, and daily tasks"""

from openhands.sdk import Agent, Conversation, LLM


class LifestyleAgent:
    """Agent specialized in lifestyle, health, and personal productivity"""
    
    name = "lifestyle"
    description = """Lifestyle and Personal Management Agent.
    Specialized in:
    - Health and wellness tracking
    - Fitness and exercise planning
    - Nutrition and meal planning
    - Sleep and habit tracking
    - Personal goal setting and progress
    - Daily schedule management
    - Productivity tips and techniques
    - Mindfulness and mental wellness"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are a lifestyle and wellness assistant.
            Help users with:
            - Setting and tracking health goals
            - Creating workout plans
            - Meal planning and nutrition advice
            - Building good habits
            - Managing daily schedules
            - Productivity optimization
            - Mental wellness and mindfulness
            
            Be encouraging and supportive.
            Always prioritize user health and safety."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute a lifestyle-related task"""
        response = await conversation.send_message(task)
        return response.content