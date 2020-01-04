from django.db import models
from django.contrib.auth.models import User

class Process(models.Model):
        username =  models.ForeignKey(
                User,
                primary_key=False,
                on_delete=models.CASCADE,
                to_field="username",
                )
        pid = models.IntegerField(primary_key=True)
        current_file = models.IntegerField(default=0)
        total_files = models.IntegerField(default=0)
        errors = models.IntegerField()
        time_started = models.DateTimeField(auto_now_add=True)
        
        #def elapsed_time():
        def increment_progress(self):
                self.current_file += 1
                self.save()
        def get_progress(self):
                print(self.current_file)
                print(self.total_files)
                return "{:.1f}%".format((self.current_file/self.total_files)*100)

