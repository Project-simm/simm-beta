const express = require('express');
const app = express();
const port = 3000;

// Suponha que esta seja a tabela de termos que você quer buscar
const terms = ["apple", "banana", "grape", "orange", "pineapple", "blueberry", "mango"];

app.get('/api/search', (req, res) => {
    const query = req.query.q.toLowerCase();
    const filteredTerms = terms.filter(term => term.toLowerCase().includes(query));
    res.json(filteredTerms);
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
