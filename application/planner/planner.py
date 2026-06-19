from domain.models.task import Task


class Planner:
    def create_plan(self, goal: str):
        return [Task(goal=goal)]
