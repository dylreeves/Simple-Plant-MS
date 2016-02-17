from django import forms

from equipment.models import equipment, maintenanceschedule
from .models import maintenancerecord, maintenancerecorddetails
from mainttask.models import MaintenanceJob, MaintenanceTaskDetailItems

class RecordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        pknumber = kwargs.pop('prikey')
        super(RecordForm, self).__init__(*args, **kwargs)
        tasks = MaintenanceTaskDetailItems.objects.filter(maintjob=pknumber).order_by('orderfield')
        Completed = 'OK'
        NotCompleted = 'NO'
        NotApplicable = 'NA'
        completed_choices = (
            (Completed, 'OK'),
            (NotCompleted, 'NO'),
            (NotApplicable, 'NA'),
            )

        itemnumber=1
        for task in tasks:
            self.fields["completed_%d" % itemnumber] = forms.ChoiceField(choices=completed_choices, label=task.task)
            self.fields["comment_%d" % itemnumber] = forms.CharField()
            itemnumber = itemnumber + 1
        ArtisanChoice = (
            (1, "Jan"),
            (2, "Colin"),
            (3, "SomeDude"),
        )
        RunningChoice = (
            (1, "Running"),
            (2, "Stopped"),
        )
        self.fields["artisan"] = forms.ChoiceField(choices=ArtisanChoice)
        self.fields["running"] = forms.ChoiceField(choices=RunningChoice)
        self.fields["generalcomments"] = forms.CharField()

    def printsuccess(self):
        print('happiness')
        pass
