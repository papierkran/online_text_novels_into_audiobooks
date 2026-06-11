<template>
    <div>
      <div class="main">
          <router-link to="/home" class="home_page">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="25" fill="currentColor" class="bi bi-house-gear" viewBox="0 0 16 16">
                <path d="M7.293 1.5a1 1 0 0 1 1.414 0L11 3.793V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v3.293l2.354 2.353a.5.5 0 0 1-.708.708L8 2.207l-5 5V13.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 1 0 1h-4A1.5 1.5 0 0 1 2 13.5V8.207l-.646.647a.5.5 0 1 1-.708-.708L7.293 1.5Z"/>
                <path fill-rule="evenodd" d="M11.886 9.46c.18-.613 1.048-.613 1.229 0l.043.148a.64.64 0 0 0 .921.382l.136-.074c.561-.306 1.175.308.87.869l-.075.136a.64.64 0 0 0 .382.92l.149.045c.612.18.612 1.048 0 1.229l-.15.043a.64.64 0 0 0-.38.921l.074.136c.305.561-.309 1.175-.87.87l-.136-.075a.64.64 0 0 0-.92.382l-.045.149c-.18.612-1.048.612-1.229 0l-.043-.15a.64.64 0 0 0-.921-.38l-.136.074c-.561.305-1.175-.309-.87-.87l.075-.136a.64.64 0 0 0-.382-.92l-.148-.044c-.613-.181-.613-1.049 0-1.23l.148-.043a.64.64 0 0 0 .382-.921l-.074-.136c-.306-.561.308-1.175.869-.87l.136.075a.64.64 0 0 0 .92-.382l.045-.148ZM14 12.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"/>
            </svg>
            <p>首页</p>
          </router-link>
          <div to="/novel" class="novel" @click="toggleDropdown">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="25" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
            </svg>
            <p>
              小说 <span class="arrow">{{ isDropdownOpen ? "▼" : "▲" }}</span>
            </p>
          </div>
          <div v-if="isDropdownOpen" class="dropdown">
            <router-link to="/internetsearch" class="dropdown_item">联网搜索</router-link>
            <router-link to="/load" class="dropdown_item">本地导入</router-link>
            <router-link to="/novel" class="dropdown_item">小说阅读</router-link>
          </div>
          <router-link to="/bookshelf" class="bookshelf">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="25" fill="currentColor" class="bi bi-book" viewBox="0 0 16 16">
                <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z"/>
            </svg>
            <p>书架</p>
          </router-link>
          <router-link to="/history" class="history">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="25" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
                <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022l-.074.997zm2.004.45a7.003 7.003 0 0 0-.985-.299l.219-.976c.383.086.76.2 1.126.342l-.36.933zm1.37.71a7.01 7.01 0 0 0-.439-.27l.493-.87a8.025 8.025 0 0 1 .979.654l-.615.789a6.996 6.996 0 0 0-.418-.302zm1.834 1.79a6.99 6.99 0 0 0-.653-.796l.724-.69c.27.285.52.59.747.91l-.818.576zm.744 1.352a7.08 7.08 0 0 0-.214-.468l.893-.45a7.976 7.976 0 0 1 .45 1.088l-.95.313a7.023 7.023 0 0 0-.179-.483zm.53 2.507a6.991 6.991 0 0 0-.1-1.025l.985-.17c.067.386.106.778.116 1.17l-1 .025zm-.131 1.538c.033-.17.06-.339.081-.51l.993.123a7.957 7.957 0 0 1-.23 1.155l-.964-.267c.046-.165.086-.332.12-.501zm-.952 2.379c.184-.29.346-.594.486-.908l.914.405c-.16.36-.345.706-.555 1.038l-.845-.535zm-.964 1.205c.122-.122.239-.248.35-.378l.758.653a8.073 8.073 0 0 1-.401.432l-.707-.707z"/>
                <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0v1z"/>
                <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5z"/>
            </svg>
            <p>历史记录</p>
          </router-link>


          <router-link to="/test" class="history">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="25" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
                <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022l-.074.997zm2.004.45a7.003 7.003 0 0 0-.985-.299l.219-.976c.383.086.76.2 1.126.342l-.36.933zm1.37.71a7.01 7.01 0 0 0-.439-.27l.493-.87a8.025 8.025 0 0 1 .979.654l-.615.789a6.996 6.996 0 0 0-.418-.302zm1.834 1.79a6.99 6.99 0 0 0-.653-.796l.724-.69c.27.285.52.59.747.91l-.818.576zm.744 1.352a7.08 7.08 0 0 0-.214-.468l.893-.45a7.976 7.976 0 0 1 .45 1.088l-.95.313a7.023 7.023 0 0 0-.179-.483zm.53 2.507a6.991 6.991 0 0 0-.1-1.025l.985-.17c.067.386.106.778.116 1.17l-1 .025zm-.131 1.538c.033-.17.06-.339.081-.51l.993.123a7.957 7.957 0 0 1-.23 1.155l-.964-.267c.046-.165.086-.332.12-.501zm-.952 2.379c.184-.29.346-.594.486-.908l.914.405c-.16.36-.345.706-.555 1.038l-.845-.535zm-.964 1.205c.122-.122.239-.248.35-.378l.758.653a8.073 8.073 0 0 1-.401.432l-.707-.707z"/>
                <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0v1z"/>
                <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5z"/>
            </svg>
            <p>test</p>
          </router-link>

          <div class="user_info">
            <div class="user_avatar">
              <!-- 头像 -->
              <router-link to="/user" class="user1">U</router-link>
          </div>
            <router-link to="/user" class="username">
              <!-- 用户名 -->
              <p>用户名</p>
            </router-link>
          </div>
        </div>
      </div>
  </template>

