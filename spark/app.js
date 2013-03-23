/**
 * Simple Node.js server to host this stuff locally without the need of Apache or nginx etc
 */
var http = require('http'),
    static = require('node-static');

// Create a node-static server instance to serve the './frontend' folder
var file = new(static.Server)('.');

var app = http.createServer(function (request, response) {
    request.addListener('end', function () {
        file.serve(request, response);
    });
//}).listen(8080);
}).listen(8080);
console.log("Started ... ");