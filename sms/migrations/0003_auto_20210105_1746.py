# Generated by Django 2.2.6 on 2021-01-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_sms_user_ip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sms',
            options={'ordering': ('-datetime',), 'verbose_name': 'پیامک', 'verbose_name_plural': 'پیامک ها'},
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_cost',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_messageid',
            new_name='messageid',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_receptor',
            new_name='receptor',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_sender',
            new_name='sender',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='entries_statustext',
            new_name='statustext',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='entries_datetime',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='return_message',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='return_status',
        ),
    ]
