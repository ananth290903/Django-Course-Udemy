from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#       user_name=forms.CharField(label="Enter your Name",max_length=100,error_messages={
#             "required":"The UserName cannot be Empty",
#             "max_length":"The username must be short"
#         })
      
#       review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=50)
#       rating=forms.IntegerField(label="Enter your rating",min_value=1,max_value=5)




class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        labels={"user_name":"Your Name","review_text":"Enter Your Review","rating":"Rating of the Page"}
        error_messages={"user_name":{
            "required":"UserName is mandatory !",
            "max_length":"Username must be short"
        }}



    