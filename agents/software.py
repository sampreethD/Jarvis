"""Software Development Agent - Builds, tests, and maintains software applications"""

from openhands.sdk import Agent, Conversation, LLM


class SoftwareAgent:
    """Agent specialized in software development"""
    
    name = "software"
    description = """Software Development Agent.
    Specialized in:
    - Writing and editing code in any language
    - Bug detection and debugging
    - Code review and optimization
    - Setting up development environments
    - Running tests and fixing failures
    - Explaining complex code patterns
    - Best practices and architecture
    - API design and documentation"""
    
    def __init__(self, llm: LLM):
        self.agent = Agent(
            name=self.name,
            description=self.description,
            llm=llm,
            instructions="""You are an expert software developer.
            Help users with:
            - Writing clean, efficient code
            - Debugging and fixing issues
            - Code review and optimization
            - Setting up projects
            - Running and testing code
            - Explaining concepts
            - Following best practices
            
            Write idiomatic code considering the specific language.
            Always explain your reasoning."""
        )
    
    async def run(self, conversation: Conversation, task: str):
        """Execute a software development task"""
        response = await conversation.send_message(task)
        return response.content