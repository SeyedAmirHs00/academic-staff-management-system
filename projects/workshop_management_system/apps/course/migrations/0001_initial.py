# Generated by Django 5.0.1 on 2024-01-30 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('teacher', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('caption', models.CharField(blank=True, max_length=150, null=True, verbose_name='Caption')),
                ('image', models.ImageField(upload_to='image/course', verbose_name='Image')),
                ('introduction_video', models.FileField(blank=True, null=True, upload_to='video/course', verbose_name='Introduction video')),
                ('level', models.CharField(choices=[('All levels', 'All levels'), ('Beginner', 'Beginner'), ('Preliminary', 'Preliminary'), ('Advanced', 'Advanced')], default='All levels', max_length=50, verbose_name='Level')),
                ('state', models.CharField(choices=[('The course has not started', 'The course has not started'), ('Uploading', 'Uploading'), ('Completion of the course', 'Completion of the course')], default='Start of the course', max_length=50, verbose_name='State')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('number_customer', models.PositiveIntegerField(default=0, verbose_name='Costumer Number')),
                ('number_video', models.PositiveIntegerField(default=0, verbose_name='Number Of Video')),
                ('video_time', models.DurationField(default=0, verbose_name='Video Time')),
                ('course_start_date', models.DateField(verbose_name='Course Start Date')),
                ('is_exam', models.BooleanField(default=False, verbose_name='Is exam')),
                ('is_graduation', models.BooleanField(default=False, verbose_name='Is Graduation')),
                ('registering_open', models.BooleanField(default=True, verbose_name='Registering Open')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('discount', models.FloatField(default=0, verbose_name='Discount')),
                ('start_discount', models.DateTimeField(blank=True, null=True, verbose_name='Start Discount')),
                ('end_discount', models.DateTimeField(blank=True, null=True, verbose_name='End Discount')),
                ('total_points', models.FloatField(default=0, verbose_name='Total Points')),
                ('type', models.CharField(choices=[('Face to face class', 'IN PERSON'), ('Online class', 'ONLINE'), ('Online and Face-to-face classes', 'IN PERSON AND ONLINE')], default='Online class', max_length=50, verbose_name='Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('customer', models.ManyToManyField(blank=True, related_name='course', to='customer.customer', verbose_name='Costumer')),
                ('teacher', models.ManyToManyField(related_name='course', to='teacher.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('discount', models.FloatField(verbose_name='Discount')),
                ('number_discount', models.PositiveIntegerField(verbose_name='Number Of Discount')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('valid_from', models.DateTimeField(verbose_name='Valid Form')),
                ('valid_to', models.DateTimeField(verbose_name='Valid To')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user_costumer', models.ManyToManyField(related_name='coupon_code', to='customer.customer', verbose_name='User Costumer')),
                ('course', models.ManyToManyField(related_name='coupon_code', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Coupon Code',
                'verbose_name_plural': 'Coupon Codes',
            },
        ),
        migrations.CreateModel(
            name='AskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, verbose_name='Question')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='course.askedquestion', verbose_name='Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ask_question_course', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ask_question', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'question and answer',
                'verbose_name_plural': 'question and answer',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='image/category/course', verbose_name='Image')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='course.coursecategory', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='course', to='course.coursecategory', verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='CourseCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('certificate_image', models.FileField(upload_to='document/certificate/course', verbose_name='Certificate Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300, verbose_name='Message')),
                ('score', models.FloatField(default=0, verbose_name='Score')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='course.course', verbose_name='Course')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='course.coursecomment', verbose_name='Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_comment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='CourseDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='course.course', verbose_name='Course')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='course.coursedescription', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Description',
                'verbose_name_plural': 'Descriptions',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='label',
            field=models.ManyToManyField(related_name='course', to='course.courselabel', verbose_name='Label'),
        ),
        migrations.CreateModel(
            name='CourseLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='course.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_course', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('start_exam', models.DateTimeField(verbose_name='Exam Start Date And Time')),
                ('link', models.URLField(verbose_name='Link')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
        ),
        migrations.CreateModel(
            name='ExamScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(verbose_name='Score')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='customer.customer', verbose_name='Costumer')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Score', to='course.exam', verbose_name='Exam')),
            ],
            options={
                'verbose_name': 'Exam Score',
                'verbose_name_plural': 'Exam Scores',
            },
        ),
        migrations.CreateModel(
            name='FAQFrequently',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_frequently', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Frequently Asked Question',
                'verbose_name_plural': 'Frequently Asked Questions',
            },
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='image/festival', verbose_name='Image')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('registering_open', models.BooleanField(default=True, verbose_name='Registering Open')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('course', models.ManyToManyField(related_name='festival', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Festival',
                'verbose_name_plural': 'Festivals',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ManyToManyField(related_name='course', to='course.language', verbose_name='Language'),
        ),
        migrations.CreateModel(
            name='LikesCourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='course.coursecomment', verbose_name='Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_course_comment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'The Like Of The Course Comment',
                'verbose_name_plural': 'The Like Of The Course Comments',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season', to='course.course', verbose_name='Course')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('location_and_time', models.TextField(blank=True, null=True, verbose_name='Location And Time')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/meeting', verbose_name='Video')),
                ('video_time', models.DurationField(default=0, verbose_name='Video Time')),
                ('file', models.FileField(blank=True, null=True, upload_to='file/document', verbose_name='File')),
                ('free', models.BooleanField(default=False, verbose_name='Is Free')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='course.season', verbose_name='Season')),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
                'ordering': ('-created_at',),
            },
        ),
    ]
