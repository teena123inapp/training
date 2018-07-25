from django.shortcuts import render
from list.models import TaskModel
# Create your views here.
from datetime import datetime
def create_task(request):
    try:
        if request.method=='POST':
         title=request.data['title']
         description=request.data.get('description',"no description")
         completion_date=datetime.strptime(request.data['completion_data'],"%d/%m%y %H:%M")
         priority=request.data['priority']
         TaskModel.objects.create(title=title,description=description,
                                  completion_date=completion_date,priority=priority)
    except Exception:
        pass
