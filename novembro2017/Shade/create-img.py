import shade
# Initialize and turn on debug logging

shade.simple_logging(debug=True)
# Initialize cloud
# Cloud configs are read with os-client-config
cloud = shade.openstack_cloud(cloud='envvars')
# Upload an image to the cloud
image = cloud.create_image('ubuntu-qcow2', filename='ubuntu.qcow2', wait=True)

print "imagem criada com sucesso!"

