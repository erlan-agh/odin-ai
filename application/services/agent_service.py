from application.workflow.runner import WorkflowRunner


class AgentService:
    def __init__(self):
        self.workflow = WorkflowRunner()

    def run(self):
        self.workflow.run()
