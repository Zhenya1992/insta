import instaloader
import os


def login():
    """Процесс авторизации"""

    load = instaloader.Instaloader(dirname_pattern='data/output_files', download_pictures=False, download_videos=False)

    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    try:
        load.login(username, password)
        print("Вход успешен")
        load.save_session_to_file()
        return load
    except Exception as e:
        print(f'Ошибка {e}. Вход не выполнен')
        return None


def get_followers(load, target_user):
    """Получение подписчиков"""

    print(f"Пользователь найден: {target_user}")

    user = instaloader.Profile.from_username(load.context, target_user)
    print(f'Всего подписчиков: {user.followers}')

    followers = user.get_followers()
    usernames = [follower.username for follower in followers]

    print(f"Всего логинов: {len(usernames)}")
    return usernames


if __name__ == "__main__":
    print("*** Парсер ***")
    load = instaloader.Instaloader(dirname_pattern='data/output_files', download_pictures=False, download_videos=False)

    if os.path.exists("SESSION"):
        print("Сессия сохранена")
        load.load_session_from_file()
    else:
        load = login()
        if not load:
            exit()

    target = input("Введите ник пользователя для сбора пользователей: ")
    usernames = get_followers(load, target)

    with open("data/output_files/followers.txt", 'w', encoding="UTF-8") as f:
        for user in usernames:
            f.write(f'user: {user}\n')

    print("Данные записаны")