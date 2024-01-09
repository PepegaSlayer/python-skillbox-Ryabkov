def check_permission(required_permission: str):
	user_permissions = ['admin', 'user_1'] 

	def decorator(func):
		def wrapper(*args, **kwargs):
			if required_permission in user_permissions:
				return func(*args, **kwargs)
			else:
				raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")

		return wrapper

	return decorator


@check_permission('admin')
def delete_site():
	print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
	print('Добавляем комментарий')


@check_permission('moderator')
def delete_post():
	print('Удаляем пост')


delete_site()
add_comment()

# пример на исключение
try:
    delete_post()
except PermissionError as e:
    print(e)