<script>

export default {
  data () {
    return {
      isDropdownOpen: false
    }
  },
  methods: {
    toggleDropdown () {
      this.isDropdownOpen = !this.isDropdownOpen
    }
  }
}
</script>

  <style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html,
  body {
    height: 100%;
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
  }
  a {
  text-decoration: none; /* 去除文本下划线 */
  color: inherit; /* 让链接的颜色继承父元素的颜色 */
  cursor: pointer; /* 更改鼠标样式，确保它看起来可以点击 */
}
.main {
  width: 300px;
  height: 100vh; /* 高度为视口高度 */
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  position: relative; /* 使子元素的绝对定位相对于此元素 */
  padding: 10px;
  display: flex;
  flex-direction: column;
  padding: 10px;
  box-sizing: border-box;
}

  .home_page,
  .novel,
  .bookshelf,
  .history {
    width: 100%;
    height: 70px;
    border-bottom: 1px solid #ddd;
    display: flex;
    align-items: center;
    padding-left: 15px;
    transition: background-color 0.3s;
  }

  .novel {
    cursor: pointer;
  }

  .novel:hover,
  .home_page:hover,
  .bookshelf:hover,
  .history:hover {
    background-color: #eaeaea;
  }

  p {
    font-size: 18px;
  color: #333;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: 15px;
  }

  .arrow {
    margin-left: 10px;
    font-size: 20px;
    margin-right: 15px;
  }

  .dropdown {
    width: 100%;
  }

  .dropdown_item {
    width: 100%;
    height: 50px;
    border-top: 1px solid #ddd;
    display: flex;
    align-items: center;
    padding-left: 15px;
    background-color: #f5f5f5;
    transition: background-color 0.3s;
  }

  .dropdown_item:hover {
    background-color: #e5e5e5;
  }

  svg {
    fill: #6c757d;
    margin-right: 10px;
    transition: fill 0.3s;
  }

  .home_page:hover svg,
  .novel:hover svg,
  .bookshelf:hover svg,
  .history:hover svg {
    fill: #007bff;
  }

  .user_info {
  position: absolute; /* 绝对定位 */
  bottom: 10px; /* 距离底部10px */
  left: 10px; /* 距离左侧10px */
  display: flex;
  align-items: center; /* 垂直居中头像和用户名 */
}

.user1 {
  width: 50px;
  height: 50px;
  border-radius: 50%; /* 圆形头像 */
  background-color: #6c757d;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white; /* 字体颜色白色 */
  font-size: 20px; /* 字体大小 */
}

.username {
  margin-left: 10px; /* 左边距 */
}

.username p {
  font-size: 18px;
  color: #333;
}

  </style>
