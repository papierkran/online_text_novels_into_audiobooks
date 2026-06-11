<template>
  <div class="container">
    <h1>本地下载</h1>
    <p>这是本地下载页面。</p>
    
    <!-- 手动输入文本的区域 -->
    <div class="text-area-container">
      <h2>手动输入文本</h2>
      <textarea v-model="text" placeholder="Enter text here..." class="text-area"></textarea>
      <button class="convert-button" @click="convertTextToSpeech">Convert Text to Speech</button>
    </div>

    <!-- 上传文件的区域 -->
    <div class="text-area-container">
      <h2>上传文本文件</h2>
      <input type="file" @change="onFileChange" accept=".txt" />
      <button class="convert-button" @click="convertFileToSpeech">Convert File to Speech</button>
      <div v-if="uploadedText" class="uploaded-text-preview">
        <h3>上传的文本内容:</h3>
        <pre>{{ uploadedText }}</pre> <!-- 显示上传的文本 -->
      </div>
    </div>

    <audio ref="audioPlayer" controls v-if="audioUrl" class="audio-player"></audio>
  </div>
</template>

<script>
export default {
  name: 'Load',
  data() {
    return {
      text: '',               // 手动输入的文本
      uploadedText: '',       // 上传的文本内容
      audioUrl: null,
      file: null              // 存储上传的文件
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.file = file; // 存储文件
        const reader = new FileReader();
        reader.onload = (e) => {
          this.uploadedText = e.target.result; // 读取文件内容到 uploadedText
        };
        reader.readAsText(file);
      }
    },
    async convertTextToSpeech() {
      try {
        const response = await fetch('http://localhost:30600/api/tts_gtts_text', {
          method: 'POST',
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ text: this.text })
        });
        if (response.ok) {
          const blob = await response.blob();
          this.audioUrl = URL.createObjectURL(blob); // 设置音频URL
          this.$refs.audioPlayer.src = this.audioUrl;
        } else {
          const errorData = await response.json();
          alert(`Error: ${errorData.error}`);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async convertFileToSpeech() {
      const formData = new FormData();
      if (this.file) {
        formData.append('file', this.file); // 上传文件
      }

      try {
        const response = await fetch('http://localhost:30600/api/tts_gtts_file', {
          method: 'POST',
          body: formData
        });
        if (response.ok) {
          const blob = await response.blob();
          this.audioUrl = URL.createObjectURL(blob); // 设置音频URL
          this.$refs.audioPlayer.src = this.audioUrl;
        } else {
          const errorData = await response.json();
          alert(`Error: ${errorData.error}`);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
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

h1 {
  text-align: center;
  color: #333;
}

p {
  text-align: center;
  color: #666;
}

.text-area-container {
  margin: 20px 0;
}

.text-area {
  width: 100%;
  height: 150px;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 10px;
  resize: none;
  font-size: 16px;
}

.uploaded-text-preview {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 4px;
  background-color: #e9ecef;
  margin-top: 10px;
}

.convert-button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.convert-button:hover {
  background-color: #0056b3;
}

.audio-player {
  margin-top: 20px;
  width: 100%;
}
</style>
