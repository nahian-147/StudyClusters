from django.db import models

class PDFName(models.Model):
    pdfName = models.TextField(max_length=500)