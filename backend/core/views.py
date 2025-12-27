from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task, TaskDependency
from .serializers import TaskSerializer
from .utils import check_circular_dependency
from .status import update_task_status
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_status(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = request.data.get('status')
    task.save()

    for dep in task.dependents.all():
        update_task_status(dep.task)

    return Response({"message": "Status updated"})


@api_view(['POST'])
def add_dependency(request, task_id):
    depends_on_id = request.data.get('depends_on_id')

    if task_id == depends_on_id:
        return Response(
            {"error": "Task cannot depend on itself"},
            status=400
        )

    deps = TaskDependency.objects.values_list('task_id', 'depends_on_id')
    cycle = check_circular_dependency(task_id, depends_on_id, deps)

    if cycle:
        return Response(
            {
                "error": "Circular dependency detected",
                "path": cycle
            },
            status=400
        )

    TaskDependency.objects.create(
        task_id=task_id,
        depends_on_id=depends_on_id
    )

    update_task_status(Task.objects.get(id=task_id))

    return Response({"message": "Dependency added"})
