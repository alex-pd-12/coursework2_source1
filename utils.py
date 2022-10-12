import json
from json import JSONDecodeError


def get_posts_all():
    """Возвращает все посты"""
    try:
        with open("data/posts.json", "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts
    except FileNotFoundError:
        print("Файл posts.json не найден")
    except JSONDecodeError:
        print("Файл posts.json не удаётся преобразовать")


def get_bookmarks():
    """Возвращает закладки  """
    with open('data/bookmarks.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name):
    """ возвращает посты определенного пользователя"""
    user_posts = []
    posts = get_posts_all()
    for post in posts:
        if post["poster_name"] == user_name:
            user_posts.append(post)
    if not user_posts:
        raise ValueError("Такого пользователя не существует")
    return user_posts


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    posts = get_posts_all()
    is_post_real = False
    for post in posts:
        if post["pk"] == post_id:
            is_post_real = True
    if not is_post_real:
        raise ValueError("Такого поста не существует")

    try:
        with open("data/comments.json", "r", encoding="utf-8") as file:
            comments = json.load(file)
    except FileNotFoundError:
        print("Файл comments.json не найден")
    except JSONDecodeError:
        print("Файл comments.json не удаётся преобразовать")

    comments_by_post_id = []
    for comment in comments:
        if comment["post_id"] == post_id:
            comments_by_post_id.append(comment)
    return comments_by_post_id


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query.lower() in post["content"].lower():
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post


def get_all_comments():
    """возвращает все комментарии"""
    with open('data/comments.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def comments_count(post_data, comments_data):
    """считает кол-во лайков"""
    result = []
    for post in post_data:
        for comment in comments_data:
            if comment['post_id'] == post['pk']:
                result.append(post['pk'])
            post['comments'] = result.count(post['pk'])
    return result
