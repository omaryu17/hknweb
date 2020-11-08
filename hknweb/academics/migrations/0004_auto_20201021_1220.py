# Generated by Django 2.2.8 on 2020-10-21 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_auto_20200723_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='current_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='current_number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='recent_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='academics.Semester'),
        ),
        migrations.AddField(
            model_name='icsr',
            name='course_name',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='current_first_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='current_instructor_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='current_last_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='recent_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='academics.Semester'),
        ),
        migrations.AddField(
            model_name='question',
            name='current_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='recent_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='academics.Semester'),
        ),
        migrations.AlterField(
            model_name='icsr',
            name='icsr_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Course'),
        ),
        migrations.AlterField(
            model_name='icsr',
            name='icsr_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Department'),
        ),
        migrations.AlterField(
            model_name='icsr',
            name='icsr_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Instructor'),
        ),
        migrations.AlterField(
            model_name='icsr',
            name='icsr_semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Semester'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='academicentity_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='academics.AcademicEntity'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='instructor_id',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Question'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.Survey'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_icsr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academics.ICSR'),
        ),
    ]
