<template>
  <div class="bookshelf_main">
    <div class="header">
      <h1>书架页面</h1>
    </div>

    <div class="bookshelf-page">
      <!-- 操作按钮 -->
      <div class="action-buttons">
        <button @click="showForm = 'add'">增加</button>
        <button @click="showForm = 'edit'">更新</button>
        <button @click="showForm = 'delete'">删除</button>
        <button @click="showForm = 'view'">查看</button>
      </div>

      <!-- 条件渲染表单，根据不同的操作显示对应的表单 -->
      <form v-if="showForm" @submit.prevent="handleSubmit">
        <div v-if="showForm === 'add' || showForm === 'edit'">
          <label for="title">书名:</label>
          <input type="text" id="title" v-model="form.title" placeholder="请输入书名" />
          
          <label for="url">链接:</label>
          <input type="text" id="url" v-model="form.url" placeholder="请输入链接" />

          <label for="content">内容:</label>
          <textarea id="content" v-model="form.content" placeholder="请输入内容"></textarea>

          <label for="cover_url">封面链接:</label>
          <input type="text" id="cover_url" v-model="form.cover_url" placeholder="请输入封面链接" />
          <label for="file_path">文件:</label>
          <input type="text" id="file_path" v-model="form.file_path" placeholder="文件" />
        </div>
        <button v-if="showForm === 'add'" type="button" @click="addBook">确认增加</button>
        <button v-if="showForm === 'edit'" type="button" @click="editBook">确认更新</button>
        <button v-if="showForm === 'delete'" type="button" @click="deleteBook">确认删除</button>
        <button v-if="showForm === 'view'" type="button" @click="viewBook">确认查看</button>
      </form>

      <!-- 小说列表展示，点击选择小说 -->
      <ul class="novel-list">
        <li v-for="(novel, index) in paginatedNovels" :key="index" class="novel-item" @click="selectNovel(novel)">
          <img v-if="novel.title" :src="novel.cover_url" alt="封面" class="novel-cover" />
          <div v-if="novel.title" class="novel-info">
            <h2>{{ novel.title }}</h2>
            <p>链接: <a :href="novel.url" target="_blank">{{ novel.url }}</a></p>
          </div>
        </li>
      </ul>

      <!-- 分页 -->
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">上一页</button>
        <span>第 {{ currentPage }} 页，共 {{ totalPages }} 页</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">下一页</button>
      </div>
    </div>
  </div>
</template>





<script>
import axios from 'axios';

export default {
  name: 'BookshelfPage',
  data() {
    return {
      form: {
        title: '',
        url: '',
        content: '',
        cover_url: '',
        file_path:''
      },
      novels: [],  // 存储所有小说数据
      currentPage: 1,
      itemsPerPage: 8,
      selectedNovel: null, // 选中的小说对象，用于更新、删除、查看操作
      showForm: null, // 用于控制显示哪个表单
      error: ''
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.novels.length / this.itemsPerPage);
    },
    paginatedNovels() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const novelsForPage = this.novels.slice(start, start + this.itemsPerPage);

      // 如果当前页的书籍数量不足 8 本，用空对象补齐位置
      while (novelsForPage.length < this.itemsPerPage) {
        novelsForPage.push({}); // 空的书籍对象
      }

      return novelsForPage;
    }
  },
  mounted() {
    this.fetchNovels();
  },
  methods: {
    // 获取所有小说数据
    async fetchNovels() {

      try {
        const response = await axios.get('http://localhost:30600/api/get_all_novels');
        this.novels = response.data;
        console.log('获取到的小说数据:', this.novels);
      } catch (error) {
        console.error("获取小说失败:", error);
      }
    },
    
    // 增加小说，不需要传递小说 ID
    async addBook() {
      console.log('发送的表单数据:', this.form)
      try {
        const response = await axios.post('http://localhost:30600/api/add_novel', this.form);
        alert('小说添加成功');
        this.fetchNovels(); // 添加成功后刷新小说列表
        this.resetForm(); // 重置表单
      } catch (error) {
        this.error = error.message;
      }
    },

    // 更新小说，需要传递小说 ID
    async editBook() {
      if (!this.selectedNovel) {
        alert('请先选择要更新的小说');
        return;
      }
      try {
        const response = await axios.put(`http://localhost:30600/api/update_novel/${this.selectedNovel.id}`, this.form);
        alert('小说更新成功');
        this.fetchNovels(); // 更新成功后刷新小说列表
        this.resetForm(); // 重置表单
      } catch (error) {
        this.error = error.message;
      }
    },

    // 删除小说，需要传递小说 ID
    async deleteBook() {
      if (!this.selectedNovel) {
        alert('请先选择要删除的小说');
        return;
      }
      try {
        await axios.delete(`http://localhost:30600/api/delete_novel/${this.selectedNovel.id}`);
        alert('小说删除成功');
        this.fetchNovels(); // 删除成功后刷新小说列表
        this.resetForm(); // 重置表单
      } catch (error) {
        this.error = error.message;
      }
    },

    // 查看单个小说信息
    async viewBook() {
      if (!this.selectedNovel) {
        alert('请先选择要查看的小说');
        return;
      }
      try {
        const response = await axios.get(`http://localhost:30600/api/get_novel/${this.selectedNovel.id}`);
        this.form = response.data; // 将获取到的小说信息填充到表单中
      } catch (error) {
        this.error = error.message;
      }
    },
    
    // 选择小说
    selectNovel(novel) {
      this.selectedNovel = novel;
      this.form = { ...novel }; // 选中小说后，将小说详情填充到表单中
    },

    // 翻页方法
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },

    // 重置表单
    resetForm() {
      this.form = {
        title: '',
        url: '',
        content: '',
        cover_url: '',
        file_path: ''
      };
      this.selectedNovel = null;
      this.showForm = null;
    }
  }
};
</script>



<style scoped>
.bookshelf-page {
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f6f9;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

h1 {
  text-align: center;
  color: #2c3e50;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  margin-bottom: 40px;
}

.novel-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 一排四本书 */
  gap: 20px;
  list-style-type: none;
  padding: 0;
  justify-content: center;
}

.novel-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 15px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  min-height: 250px; /* 设置最小高度，确保空白也占位置 */
}

.novel-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.novel-cover {
  width: 120px;
  height: 180px;
  object-fit: cover;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.novel-info {
  text-align: center;
}

.novel-info h2 {
  margin: 10px 0;
  font-size: 18px;
  color: #34495e;
}

.novel-info a {
  color: #3498db;
  text-decoration: none;
}

.novel-info a:hover {
  text-decoration: underline;
}

/* 分页按钮样式 */
.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.pagination button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 15px;
  margin: 0 10px;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.pagination button:disabled {
  background-color: #95a5a6;
  cursor: not-allowed;
}

.pagination span {
  line-height: 36px;
}

.action-buttons {
  right: 80px; /* 调整位置 */
  top: 10px; /* 调整位置 */
  gap: 10px;
}

.action-buttons button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.action-buttons button:hover {
  background-color: #2980b9;
}

.bookshelf_main{
  width: 80%;
}

</style>
