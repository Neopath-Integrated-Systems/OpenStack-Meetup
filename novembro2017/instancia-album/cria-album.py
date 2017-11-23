import shade

print 'Iniciando script \n'
cloud = shade.openstack_cloud(cloud='envvars')

# Criando container
print 'criando container \n'
container_name = 'minhas-fotos'
container = cloud.create_container(container_name, public=True)

print 'container criado \n'
# Upload das fotos para o storage.
pets = {'cat1': 'fotos/cat1.jpg', 'cat-dog1': 'fotos/cat-dog1.jpg', 'dog1': 'fotos/dog1.jpg', 'pig1': 'fotos/pig1.jpg', 'pig2': 'fotos/pig2.jpg'}

print "lista de imgs criada \n"
print "enviando fotos para o storage"

for object_name, file_path in pets.items():
        cloud.create_object(container=container_name, name=object_name, filename=file_path)

print "objetos adicionados com sucesso!"
