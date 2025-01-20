from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=255, unique=True) 

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    initials = models.CharField(max_length=2, blank=True, null=True)
    color = models.CharField(max_length=25, default="#ACAFC1")

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIO_CHOICES = [
        ('urgent',"urgent"),
        ('medium',"medium"),
        ('low',"low"),
    ]

    CATEGORY_CHOICES = [
        ('technicalTask', "technicalTask"),
        ('userStory', "userStory"),
        ('bug', "bug"),
        ('feature', "feature"),
        ('refactor"', "refactor"),
        ('documentation', "documentation"),
        ('doTestingne', "Testing"),
        ('Analysis', "Analysis"),
        ('Design', "Design"),
        ('No Category', "No Category"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True, null=True)
    assignedTo = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="tasks") #models.CharField(max_length=30, blank=True, null=True) 
    dueDate = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIO_CHOICES, default='low')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='No Category')
    #subtasks = models.JSONField(default=list, blank=True)
    currentProgress = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    sub_task_name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.sub_task_name


#class Task(models.Model):

#    STATUS_CHOICES = [
#       ('todo', 'To Do'),
#        ('inprogress', 'In Progress'),
#        ('awaitfeedback', 'Awaiting Feedback'),
#        ('done', 'Done'),
#    ]
#    PRIO_CHOICES = [
#        ('urgent','urgent' ),
#        ('medium','medium'),
#        ('low',"low"),
#    ]
#
#    title = models.CharField(max_length=30)
#    description = models.CharField(max_length=200, blank=True)
#    users = models.ManyToManyField(User, related_name='tasks') 
#    due_date = models.DateField(("Date"), default=datetime.date.today)
#    priority = models.CharField(max_length=20, choices=PRIO_CHOICES, default='low')
#    category = models.ForeignKey(TaskCategory, related_name='tasks', on_delete=models.CASCADE)
#    board = models.ForeignKey(Board, related_name='tasks', on_delete=models.CASCADE)
#    subtasks = models.JSONField(default=list, blank=True)
#    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

#    def __str__(self):
#        return self.title