# Generated by Django 2.2.16 on 2020-10-28 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0015_remove_networkgroup_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmembership',
            name='order',
            field=models.IntegerField(blank=True, help_text='Higher numbers mean higher up in the list', null=True),
        ),
        migrations.AlterField(
            model_name='networkgroup',
            name='group_type',
            field=models.IntegerField(choices=[(0, 'Local group'), (1, 'Chapter'), (2, 'Established group'), (3, 'Incubating group'), (4, 'Hibernated group'), (5, 'Affiliate')], default=0),
        ),
        migrations.AlterField(
            model_name='networkgrouplist',
            name='group_type',
            field=models.IntegerField(choices=[(0, 'Local group'), (1, 'Chapter'), (2, 'Established group'), (3, 'Incubating group'), (4, 'Hibernated group'), (5, 'Affiliate')], default=0),
        ),
        migrations.AlterField(
            model_name='networkgroupmembership',
            name='order',
            field=models.IntegerField(blank=True, help_text='The lower the number the higher on the page this Person will be shown.', null=True),
        ),
        migrations.AlterField(
            model_name='nowdoing',
            name='doing_type',
            field=models.CharField(choices=[('reading', 'reading'), ('listening', 'listening'), ('working', 'working'), ('location', 'location'), ('watching', 'watching'), ('eating', 'eating')], max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, upload_to='organisation/people/photos'),
        ),
        migrations.AlterField(
            model_name='project',
            name='old_project',
            field=models.BooleanField(default=False, help_text='Is this an old/archived project?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, help_text='A simple logo or picture to represent this project', upload_to='projects/pictures'),
        ),
        migrations.AlterField(
            model_name='project',
            name='teaser',
            field=models.CharField(help_text='A single line description for list views', max_length=400),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='project_type',
            field=models.ForeignKey(blank=True, help_text='Limit to projects with this type', null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.ProjectType'),
        ),
        migrations.AlterField(
            model_name='projectlist',
            name='theme',
            field=models.ForeignKey(blank=True, help_text='Limit to projects with this theme', null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Theme'),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='title',
            field=models.CharField(default='Get Connected to Open Knowledge', max_length=50),
        ),
        migrations.AlterField(
            model_name='theme',
            name='blurb',
            field=models.TextField(help_text='Blurb for theme page'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='picture',
            field=models.ImageField(blank=True, help_text='A simple logo or picture to represent this theme', upload_to='themes/pictures'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='order',
            field=models.IntegerField(blank=True, help_text='Higher numbers mean higher up in the list', null=True),
        ),
        migrations.AlterField(
            model_name='unitmembership',
            name='order',
            field=models.IntegerField(blank=True, help_text='Higher numbers mean higher up in the list', null=True),
        ),
        migrations.AlterField(
            model_name='workinggroup',
            name='incubation',
            field=models.BooleanField(default=True, help_text='Is this group in incubation?'),
        ),
        migrations.AlterField(
            model_name='workinggroup',
            name='logo',
            field=models.ImageField(blank=True, upload_to='organisation/working-groups/logos'),
        ),
    ]
