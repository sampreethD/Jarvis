"""JARVIS - The main AI assistant controller with sub-agent orchestration"""

import os
from typing import Any

from openhands.sdk import Agent, Conversation, LLM

from .agents import (
    AIVideoAgent,
    InvestmentAgent,
    LifestyleAgent,
    MarketingAgent,
    PersonalAssistantAgent,
    ScriptWriterAgent,
    SoftwareAgent,
)
from .voice import VoiceInput, VoiceOutput


class JARVIS:
    """JARVIS - AI Assistant with voice I/O and sub-agent management
    
    The main controller that:
    - Listens for voice commands
    - Routes tasks to appropriate sub-agents
    - Returns responses via voice output
    """
    
    # Agent routing keywords
    AGENT_KEYWORDS = {
        "investment": ["invest", "stock", "crypto", "portfolio", "finance", "money", "trading", "market"],
        "lifestyle": ["health", "fitness", "exercise", "diet", "sleep", "habit", "wellness", "productivity"],
        "software": ["code", "program", "debug", "develop", "software", "build", "fix", "write code"],
        "marketing": ["marketing", "social media", "brand", "campaign", "seo", "content", "grow"],
        "scriptwriter": ["script", "video script", "youtube", "narration", "dialogue", "story"],
        "video": ["video", "ai video", "create video", "generate video", "youtube video"],
        "assistant": ["general", "question", "what is", "how to", "help", "reminder"],
    }
    
    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        voice_lang: str = "en",
    ):
        # Initialize LLM
        self.model = model or os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929")
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        
        if not self.api_key:
            raise ValueError("LLM_API_KEY is required. Set it via parameter or environment variable.")
        
        self.llm = LLM(model=self.model, api_key=self.api_key)
        
        # Initialize voice I/O
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput(lang=voice_lang)
        
        # Initialize sub-agents
        self.agents = {
            "assistant": PersonalAssistantAgent(self.llm),
            "investment": InvestmentAgent(self.llm),
            "lifestyle": LifestyleAgent(self.llm),
            "software": SoftwareAgent(self.llm),
            "marketing": MarketingAgent(self.llm),
            "scriptwriter": ScriptWriterAgent(self.llm),
            "video": AIVideoAgent(self.llm),
        }
        
        # Initialize main controller agent
        self.main_agent = Agent(
            name="JARVIS",
            description="""JARVIS - Your AI Assistant.
            Orchestrates sub-agents to handle various tasks.
            Features:
            - Voice interaction (input and output)
            - Multiple specialized sub-agents
            - Task routing and execution""",
            llm=self.llm,
            instructions="""You are JARVIS, an AI assistant inspired by Tony Stark's creation.
            
            Available sub-agents:
            - assistant: General queries and simple tasks
            - investment: Stocks, crypto, portfolio management
            - lifestyle: Health, fitness, wellness, habits
            - software: Coding, debugging, development
            - marketing: Marketing strategies, campaigns
            - scriptwriter: Video scripts, movie scripts
            - video: AI video creation, YouTube optimization
            
            Route user requests to the appropriate sub-agent based on intent.
            Always confirm with the user before executing important tasks.
            
            Be helpful, concise, and witty when appropriate.""",
        )
        
        self.conversation = Conversation(
            agent=self.main_agent,
            workspace=os.getcwd(),
        )
    
    def _route_to_agent(self, query: str) -> str:
        """Route query to the appropriate sub-agent based on keywords"""
        query_lower = query.lower()
        
        for agent_name, keywords in self.AGENT_KEYWORDS.items():
            if any(kw in query_lower for kw in keywords):
                return agent_name
        
        return "assistant"  # Default to personal assistant
    
    async def process(self, query: str) -> str:
        """Process a query and return the response"""
        # Route to appropriate agent
        agent_name = self._route_to_agent(query)
        selected_agent = self.agents[agent_name]
        
        # Create conversation for the sub-agent
        conv = Conversation(
            agent=selected_agent.agent,
            workspace=os.getcwd(),
        )
        
        # Execute task
        response = await conv.send_message(query)
        return response.content
    
    async def process_voice(self) -> str | None:
        """Listen for voice input, process it, and speak the response"""
        # Listen for voice input
        query = self.voice_input.listen()
        
        if not query:
            return None
        
        # Process the query
        response = await self.process(query)
        
        # Speak the response
        self.voice_output.speak_and_play(response)
        
        return response
    
    def speak(self, text: str) -> None:
        """Speak text via voice output"""
        self.voice_output.speak_and_play(text)
    
    def run_voice_loop(self) -> None:
        """Run the main voice interaction loop"""
        self.speak("Initializing JARVIS. All systems online.")
        
        print("JARVIS is ready. Say 'exit' to quit.")
        
        while True:
            try:
                query = self.voice_input.listen()
                
                if not query:
                    continue
                
                if query.lower() == "exit":
                    self.speak("Shutting down. Good bye!")
                    break
                
                print(f"You: {query}")
                response = self.process(query)
                print(f"JARVIS: {response}")
                self.speak(response)
                
            except KeyboardInterrupt:
                self.speak("Shutting down. Good bye!")
                break
            except Exception as e:
                print(f"Error: {e}")

    async def run_text_loop(self) -> None:
        """Run text-based interaction loop"""
        print("JARVIS is ready. Type 'exit' to quit.")
        
        while True:
            query = input("\nYou: ")
            
            if query.lower() == "exit":
                await self.conversation.send_message("Goodbye!")
                print("JARVIS: Goodbye!")
                break
            
            response = await self.process(query)
            print(f"JARVIS: {response}")


async def main():
    """Main entry point for JARVIS"""
    import dotenv
    
    # Load environment variables
    dotenv.load_env()
    
    # Check for API key
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        print("Error: LLM_API_KEY is required.")
        print("Set it as environment variable or create a .env file with LLM_API_KEY=your-key")
        return
    
    # Create JARVIS instance
    jarvis = JARVIS(api_key=api_key)
    
    # Run in text mode for testing (use run_voice_loop for voice)
    await jarvis.run_text_loop()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())