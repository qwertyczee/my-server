const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

let servers = [];

app.post('/create-server', (req, res) => {
    const serverName = req.body.name;
    const newServer = { name: serverName, id: servers.length + 1 };
    servers.push(newServer);
    res.json({ success: true, server: newServer });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
