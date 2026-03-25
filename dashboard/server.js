const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");


const app = express();
const PORT = 3001;


app.use(cors());

app.get("/api/results",(req, res) => {
    const filepath = path.join(__dirname, "..", "reports", "results.json");
    fs.readFile(filepath, "utf-8", (err, data)=>{
        if(err){
            res.status(500).json({error: "Arquivo não encontrado"})
        }
        else{
            res.json(JSON.parse(data))
        }
    });

});

app.get("/api/health", (req, res) => {
 res.json({ status: "ok"});

});


app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});