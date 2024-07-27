class Club():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def orgainze_event(self):
        return f'{self} orgainzes a club'

class Musician():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def play_music(self):
        return f'{self} plays music'


class Dancer():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def dance(self):
        return f'{self} dances'


class Adapter():
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    objects = [Club('Club'), Musician('Musician'), Dancer('Dancer')]

    for obj in objects:
        if hasattr(obj, 'orgainze_club'):
            obj = Adapter(obj, dict(orgainze_event=obj.orgainze_club))
        elif hasattr(obj, 'play_music'):
            obj = Adapter(obj, dict(orgainze_event=obj.play_music))
        elif hasattr(obj, 'dance'):
            obj = Adapter(obj, dict(orgainze_event=obj.dance))
        print(obj.orgainze_event())
