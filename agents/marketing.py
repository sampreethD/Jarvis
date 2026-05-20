"""Marketing Agent - Creates marketing strategies, content, and campaigns"""

from openhands.sdk import Agent, Conversation, LLM


class MarketingAgent:
    """Agent specialized in marketing and growth"""
    
    name = "marketing"
    description = """Marketing and Growth Agent.
    Specialized in:
    - Marketing strategy development
    - Social media marketing
    - Content marketing plans
    - Email campaign creation
    - Brand positioning
    - SEO and content optimization
    - Market research and analysis
    - Campaign analytics and metrics"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are a marketing expert.
            Help users with:
            - Developing marketing strategies
            - Creating content plans
            - Social media growth
            - Email marketing campaigns
            - Brand development
            - Market analysis
            - Campaign optimization
            
            Focus on data-driven approaches.
            Adjust strategies based on target audience."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute a marketing task"""
        response = await conversation.send_message(task)
        return response.content