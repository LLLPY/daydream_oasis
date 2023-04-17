from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget



class BlogAdminForm(forms.ModelForm):
    # content=forms.CharField(widget=CKEditorWidget(),label='正文',required=True)
    content=forms.CharField(widget=CKEditorUploadingWidget(),label='正文',required=True)

