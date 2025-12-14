from django import forms

class ReviewForm(forms.Form):
      user_name=forms.CharField(label="Enter your Name",max_length=100,error_messages={
            "required":"The UserName cannot be Empty",
            "max_length":"The username must be short"
        })
      
      review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=50)
      rating=forms.IntegerField(label="Enter your rating",min_value=1,max_value=5)


    