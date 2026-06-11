<template>
  <div class="main">

    <div class="loginbox">
      <div class="loginbox-in">
        <h2 class="title">欢迎登录</h2> <!-- 登录框标题 -->
        <div class="userbox">
          <input class="user" id="user" v-model="name" placeholder="用户名" />
        </div>
        <div class="pwdbox">
          <input class="pwd" id="password" v-model="pwd" type="password" placeholder="密码" />
        </div>
        <button type="primary" class="register_btn" @click="login">登录</button> <!-- 登录按钮 -->
        <div class="log-box">
          <p class="log-box-text">忘记密码？</p> <!-- 忘记密码提示 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      name: '', // 用户名
      pwd: '' // 密码
    }
  },

  methods: {
    async login() {
      const username = this.name; // 获取用户名
      const password = this.pwd; // 获取密码

      try {
        // 发送POST请求到后端的登录接口
        // const response = await axios.post('http://localhost:30600/api/login', {
        //   username: username,
        //   password: password
        // });

        // // 登录成功后跳转到主页
        // if (response.data.message === '登录成功') {
        //   this.$router.push({ name: 'Home' }); // 跳转到首页
        // } else {
        //   console.log('登录失败:', response.data.error); // 登录失败提示
        // }
        // 登录成功后跳转到主页
        if (username === '123456' && password === '123456') {
          this.$router.push({ name: 'Home' }); // 跳转到首页
        } else {
          console.log('登录失败:', response.data.error); // 登录失败提示
        }
        
      } catch (error) {
        console.log('请求失败:', error); // 请求失败的错误
      }
    }
  }
};
</script>

<style scoped>
.main {
  display: flex; /* 使用 Flexbox 布局 */
  width: 100%;
  height: 100vh; /* 设置高度为视口高度 */
  overflow: hidden; /* 隐藏溢出的内容 */
  background-image: url('../assets/beijing.png');
}

.loginbox {
  position: absolute; /* 绝对定位 */
  width: 450px; /* 登录框宽度 */
  height: auto; /* 高度自适应 */
  top: 50%; /* 垂直居中 */
  left: 50%; /* 水平居中 */
  transform: translate(-50%, -50%); /* 使其真正居中 */
  box-shadow: 0 12px 16px rgba(0, 0, 0, 0.24), 0 17px 50px rgba(0, 0, 0, 0.19); /* 添加阴影效果 */
  background-color: rgba(255, 255, 255, 0.3); /* 背景色 */
  border-radius: 15px; /* 圆角边框 */
  padding: 20px; /* 内边距 */
  box-sizing: border-box; /* 包括内边距和边框在内的总宽度和高度 */
}

.title {
  font-weight: bold; /* 字体加粗 */
  font-size: 24px; /* 字体大小 */
  color: skyblue; /* 字体颜色 */
  text-align: center; /* 文本居中 */
  margin-bottom: 20px; /* 下边距 */
}

.userbox,
.pwdbox {
  margin-bottom: 20px; /* 输入框之间的间距 */
}

input {
  outline: none; /* 去除轮廓样式 */
  border: 1px solid #d1d1d1; /* 边框颜色 */
  border-radius: 5px; /* 圆角边框 */
  height: 40px; /* 输入框高度 */
  font-size: 16px; /* 字体大小 */
  padding: 0 10px; /* 左右内边距 */
  width: 96%; /* 宽度占满 */
  transition: border 0.2s ease-in; /* 边框变化的过渡效果 */
}

input:focus {
  border: 1px solid #5f8276; /* 聚焦时边框颜色 */
}

input::placeholder {
  color: #a9a9a9; /* 占位符颜色 */
  opacity: 1; /* 确保占位符不透明 */
}

.log-box {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: center; /* 水平居中对齐 */
  margin-top: 10px; /* 上边距 */
}

.log-box-text {
  color: skyblue; /* 字体颜色 */
  font-size: 14px; /* 字体大小 */
  text-decoration: underline; /* 下划线 */
  cursor: pointer; /* 鼠标指针为手形 */
}

.register_btn {
  background-color: skyblue; /* 按钮背景色 */
  border: none; /* 去除边框 */
  color: #fafafa; /* 字体颜色 */
  padding: 10px 20px; /* 内边距 */
  text-align: center; /* 文本居中 */
  font-size: 18px; /* 字体大小 */
  border-radius: 5px; /* 圆角边框 */
  width: 100%; /* 宽度占满 */
  transition: background-color 0.2s; /* 背景色变化的过渡效果 */
}

.register_btn:hover {
  background-color: #4a6d5e; /* 悬停时背景色 */
}
</style>
