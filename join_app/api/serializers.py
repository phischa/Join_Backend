from rest_framework import serializers
from rest_framework import status

from join_app.models import User, Task, Contact, SubTask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['sub_task_name', 'done']

#class TaskSerializer(serializers.ModelSerializer):
#    subtasks = SubTaskSerializer(many=True, read_only=True)

#    class Meta:
#        model = Task
#        fields = [
#            'title', 'description', 'assignedTo',
#           'dueDate', 'priority', 'category', 'subtasks', 'currentProgress'
#        ]

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True)  # Verschachtelte Subtasks
    assignedTo = serializers.JSONField()  # JSON-Feld für zugewiesene Kontakte

    class Meta:
        model = Task
        fields = [
            'title', 'description', 'assignedTo', 'dueDate',
            'priority', 'category', 'subtasks', 'currentProgress'
        ]

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)

        return task

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = []

