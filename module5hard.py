from time import sleep


class Video:

    def __init__(self, title, duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Имя:{self.nickname} Возраст:{self.age} Хэш пароля:{self.password}'


class UrTube:
    users = []
    videos = []
    current_user = ''

    def add(self, *Video):
        self.videos = Video

    def __str__(self):
        var_str_vid = ''
        var_str_user = ''
        for video in self.videos:
            var_str_vid += str(video) + '\n'
        for user in self.users:
            var_str_user += str(user) + '\n'

        return f'Список видео:\n{var_str_vid}\nСписок пользователей:\n{var_str_user}'

    def get_videos(self, find_str):
        var_str = []
        for video in self.videos:
            if str(video).lower().find(str(find_str).lower()) >= 0:
                var_str.append(str(video) + '')
        return f'Результат поиска: {var_str}'

    def watch_video(self, title):
        if self.current_user == '':
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            count = 0
            for video in self.videos:
                if str(video) == str(title):
                    if video.adult_mode:
                        for user in self.users:
                            if self.current_user == user.nickname:
                                if user.age >= 18:
                                    print(self.current_user + ' - смотрит видео "' + str(video) + '"')
                                    for var_str in range(video.duration + 1):
                                        sleep(0.5)
                                        video.time_now += 1
                                        print(' ', end='')
                                        print(var_str, sep="", end="")
                                    video.time_now = 0
                                    print(' Конец видео\n')
                                    return
                                else:
                                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                                    return
                else:
                    count += 1
            if count > 0:
                print('Нет такого видео')

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            self.users.append(User(nickname, password, age))
            self.current_user = nickname
        else:
            for user in self.users:
                if user.nickname == nickname:
                    if user.password == hash(password):
                        self.current_user = nickname
                        user.age = age
                        break
                    else:
                        print('Не верный пароль для ' + str(nickname) + ', этот пользователь уже существует')
                        self.current_user = ''
                        break
                else:
                    self.users.append(User(nickname, password, age))
                    self.current_user = nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(ur)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 55)
print('В системе зарегистрирован пользователь: ' + (ur.current_user))
ur.watch_video('Для чего девушкам парень программист?')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print(ur)
