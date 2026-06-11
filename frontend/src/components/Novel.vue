<template>
  <div class="container">
    <h1>小说列表</h1>
    <div v-if="!selectedNovel">
      <div class="novel-titles">
        <ul>
          <li v-for="novel in novels" :key="novel.id" @click="fetchNovelContent(novel)">
            {{ novel.title }}
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
  data() {
    return {
      novels: [],         // 存储所有小说信息
      selectedNovel: null, // 当前选中的小说
      novelContent: '',    // 当前选中的小说内容
      userId: 1,          // 示例用户 ID，实际应用中应通过用户登录获取
    };
  },
  methods: {
    async fetchNovels() {
      try {
        const response = await fetch('http://localhost:30600/api/get_all_novels');
        if (response.ok) {
          this.novels = await response.json(); // 获取所有小说
        } else {
          console.error('Error fetching novels');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async fetchNovelContent(novel) {
      try {
        const response = await fetch(`http://localhost:30600/api/get_all_novels/${novel.title}`);
        if (response.ok) {
          const data = await response.json();
          this.novelContent = data.content; // 设置当前小说内容
          this.selectedNovel = { title: novel.title, id: novel.id }; // 设置当前选中的小说信息

          // 保存阅读历史
          await this.saveReadingHistory(this.userId, novel.id, data.content);
        } else {
          console.error('Error fetching novel content');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async saveReadingHistory(userId, novelId, content) {
      try {
        const response = await fetch('http://localhost:30600/api/save_reading_history', {
          method: 'POST',
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ user_id: userId, novel_id: novelId, content })
        });
        if (!response.ok) {
          console.error('Error saving reading history');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    goBack() {
      this.selectedNovel = null;  // 清空选中状态
      this.novelContent = '';      // 清空内容
    },
  },
  mounted() {
    this.fetchNovels(); // 在组件挂载时获取小说列表
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

.novel-titles {
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
  transition: background-color 0.3s;
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
