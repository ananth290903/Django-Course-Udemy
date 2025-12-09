from django import forms


class ReviewForm(forms.Form):
    user_name=forms.CharField(label="Enter the username",max_length=10,error_messages={"max_length":"The username must have <=10 chars","required":"Username is required"})
