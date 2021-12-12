from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid
from random import choice


def find_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__icontains=name)
    except Schoolkid.objects.MultipleObjectsReturned:
        print('С такими данными в базе более одного ученика')
    except Schoolkid.objects.ObjectDoesNotExist:
        print('C такими данными учеников нет')


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__range=(2, 3)).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject_title):
    praises = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]

    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_of_study=schoolkid.group_letter,
        subject__title=subject_title
    ).order_by('?').first()

    random_praise = choice(praises)

    if lesson:
        Commendation.object.create(
            text=random_praise,
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
    else:
        return 'Неправильное название предмета'
