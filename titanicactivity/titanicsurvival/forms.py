from django import forms

class TitanicForm(forms.Form):
    Pclass = forms.ChoiceField(
        choices=[(1, "1st Class"), (2, "2nd Class"), (3, "3rd Class")],
        label="Passenger Class"
    )
    Sex = forms.ChoiceField(
        choices=[("male", "Male"), ("female", "Female")]
    )
    Age = forms.FloatField()
    SibSp = forms.IntegerField(label="Number of Siblings/Spouses Aboard")
    Parch = forms.IntegerField(label="Number of Parents/Children Aboard")
    Fare = forms.FloatField(label="Ticket Fare")
    Embarked = forms.ChoiceField(
        choices=[("C", "Cherbourg"), ("Q", "Queenstown"), ("S", "Southampton")],
        label="Port of Embarkation"
    )
    Name = forms.CharField(max_length=100)
    Ticket = forms.CharField(max_length=50)
    Cabin = forms.CharField(max_length=20, required=False) 

