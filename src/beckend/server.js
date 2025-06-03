// server.js
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());

const MOCK_SERVICES = [
  { id: 1, title: 'Массаж', description: 'Релакс массаж спины', price: 2000, date: '2025-04-01' },
  { id: 2, title: 'Спа', description: 'Спа-процедуры для лица', price: 4500, date: '2025-04-05' }
];

app.get('/api/services', (req, res) => {
  let results = MOCK_SERVICES;

  const { name, minPrice, maxPrice } = req.query;

  if (name) {
    results = results.filter(s => s.title.toLowerCase().includes(name.toLowerCase()));
  }

  if (minPrice) {
    results = results.filter(s => s.price >= parseInt(minPrice));
  }

  if (maxPrice) {
    results = results.filter(s => s.price <= parseInt(maxPrice));
  }

  res.json(results);
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});