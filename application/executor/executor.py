from domain.models.task import Task


class Executor:
    def execute(self, task: Task):
        task.status = "completed"
        task.result = f"Executed: {task.goal}"
        return task
