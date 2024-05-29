from django.contrib import admin
from principal.models import LectiveYear, BasicStage, SchoolYear
from principal.forms import LectiveYearForm, BasicStageForm

admin.site.register(LectiveYear)
admin.site.register(BasicStage)
admin.site.register(SchoolYear)
