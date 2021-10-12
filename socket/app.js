const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const cors = require('cors')

const port = process.env.PORT || 4001;
const index = require("./routes/index");

const app = express();

app.use(cors())
app.use(index);

app.get('/products/:id', function (req, res, next) {
    res.json({ msg: 'This is CORS-enabled for all origins!' })
})


const server = http.createServer(app);

const io = socketIo(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"],
        credentials: true
    }
});


// clinet connection
io.on("connection", (socket) => {
    console.log("New client connected");
    // message from 
    socket.on("pi-message", message => {
        console.log(message)
        io.sockets.emit("message", message);
    })

    // webRTC message
    socket.on("rtc-message", message => {
        console.log('get messsage');
        socket.broadcast.emit('rtc-message', message);
    })
    
    // prgress message
    // for image analyze 
    socket.on("progress", message => {
        socket.broadcast.emit('progress', message);
    })

    //LED
    socket.on("light", msg => {
        socket.broadcast.emit("light",msg)
    })
    
    //water
    socket.on("water", msg => {
        socket.broadcast.emit("water",msg)
    })

    //slider
    socket.on("slider", msg => {
        socket.broadcast.emit("slider",msg)
    })

    //fan
    socket.on("fan", msg =>{
        socket.broadcast.emit("fan",msg)
    })
});

server.listen(port, () => console.log(`Listening on port ${port}`));