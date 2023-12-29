current_users = ['Manolo', 'Jacinto', 'David', 'Chicote', 'Pedro']

new_users = ['antonio', 'juan', 'pedro', 'vicente', 'david', 'chicote']

current_users_low = [user.lower() for user in current_users]#['manolo', 'jacinto', 'david', 'chicote', 'pedro']


for i in new_users:

    if i.lower() in current_users_low:
        print(f'Tienes que introducir otro nombre, {i.title()} esta usado.')

    else:
        print('El nombre usuario esta disponible.')