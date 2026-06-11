<template>
  <div class="container">
    <h1>联网搜索</h1>
    <p>这是联网搜索页面。</p>
    <div class="search-area">
      <input v-model="query" placeholder="输入小说名称" class="search-input" />
      <button class="search-button" @click="searchNovels">搜索</button>
    </div>

    <div v-if="novels.length" class="results-container">
      <h2>搜索结果</h2>
      <ul class="results-list">
        <li v-for="novel in novels" :key="novel.url" class="result-item">
          <h3 class="novel-title">{{ novel.title }}</h3>
          <p class="source">来源: {{ novel.source }}</p>
          <p class="link">链接: <a :href="novel.url" target="_blank">{{ novel.url }}</a></p>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
  text-align: center;
}

p {
  color: #666;
  text-align: center;
}

.search-area {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.search-input {
  width: 60%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  margin-right: 10px;
}

.search-button {
  padding: 10px 15px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #0056b3;
}

.results-container {
  margin-top: 20px;
}

.results-list {
  list-style-type: none;
  padding: 0;
}

.result-item {
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  padding: 15px;
  margin-bottom: 15px;
  transition: box-shadow 0.3s;
}

.result-item:hover {
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
}

.novel-title {
  margin: 0;
  color: #007BFF;
}

.source, .link {
  margin: 5px 0;
  color: #555;
}
</style>

<script>
import axios from 'axios';

export default {
  name: 'InternetSearch',
  data() {
    return {
      query: '',
      novels: []
    };
  },
  methods: {
    async searchNovels() {
      try {
        const response = await axios.get(`http://localhost:30600/api/search_for_novels`, {
          params: { query: this.query }
        });
        this.novels = response.data;
      } catch (error) {
        console.error("搜索失败:", error);
      }
    }
  }
}
</script>