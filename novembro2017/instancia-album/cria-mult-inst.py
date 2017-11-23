# Realizando o deploy de uma aplicacao em multiplas instancias com python shade!
# Utilizando um storage container.
# Importando a biblioteca
import shade
import munch

print ("Iniciando script para inicializar multiplas instancias \n")

# Gerando a conexao com a nuvem
cloud = shade.openstack_cloud(cloud='envvars')

# Criando acesso e credenciamento:
# Inserindo a chave no Openstack para acesso remoto a instancia que sera criada
print('\n Inserindo chave para acesso remoto ')
print('\n Verificando se a chave ja existe... ')

keypair_name = 'minha-chave'
pub_key = open("./minha-chave.pub", 'r').read().strip()

if cloud.search_keypairs(keypair_name):
    print('\n Uma chave com esse nome ja existe, ela sera usada.')
else:
    print('\n Adicionando a chave.')
    cloud.create_keypair(keypair_name, pub_key)

for keypair in cloud.list_keypairs():
    print("\n Nome da chave: " + keypair.name + "\n Chave: " + keypair.public_key)

print "\n Chave adicionada com sucesso"

# Criando grupo para liberar o acesso a instancia
print("\n Criando grupo de acesso")
print('\n Verificando se o grupo ja existe...')

sec_group_name = 'meu-grupo'

if cloud.search_security_groups(sec_group_name):
    print('\n Um grupo com esse nome ja existe, ele sera usado.')
else:
    print('\n Adicionando grupo')
    cloud.create_security_group(sec_group_name, 'Grupo de acesso a rede da minha primeira instancia com Shade')
    cloud.create_security_group_rule(sec_group_name, 80, 80, 'TCP')
    cloud.create_security_group_rule(sec_group_name, 22, 22, 'TCP')

print ("\n grupo criado com sucesso " + cloud.get_security_group(sec_group_name).name)

# Criando parametros das instancias
# Escolhendo e verificando os parametros contidos na nuvem.
image_name = 'ubuntu_x64'
image = cloud.get_image(image_name)
flavor_name = 'pequeno'
flavor = cloud.get_flavor(flavor_name)
rede_name = "interno"
rede = cloud.get_network(rede_name)

print("\n ID da imagem: " + image.id + '\n')
print("\n ID do flavor: " + flavor.id + '\n')
print("\n ID da rede: " + rede.id + '\n')
print("Parametros OK")

# parametros enviados
ex_userdata = open("./cria-pag.sh", 'r').read()
instance_name = 'minha-aplicacao-balanceada'

print ("\n criando instancia")

cloud.create_server(instance_name, image=image_name, flavor=flavor_name, wait=True, auto_ip=False, key_name=keypair_name, security_groups=[sec_group_name], network=rede_name, userdata=ex_userdata, min_count=2, max_count=6)
print ("\n instancia criada com sucesso \n script finalizado.")
