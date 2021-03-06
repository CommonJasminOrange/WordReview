from django.db import models
import django.utils.timezone as timezone

import uuid


class Review(models.Model):
    '''复习单词表'''
    word = models.CharField('英文单词', max_length=50, unique=False)
    # mean = models.CharField('中文释义', max_length=500, default='')
    total_num = models.IntegerField('复习总次数', default=0)
    forget_num = models.IntegerField('忘记次数', default=0)
    rate = models.FloatField(
        '单词遗忘率', default=-1, null=False)
    LIST = models.IntegerField('list', default=0)
    UNIT = models.IntegerField('unit', default=0)
    INDEX = models.IntegerField('index', default=0)
    BOOK = models.CharField('单词书', max_length=20, default='')
    history = models.CharField('记忆历史', max_length=100,
                               default='')  # 10100101

    class Meta:
        db_table = 'review'
        ordering = ('LIST', 'UNIT', 'INDEX')


class Books(models.Model):
    '''单词书清单'''
    index_choices = (
        (0, '从0开始'),
        (1, '从1开始'),
    )
    BOOK = models.CharField(
        '单词书', max_length=20, default='UnknowBook', unique=True)
    BOOK_zh = models.CharField(
        '单词书中文', max_length=20, default='未知书本', unique=True)
    BOOK_abbr = models.CharField(
        '单词书简写', max_length=10, default='UNKNOWN BOOK')
    uuid = models.UUIDField(
        'uuid', default=uuid.uuid4, editable=False, unique=True)
    create_time = models.DateTimeField(
        '创建时间', default=timezone.now, editable=False)
    begin_index = models.IntegerField('列表开始是1还是0', default=0)

    class Meta:
        db_table = 'books'
        ordering = ('create_time',)


class BookList(models.Model):
    '''单词书的 List 信息'''
    BOOK = models.CharField('单词书', max_length=20, default='UnknowBook')
    LIST = models.IntegerField('list', default=0)
    last_review_date = models.CharField('上次复习时间', max_length=10, default='')
    review_dates = models.CharField(
        '所有复习日期（仅记录复习曲线时间）', max_length=100, default='')
    list_uuid = models.UUIDField(
        'uuid', default=uuid.uuid4, editable=False, unique=True)
    list_rate = models.FloatField('表记忆率', default=0)
    review_word_counts = models.CharField(
        'list 内单词复习次数（分号分隔）set', max_length=100, default='')
    word_num = models.IntegerField('list 内的单词数目', default=0)
    ebbinghaus_counter = models.IntegerField('艾宾浩斯复习次数', default=0)

    class Meta:
        db_table = 'book_list'
        ordering = ('BOOK', 'LIST', 'last_review_date')


class Words(models.Model):
    '''单纯的单词表'''
    flag_choices = (
        (-1, '太简单'),
        (0, 'default'),
        (1, '重难词'),
    )
    word = models.CharField('英文单词', max_length=50, unique=True)
    mean = models.CharField('中文释义', max_length=500, default='')
    note = models.CharField('记忆法', max_length=200, default='')
    total_num = models.IntegerField('复习总次数', default=0)
    forget_num = models.IntegerField('忘记次数', default=0)
    rate = models.FloatField(
        '单词遗忘率', default=-1, null=False)
    history = models.CharField('记忆历史', max_length=100,
                               default='')  # 10100101
    flag = models.IntegerField('tag', default=0, choices=flag_choices)

    class Meta:
        db_table = 'words'
        ordering = ('word',)
