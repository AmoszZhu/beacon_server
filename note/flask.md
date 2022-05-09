- 安装Nodehs

    ```sh
    wget https://nodejs.org/dist/v16.10.0/node-v16.10.0-linux-x64.tar.xz
    tar xf node-v16.10.0-linux-x64.tar.xz
    cd node-v16.10.0-linux-x64.tar.xz
    ./bin/node -v
    ln -s /usr/software/nodejs/bin/npm   /usr/local/bin/ 
    ln -s /usr/software/nodejs/bin/node   /usr/local/bin/
    
    node -V # 验证Node版本
    npm -V
    ```

- Swagger-editor

    ```shell
    git clone https://github.com/swagger-api/swagger-editor
    npm install -g http-server
    cd swagger-editor
    http-server -p 8000
    
    # 后台运行
    nohup http-server -p 8000 &
    ```

- Swagger-Ui

    ```shell
    git clone https://github.com/swagger-api/swagger-ui 
    mkdir swagger
    cd swagger
    touch package.json
    npm init package.json
    npm install express --save
    mkdir public
    cp -r ../swagger-ui/dist public/
    vim index.js
    ########################################################
    var express = require('express');
    var http = require('http');
    var app = express();
    app.use('/static', express.static('public'));
    app.listen(8001, function () {
      console.log('app listening on port 8001!');
    });
    ########################################################
    node index.js
    
    #######
    vim swagger-initializer.js
    url: "https://petstore.swagger.io/v2/swagger.json"
    url: "/static/<我们的json文件名>"
    #######
    
    # 后台运行
    npm install forever -g
    forever start index.js
    ```

    