from django.db import models
from django.contrib.auth.models import Group, User
#oa
class Usuario():
    def __init__(self,usr,pswd,mail,group_id):
        self.usuario=usr
        self.password=pswd
        self.email=mail
        self.id_grupo=group_id
    def create_user(self):
        try:
            user = User.objects.create_user(self.usuario,self.email,self.password)
        except Exception as e:
            raise f'Error al registrar usuario: {e.__str__}'
        try:
            user.groups.add(self.id_grupo)
        except Exception as e:
            raise f'Error al registrar el grupo del usuario: {e.__str__}'
    def lista_grupos():
        lista=[]
        #Obtenemos la cantidad total de grupos
        size= Group.objects.count()
        #Iteramos segun la cantidad de grupos y añadimos uno por uno los grupos
        for g in range (size):
            lista.append(Group.objects.values_list()[g])
        #Finalmente retornamos la lista
        return lista