from core.agent import Agent


class WorkflowRunner:
    def __init__(self):
        self.agent = Agent()

    def run(self):
        self.agent.run()
