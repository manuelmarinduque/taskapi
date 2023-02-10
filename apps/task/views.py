from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import TaskSerializer


# Create your views here.
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(
            user=self.request.user.id, deleted=False, **self.get_filter()
        ).order_by("id")

    def get_filter(self):
        task_filter = {}
        for query_param, value in self.request.query_params.items():
            if hasattr(self.get_serializer().Meta.model, query_param):
                if query_param in ("description", "title"):
                    query_param = f"{query_param}__contains"
                task_filter.update({query_param: value})
        return task_filter

    def create(self, request, *args, **kwargs):
        request.data.update({"user": request.user.id})
        return super().create(request, *args, **kwargs)
