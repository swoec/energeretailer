# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-


from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Bill)
admin.site.register(models.Output)
