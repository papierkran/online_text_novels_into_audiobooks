<template>
  <div id="app">
    <HomeView v-if="!isNoSidebarPage" /> <!-- 引入 Sidebar 组件 -->
    <router-view /> <!-- 用于显示路由内容 -->
  </div>
</template>

<script>
import HomeView from './components/HomeView.vue'

export default {
  components: {
    HomeView
  },
  computed: {
    isNoSidebarPage () {
      // 检查当前路由是否为需要隐藏 Sidebar 的页面
      return this.$route.meta.layout === 'no-sidebar'
    }
  }
}
</script>

<style scoped>
#app {
  display: flex; /* 使用 flexbox 布局 */
  height: 100vh; /* 设置高度为视口高度 */
}

.sidebar {
  width: 250px; /* 设置 Sidebar 的宽度 */
}
</style>
