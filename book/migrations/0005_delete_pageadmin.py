# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_pageadmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageAdmin',
        ),
    ]
