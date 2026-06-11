// src/main.jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { RouterProvider } from 'react-router-dom';
import { Link } from 'react-router-dom';
import router from './router';

import './css/index.css'
import App from './pages/App.jsx'

createRoot(document.getElementById('app')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
