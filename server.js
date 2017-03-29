var express     = require('express');
var app         = express();
var http                = require('http').Server(app);
var io                  = require('socket.io')(http);

io.on('connection', function(socket){
    socket.on('chat message', function(msg){
        io.emit('chat message', msg);
    });
});

http.listen(8000, function(){
    console.log('Sockets listen on port 8000');
});
//app.use("/node_modules", express.static(__dirname + '/node_modules'));

/*app.use("/", express.static(__dirname + '/'));

app.listen(1234, function () {
    console.log('Test on port 1234!')
});*/