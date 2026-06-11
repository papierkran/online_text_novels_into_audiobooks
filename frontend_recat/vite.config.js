import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 8080, // 自定义端口
    open: true, // 启动后自动打开浏览器
    hmr: true,  // 确保热更新功能启用
  },
});
