var http = require('http'),
    static = require('node-static');

var file = new(static.Server)('.');
var app = http.createServer(function (request, response) {
    request.addListener('end', function () {
        file.serve(request, response);
    });
}).listen(8080);
console.log("Started ... ");