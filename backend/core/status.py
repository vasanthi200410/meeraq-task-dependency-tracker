def update_task_status(task):
    """
    Update task status based on the status of tasks it depends on.
    """

    dependencies = task.dependencies.all()

    # If no dependencies, do nothing
    if not dependencies.exists():
        return

    dep_statuses = [dep.depends_on.status for dep in dependencies]

    # If any dependency is blocked → blocked
    if any(status == "blocked" for status in dep_statuses):
        task.status = "blocked"

    # If all dependencies are completed → in_progress
    elif all(status == "completed" for status in dep_statuses):
        task.status = "in_progress"

    # Otherwise → pending
    else:
        task.status = "pending"

    task.save()
