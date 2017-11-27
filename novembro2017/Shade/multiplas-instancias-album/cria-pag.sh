#!/usr/bin/env bash
echo "nameserver 8.8.8.8" >> /etc/resolv.conf;
sudo apt-get -y install apache2;

echo "<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>My OpenStack Swift Photo Album</title>

    <style type="text/css">
        body {
            padding-top: 70px; /* Required padding for .navbar-fixed-top. Change if height of navigation changes. */
        }
         .img_ft{
                max-width: 200px;
                display: inline-block;
        margin: 20px;
                }
        .thumb {
            margin-bottom: 30px;
        }

        footer {
            margin: 50px 0;
        }
    </style>
</head>
<body>
   <div class=container>
        <div class=row>
         <h1 class=page-header align="center">Meus animais favoritos!<br><br>
            <small>Na minha primeira instância Openstack!</small> </h1>
            <div align="center">
		    <img class="img_ft" src=ip-container/swift/v1/minhas-fotos/cat-dog1 alt=>
                    <img class="img_ft" src=ip-container/swift/v1/minhas-fotos/pig1 alt=>
                    <img class="img_ft" src=ip-container/swift/v1/minhas-fotos/cat1 alt=>
                    <img class="img_ft" src=ip-container/swift/v1/minhas-fotos/pig2 alt=>
                    <img class="img_ft" src=ip-container/swift/v1/minhas-fotos/dog1 alt=>
            </div>
     </div>
        <hr>
    </div>
</body>
</html>" > /var/www/html/index.html;
