// src/router/index.jsx
import { createBrowserRouter } from 'react-router-dom';
import MainPage from '../pages/mainpage';
import Home from '../components/home';
import Bookshelf from '../components/bookshelf';


const router = createBrowserRouter([
  {
    path: '/',
    element: <MainPage />, // MainPage 是父组件
    children: [
      {
        path: '/home',
        element: <Home />, // 在 MainPage 的 Outlet 中渲染
      },
      {
        path: '/bookshelf',
        element: <Bookshelf />,
      }

    ],
  },
]);

export default router;
