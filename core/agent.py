"""
ODIN AI Framework
Core Agent
"""

from datetime import datetime

from config.settings import APP_NAME, VERSION
from core.logger import logger


class Agent:
    def __init__(self):
        self.name = APP_NAME
        self.version = VERSION
        self.started_at = datetime.now()

        logger.info(f"{self.name} initialized.")

    def think(self):
        logger.info("Thinking...")

    def execute(self):
        logger.info("Executing task...")

    def remember(self):
        logger.info("Saving memory...")

    def learn(self):
        logger.info("Learning...")

    def run(self):
        print("=" * 50)
        print(f"{self.name} AI Framework")
        print(f"Version : {self.version}")
        print("=" * 50)

        self.think()
        self.execute()
        self.remember()
        self.learn()


if __name__ == "__main__":
    agent = Agent()
    agent.run()