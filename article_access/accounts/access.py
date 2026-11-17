def check_article_access(user):
    if user.has_perm("accounts.change_article"):
        print("Можно редактировать статью")
    else:
        print("Доступ запрещён")