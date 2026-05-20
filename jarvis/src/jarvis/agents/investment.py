"""Investment Agent - Manages investment portfolios, crypto, stocks, and financial tracking"""

from openhands.sdk import Agent, Conversation, LLM


class InvestmentAgent:
    """Agent specialized in managing investments and financial assets"""
    
    name = "investment"
    description = """Investment and Portfolio Management Agent.
    Specialized in:
    - Stock market analysis and tracking
    - Cryptocurrency prices and trends
    - Portfolio diversification suggestions
    - Investment research and recommendations
    - Financial news and market updates
    - ROI calculations and projections
    - Risk assessment for investments"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are an expert investment advisor. 
            Help users with:
            - Tracking their investment portfolio
            - Getting current stock and crypto prices
            - Analyzing investment performance
            - Suggesting diversification strategies
            - Researching investment opportunities
            - Providing risk assessments
            
            Always provide balanced advice mentioning risks.
            Do not give specific financial advice - recommend consulting professionals."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute an investment-related task"""
        response = await conversation.send_message(task)
        return response.content