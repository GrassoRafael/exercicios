# Importando módulo
from user import Admin

# Programa principal
admin = Admin("rafael", "grasso", privileges=["can ban user", "can delete comments", "can add post"])
admin.privileges.show_privileges()
