<template>
  <div class="main">
    <div class="box1">
      <p>Ranking of listenters</p>

      <div style="border: 1px solid #e0e0e0;"></div>
      <div class="image-container">
        1
        <p>斗破苍穹</p>
        <img src="../imge/img1.jpg" alt="头像" class="profile-image">
        <p class="description">已听200个小时</p>
      </div>
      <div style="border: 1px solid #e0e0e0;"></div>

      <div class="image-container">
        2
        <p>诡秘之主</p>
        <img src="../imge/img2.jpg" alt="头像" class="profile-image">
        <p class="description">已听150个小时</p>
      </div>
      <div style="border: 1px solid #e0e0e0;"></div>

      <div class="image-container">
        3
        <p>剑来</p>
        <img src="../imge/imge3.jpg" alt="头像" class="profile-image">
        <p class="description">已听120个小时</p>
      </div>
      <div style="border: 1px solid #e0e0e0;"></div>

      <div class="image-container">
        4
        <p>吞噬星空</p>
        <img src="../imge/image4.jpg" alt="头像" class="profile-image">
        <p class="description">已听100个小时</p>
      </div>
      <div style="border: 1px solid #e0e0e0;"></div>

      <div class="image-container">
        5
        <p>雪中悍刀行</p>
        <img src="../imge/image5.jpg" alt="头像" class="profile-image">
        <p class="description">已听95个小时</p>
      </div>
      <div style="border: 1px solid #e0e0e0;"></div>

      <div class="image-container">
        6
        <p>大道之上</p>
        <img src="../imge/image6.jpg" alt="头像" class="profile-image">
        <p class="description">已听80个小时</p>
      </div>
      <div style="border: 1px solid #e0e0e0;"></div>
    </div>

    <div class="container">
      <div class="box2">
        <h1>小说总字数统计</h1>
        <p v-if="wordCountLoading">正在加载...</p>
        <p v-if="wordCountError" class="error">{{ wordCountError }}</p>
        <p v-if="totalWordCount !== null">总字数: {{ totalWordCount }}</p>
      </div>
      <div class="box3" @click="goToHistory">
        <h2>最近阅读的小说</h2>
        <p v-if="historyLoading">加载中...</p>
        <p v-if="historyError" class="error">{{ historyError }}</p>
        <div v-if="recentHistory">
          <h3>{{ recentHistory.novel_title }}</h3>
          <p>{{ recentHistory.read_content }}</p>
          <small>{{ new Date(recentHistory.read_time).toLocaleString() }}</small>
        </div>
      </div>
      <div class="box4">
        <div class="carousel">
          <div class="carousel-images" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
            <img v-for="(image, index) in images" :key="index" :src="image" alt="轮播图" class="carousel-image" />
          </div>
          <button @click="prevImage" class="carousel-button prev">◀</button>
          <button @click="nextImage" class="carousel-button next">▶</button>
          <div class="carousel-indicators">
            <span v-for="(image, index) in images" :key="index" :class="{ active: currentIndex === index }"
              @click="goToImage(index)"></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      totalWordCount: null,
      wordCountLoading: true,
      wordCountError: null,

      recentHistory: null,
      historyLoading: true,
      historyError: null,

      currentIndex: 0,
      images: [
        require('../imge/image4.jpg'),
        require('../imge/image5.jpg'),
        require('../imge/image6.jpg'),
        require('../imge/image7.jpg'),
      ],
      autoSlideInterval: null, // 存储自动轮播的计时器
    };
  },

  methods: {
    async fetchWordCount() {
      try {
        const response = await fetch('http://localhost:30600/api/count_words');
        if (!response.ok) {
          throw new Error('无法获取字数统计');
        }
        const data = await response.json();
        this.totalWordCount = data.total_word_count;
        console.log(this.totalWordCount);
      } catch (err) {
        this.wordCountError = err.message;
      } finally {
        this.wordCountLoading = false;
      }
    },
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.resetAutoSlide(); // 重置计时器，避免冲突
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.resetAutoSlide(); // 重置计时器，避免冲突
    },
    goToImage(index) {
      this.currentIndex = index;
      this.resetAutoSlide(); // 重置计时器，避免冲突
    },
    startAutoSlide() {
      this.autoSlideInterval = setInterval(() => {
        this.nextImage(); // 自动切换到下一张图片
      }, 2500); // 3秒自动切换一次
    },
    resetAutoSlide() {
      if (this.autoSlideInterval) {
        clearInterval(this.autoSlideInterval); // 清除现有计时器
        this.startAutoSlide(); // 重启计时器
      }
    },
    stopAutoSlide() {
      if (this.autoSlideInterval) {
        clearInterval(this.autoSlideInterval); // 停止自动轮播
      }
    },
    async fetchRecentHistory() {
  const userId = 1; // 根据实际情况动态获取用户ID
  try {
    const response = await fetch(`http://localhost:30600/api/get_recent_reading_history/${userId}`); // 调用新的API
    if (!response.ok) {
      throw new Error('无法获取最近的历史记录');
    }

    const recentHistory = await response.json();

    if (recentHistory) {
      this.recentHistory = recentHistory; // 只处理单条记录
    } else {
      this.recentHistory = null;
    }

  } catch (err) {
    this.historyError = err.message;
  } finally {``
    this.historyLoading = false;
  }
},

    goToHistory() {
      this.$router.push({ name: 'History' }); // 确保路由配置中的名称正确
    }
  },
  mounted() {
    this.startAutoSlide(); // 组件挂载后开始自动轮播、
    this.fetchWordCount();
    this.fetchRecentHistory();
  },
  beforeDestroy() {
    this.stopAutoSlide(); // 组件销毁前清除计时器
  },
}
</script>


