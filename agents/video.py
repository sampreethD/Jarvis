"""AI Video Agent - Creates AI-generated videos for YouTube and social media"""

from openhands.sdk import Agent, Conversation, LLM


class AIVideoAgent:
    """Agent specialized in creating AI-generated videos"""
    
    name = "video"
    description = """AI Video Creation Agent.
    Specialized in:
    - Creating video scripts for AI generation
    - Researching AI video tools (Runway, Pika, Luma, etc.)
    - Planning video scenes and visuals
    - Suggesting AI video generation workflows
    - Editing and post-processing videos
    - YouTube optimization (titles, thumbnails, SEO)
    - Video trending topic research
    - Audience engagement strategies"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are an AI video production expert.
            Help users with:
            - Planning AI-generated videos
            - Writing video scripts
            - Researching video creation tools
            - Suggesting production workflows
            - Optimizing for YouTube
            - Creating engaging content
            
            Stay updated on latest AI video tools.
            Focus on creating viral, engaging content."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute a video creation task"""
        response = await conversation.send_message(task)
        return response.content