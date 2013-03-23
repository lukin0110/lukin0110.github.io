Node.js
=======
´´´
sudo apt-get install nodejs
sudo apt-get install npm
sudo npm config set registry http://registry.npmjs.org/
sudo npm install -g node-static
´´´

Make global node modules available
´´´
export NODE_PATH=$NODE_PATH:/usr/local/lib/node_modules
source .bashrc
´´´

Node static: https://github.com/cloudhead/node-static

Spark is a CDN to fit my own needs for Twitter Bootstrap, Bootswatch, Font Awsesome, some popular open-source JavaScript libraries and many more. Spark uses S3 and CloudFront to deliver the shizzle.
