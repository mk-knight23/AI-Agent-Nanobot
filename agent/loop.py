import asyncio
from .memory import MemoryProvider
from .skills import SkillLoader

class NanobotAgent:
    def __init__(self):
        self.memory = MemoryProvider()
        self.skills = SkillLoader()
        self.version = "0.1.3"

    async def main_loop(self):
        """The core 4,000 line lean engine loop."""
        print("Nanobot initializing...")
        while True:
            await self.process_message()
