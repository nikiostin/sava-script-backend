from django.db import models

class Code(models.Model):
    name = models.CharField(max_length=255)

    code = models.TextField()
    execution_response = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)