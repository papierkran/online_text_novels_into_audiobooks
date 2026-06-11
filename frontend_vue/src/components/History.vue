<template>
  <div class="container">
    <h1>阅读历史记录</h1>
    <div v-if="!selectedNovel">
      <div class="history-list">
        <ul>
          <li v-for="history in readingHistories" :key="history.id" @click="fetchNovelContent(history)">
            <div>
              <strong>{{ history.novel_title }}</strong>
              <span> ({{ formatDate(history.read_time) }})</span>
            </div>
            <p>{{ history.read_content }}</p>
          </li>
        </ul>
      </div>
    </div>
    <div v-else>
      <h2>{{ selectedNovel.title }}</h2>
      <p>{{ novelContent }}</p>
      <button @click="goBack">返回</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'History',
  data() {
    return {
      readingHistories: [], // 确保这里初始化为一个空数组
      selectedNovel: null, // 当前选中的小说
      novelContent: '', // 当前选中的小说内容
      userId: 1, // 示例用户 ID，实际应用中应通过用户登录获取
    };
  },
  
  methods: {
    // 获取用户阅读历史记录
    async fetchReadingHistories() {
      const userId = 1; // 根据实际情况动态获取用户ID
      try {
        const response = await fetch(`http://localhost:30600/api/get_reading_history/${userId}`);
        if (response.ok) {
          const data = await response.json(); // 获取用户的阅读历史
          console.log('获取到的阅读历史:', data); // 打印返回的数据，检查格式
          this.readingHistories = data; // 直接将返回的列表赋值给 readingHistories
        } else {
          console.error('Error fetching reading histories');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },

    // 获取小说内容
    async fetchNovelContent(history) {
      try {
        const response = await fetch(`http://localhost:30600/api/get_all_novels/${history.novel_title}`);
        if (response.ok) {
          const data = await response.json();
          this.novelContent = data.content; // 设置当前小说内容
          this.selectedNovel = { title: history.novel_title }; // 设置当前选中的小说信息
        } else {
          console.error('Error fetching novel content');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },

    // 格式化时间
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleString(); // 格式化时间
    },

    // 返回上一页
    goBack() {
      this.selectedNovel = null;  // 清空选中状态
      this.novelContent = '';      // 清空内容
    },
  },

  mounted() {
    this.fetchReadingHistories(); // 在组件挂载时获取用户的阅读历史
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f3f4f8;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

h1, h2 {
  text-align: center;
}

.history-list {
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
  transition: background-color 0.3s;
  cursor: pointer;
}

li:hover {
  background-color: #e9ecef;
}

button {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