<style>
.main {
  width: 100%;
  height: 100vh;
  background-color: #f3f4f8;
  display: flex;
}


.container {
  width: 800px;
  height: 500px;

  /* display: flex;  */
  /* flex-direction: row; 垂直方向的排列 */
  margin-left: 10px;
  /* 居中容器 */
}

.box1 {
  width: 400px;
  height: 630px;
  background-color: white;
  margin-left: 50px;
  margin-top: 50px;
  border-radius: 15px;
  /* 圆角效果 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  /* 阴影效果 */
  transition: transform 0.3s, box-shadow 0.3s;
  /* 平滑过渡效果 */
}

.box1 p {
  font-family: Arial, sans-serif;
  /* 设置字体为黑体 */
  font-size: 20px;
  /* 设置字体大小 */
  font-weight: bold;
  /* 设置字体加粗 */
  margin-left: 30px;
  margin-top: 30px;
}

.image-container {
  display: flex;
  /* 使用 Flexbox */
  align-items: center;
  /* 垂直居中对齐 */
  justify-content: flex-start;
  /* 水平分散对齐 */
  margin-top: 20px;
  /* 上边距 */
  margin-left: 30px;
  /* 左边距 */
  padding: 10px 0;
  /* 添加上下内边距 */
  transition: background-color 0.3s, transform 0.2s;
  /* 添加过渡效果 */
  cursor: pointer;
  /* 鼠标悬停时显示为手型 */
}

.image-container:hover {
  background-color: #f0f0f0;
  /* 悬停时背景颜色变化 */
  transform: scale(1.02);
  /* 鼠标悬停时放大 */
}

.image-container p {
  margin: 0;
  /* 去掉默认的段落外边距 */
  margin-left: 10px;
  /* 图片和文本之间的空隙 */
  color: #333;
  /* 文本颜色 */
  transition: color 0.3s;
  /* 添加文字颜色过渡效果 */
}

.image-container:hover p {
  color: #007BFF;
  /* 悬停时文字颜色变化 */
}

.profile-image {
  width: 50px;
  /* 图片宽度 */
  height: 50px;
  /* 图片高度 */
  border-radius: 50%;
  /* 圆形边框 */
  margin-right: 0px;
  /* 图片和文字之间的空隙 */
  margin-left: 10px;
  transition: transform 0.2s;
  /* 添加过渡效果 */
}

.image-container:hover .profile-image {
  transform: rotate(10deg);
  /* 悬停时微微旋转图片 */
}

.description {
  font-family: Arial, sans-serif;
  /* 设置字体 */
  font-size: 16px;
  /* 字体大小 */
}

.box2 {
  width: 300px;
  height: 200px;
  background-color: white;
  margin-left: 30px;
  margin-top: 50px;
  border-radius: 15px;
  /* 圆角效果 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  /* 阴影效果 */
  transition: transform 0.3s, box-shadow 0.3s;
  /* 平滑过渡效果 */
  float: left;
}

.box3 {
  width: 300px;
  height: 200px;
  background-color: white;
  margin-left: 30px;
  margin-top: 50px;
  border-radius: 15px;
  /* 圆角效果 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  /* 阴影效果 */
  transition: transform 0.3s, box-shadow 0.3s;
  /* 平滑过渡效果 */
  float: left;
}

.box4 {
  width: 630px;
  height: 400px;
  background-color: white;
  margin-left: 30px;
  margin-top: 30px;
  border-radius: 15px;
  /* 圆角效果 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  /* 阴影效果 */
  transition: transform 0.3s, box-shadow 0.3s;
  /* 平滑过渡效果 */
  float: left;
}

.box1:hover,
.box2:hover,
.box3:hover,
.box4:hover {
  transform: translateY(-10px);
  /* 提升效果 */
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
  /* 增强阴影效果 */
}

.carousel {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
}

.carousel-images {
  display: flex;
  transition: transform 0.5s ease-in-out;
  /* 使切换更平滑 */
  width: 100%;
  /* 确保容器宽度适配 */
  height: 100%;
  /* 设置高度适应容器 */
}

.carousel-image {
  min-width: 100%;
  /* 图片宽度撑满容器 */
  height: 100%;
  /* 高度适应容器 */
  object-fit: cover;
  /* 图片裁剪为容器大小 */
  border-radius: 10px;
  /* 圆角效果 */
  transition: opacity 0.5s ease-in-out;
  /* 添加淡入淡出效果 */
}


.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.8);
  /* 更加透明的背景 */
  border: none;
  cursor: pointer;
  padding: 10px;
  transition: background-color 0.3s;
  /* 悬停时按钮背景变化 */
}

.carousel-button.prev {
  left: 10px;
}

.carousel-button.next {
  right: 10px;
}

.carousel-indicators {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.carousel-indicators span {
  width: 12px;
  /* 调整大小 */
  height: 12px;
  margin: 0 5px;
  border-radius: 50%;
  background: lightgray;
  cursor: pointer;
  transition: background-color 0.3s;
  /* 悬停时变化 */
}

.carousel-button:hover {
  background-color: rgba(255, 255, 255, 1);
  /* 悬停时背景变为不透明 */
}

.carousel-indicators span.active {
  background: #007BFF;
  /* 更加醒目的颜色 */
}
</style>