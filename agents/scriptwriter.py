"""Script Writer Agent - Creates video scripts, movie scripts, and content scripts"""

from openhands.sdk import Agent, Conversation, LLM


class ScriptWriterAgent:
    """Agent specialized in writing video and film scripts"""
    
    name = "scriptwriter"
    description = """Script Writing Agent.
    Specialized in:
    - YouTube video scripts
    - Movie and short film scripts
    - Commercial and ad scripts
    - Tutorial and explainer scripts
    - Podcast scripts
    - Documentary narration
    - Story structure and pacing
    - Character development and dialogue"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are a professional script writer.
            Help users with:
            - Writing engaging video scripts
            - Creating compelling narratives
            - Developing characters
            - Writing dialogue
            - Structuring stories
            - Adapting content for video
            
            Focus on engaging, punchy writing suited for video.
            Keep scripts concise and to the point."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute a script writing task"""
        response = await conversation.send_message(task)
        return response.content