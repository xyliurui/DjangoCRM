# Generated by Django 2.1.3 on 2018-11-08 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='校区名')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='地址')),
            ],
            options={
                'verbose_name': '校区',
                'verbose_name_plural': '校区',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.SmallIntegerField(choices=[(1, '工作日'), (2, '周末'), (3, '网络班')], verbose_name='班级类型')),
                ('semester', models.SmallIntegerField(verbose_name='学期')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(blank=True, null=True, verbose_name='毕业日期')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Branch', verbose_name='所属校区')),
            ],
            options={
                'verbose_name': '班级信息',
                'verbose_name_plural': '班级信息',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='课程名称')),
                ('price', models.PositiveSmallIntegerField(verbose_name='价格')),
                ('period', models.PositiveSmallIntegerField(default=5, verbose_name='课程周期（月）')),
                ('outline', models.TextField(verbose_name='大纲')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.PositiveSmallIntegerField(verbose_name='课程节次')),
                ('title', models.CharField(max_length=200, verbose_name='本节主题')),
                ('content', models.TextField(verbose_name='本节内容')),
                ('has_homework', models.BooleanField(default=False, verbose_name='本节是否有作业')),
                ('homework', models.TextField(blank=True, null=True, verbose_name='作业内容')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('class_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Class', verbose_name='班级')),
            ],
            options={
                'verbose_name': '上课记录',
                'verbose_name_plural': '上课记录',
            },
        ),
        migrations.CreateModel(
            name='CustomerFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='跟进内容')),
                ('status', models.SmallIntegerField(choices=[(0, '近期无报名计划'), (1, '一个月内报名'), (2, '半个月报名'), (3, '已报名')], verbose_name='客户状态')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '跟进记录',
                'verbose_name_plural': '跟进记录',
            },
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='客户姓名')),
                ('contact_type', models.SmallIntegerField(choices=[(1, 'qq'), (2, '微信'), (3, '手机'), (4, '其他')], default=1, verbose_name='联系媒介')),
                ('contact', models.CharField(max_length=50, unique=True, verbose_name='联系方式')),
                ('source', models.SmallIntegerField(choices=[(1, 'qq群'), (2, '微信'), (3, '转介绍'), (4, '其它')], verbose_name='客户来源')),
                ('consult_content', models.TextField(verbose_name='咨询内容')),
                ('status', models.SmallIntegerField(choices=[(1, '未报名'), (2, '已报名'), (3, '结业')], verbose_name='客户状态')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('consult_courses', models.ManyToManyField(to='crm.Course', verbose_name='咨询课程')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='角色名称')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_grades', models.ManyToManyField(to='crm.Class', verbose_name='班级')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.CustomerInfo', verbose_name='客户')),
            ],
            options={
                'verbose_name': '学员',
                'verbose_name_plural': '学员',
            },
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.SmallIntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (75, 'B-'), (70, 'C+'), (60, 'C'), (40, 'C-'), (-50, 'D'), (0, 'N/A'), (-100, 'COPY')], default=0, verbose_name='得分')),
                ('show_status', models.SmallIntegerField(choices=[(0, '缺勤'), (1, '已签到'), (2, '迟到'), (3, '早退')], default=1, verbose_name='出勤')),
                ('note', models.TextField(blank=True, null=True, verbose_name='成绩备注')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '学习记录',
                'verbose_name_plural': '学习记录',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('role', models.ManyToManyField(blank=True, null=True, related_name='roles', to='crm.Role', verbose_name='角色列表')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='关联系统User')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='consultant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='referral_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.CustomerInfo', verbose_name='转介绍客户'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CustomerInfo', verbose_name='客户'),
        ),
        migrations.AddField(
            model_name='customerfollowup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='跟进人'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together={('class_grade', 'day_num')},
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('branch', 'course', 'class_type', 'semester')},
        ),
    ]
