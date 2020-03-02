from django.db import models
import uuid
from .utils import get_unique_slug
from django.urls import reverse


class NewEntry(models.Model):
    document_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    received_on = models.DateField(auto_now_add=True)
    ENTRY_CLASS = (
        ('Incoming Documents', 'Incoming Documents'),
        ('Outgoing Documents', 'Incoming Documents'),
        ('Documents Within', 'Documents Within')
    )
    entry_class = models.CharField(max_length=30, choices=ENTRY_CLASS)
    slug = models.SlugField(unique=True, null=True, blank=True)
    document_title = models.CharField(max_length=250)
    created_on = models.DateField(auto_now=True)
    DOC_TYPE = (
        ('Forms', 'Forms'),
        ('Memo', 'Memo'),
        ('Reports', 'Reports'),
        ('Letter', 'Letter'),
        ('Envelope', 'Envelope'),
        ('CV', 'CV'),
        ('Proposal', 'Proposal'),
    )
    document_type = models.CharField(verbose_name='Document Type', max_length=20,choices=DOC_TYPE)
    doc_sender = models.CharField(verbose_name='Sender name:Designation', max_length=250)
    sender_thru = models.CharField(verbose_name='Sender name Thru:Designation', max_length=250)
    doc_receiver = models.CharField(verbose_name='Receiver name:Designation', max_length=250)
    doc_source  = models.CharField(verbose_name='Source of Document/Department/Unit', max_length=250)
    doc_destination = models.CharField(verbose_name='Destination of Document/Department/Unit', max_length=250)
    comment = models.TextField()

    def __str__(self):
        return self.document_title
    
    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'document_title', 'slug')
        super().save(*args, **kwargs)      