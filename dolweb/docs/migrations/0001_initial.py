# Generated by Django 2.0.7 on 2018-07-21 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('short_title', models.CharField(max_length=64)),
                ('slug', models.SlugField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('display_order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField()),
                ('display_order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'FAQ category',
                'verbose_name_plural': 'FAQ categories',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('wiki_page', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('listed', models.BooleanField(default=False)),
                ('display_order', models.IntegerField()),
            ],
            options={
                'db_table': 'docs_guide2',
            },
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='docs.FAQCategory'),
        ),
    ]