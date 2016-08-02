from copy import copy

def serialize_to_show(word):
    return {
        'id': word.id,
        'name': word.word,
        'translation': word.translation,
        'createdDate': word.created_date,
        'updatedDate': word.updated_date,
        'testedDate': word.last_repeat,

        'sound': word.sound,
        'repeats': word.repeats,
        'trained': word.trained,
        'example': word.example,

        # пока неизвестные параметры, для mobile api
        # выводить не нужно, но хранить в бд
        'marked': word.mob_marked,
        'flags': word.mob_flags,
        'retentionMax': word.mob_retention_max,
        'retention': word.mob_retention,
        'incorrect': word.mob_incorrect,

        'keyword': word.mob_keyword,
        'list': word.list,
        'transcription': word.transcription
    }


def swap_translation(words):
    """ запрашивает слова меняя местами translation и word """
    # копируем список
    result = []
    for word in words:
        w = copy(word)
        w.word, w.translation = w.translation, w.word
        result.append(w)
    return result