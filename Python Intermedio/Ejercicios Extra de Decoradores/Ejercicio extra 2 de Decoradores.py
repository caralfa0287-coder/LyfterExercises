from functools import wraps


user_logged_in = False

def requires_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global user_logged_in
        if not user_logged_in:
            raise Exception("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


# Intentamos llamar a la función sin estar autenticado
try:
    view_profile()           
except Exception as e:
    print(e)

# Ahora autenticamos al usuario y llamamos a la función nuevamente
user_logged_in = True
view_profile()  
