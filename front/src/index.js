import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './pages/Home/Home.js';
import Header from './components/Header/Header';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Buys from './pages/Buys/Buys.js';
import Add from './pages/AddBuys/index.js';
import Products from './pages/Products/index.js';
import Clients from './pages/Clients/index.js';

//<Route path="*" element={<NoPage />} />
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Header />
    <BrowserRouter>
      <Routes>
        <Route index element={<Home />} />
        <Route path='/compras' element={<Buys />} />
        <Route path='/add' element={<Add />} />
        <Route path='/products' element={<Products />} />
        <Route path='/clients' element={<Clients />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
