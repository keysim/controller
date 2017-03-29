var express     = require('express');
var app         = express();
var http                = require('http').Server(app);
var io                  = require('socket.io')(http);

io.on('connection', function(socket){
    console.log("Connexion !!!!!");
    socket.on('aaa', function(msg){
        io.emit('chat message', msg);
    });
});

http.listen(8000, "0.0.0.0", function(){
    console.log('Sockets listen on port 8000');
});
//app.use("/node_modules", express.static(__dirname + '/node_modules'));

//app.use("/", express.static(__dirname + '/'));
/*app.get("/", function (req, res) {
    res.send('Hello World!');
});

app.listen(4242, "0.0.0.0", function () {
    console.log('Test on port 4242!')
});*/