import React from "react";
import "../css/home.css";

function Home() {
  return (
      <div class="main">
        <div class="box1">
          <p>Ranking of listenters</p>

          <div></div>
          <div class="image-container">
            1<p>斗破苍穹</p>
            <p class="description">已听200个小时</p>
          </div>
          <div></div>

          <div class="image-container">
            2<p>诡秘之主</p>
            <p class="description">已听150个小时</p>
          </div>
          <div></div>

          <div class="image-container">
            3<p>剑来</p>
            <p class="description">已听120个小时</p>
          </div>
          <div  ></div>

          <div class="image-container">
            4<p>吞噬星空</p>
            <p class="description">已听100个小时</p>
          </div>
          <div  ></div>

          <div class="image-container">
            5<p>雪中悍刀行</p>
            <p class="description">已听95个小时</p>
          </div>
          <div  ></div>

          <div class="image-container">
            6<p>大道之上</p>
            <p class="description">已听80个小时</p>
          </div>
          <div  ></div>
        </div>

        <div class="container">
          <div class="box2">
            <h1>小说总字数统计</h1>
            <p v-if="wordCountLoading">正在加载...</p>
            <p v-if="wordCountError" class="error">
              {}
            </p>
            <p v-if="totalWordCount !== null">总字数: {}</p>
          </div>
          <div class="box3">
            <h2>最近阅读的小说</h2>
            <p v-if="historyLoading">加载中...</p>
            <p v-if="historyError" class="error">
              {}
            </p>
            <div v-if="recentHistory">
              <h3>{}</h3>
              <p>{}</p>
              <small>{}</small>
            </div>
          </div>
          <div class="box4">
            <div class="carousel">
              <div class="carousel-images">
                <img
                  v-for="(image, index) in images"
                  alt="轮播图"
                  class="carousel-image"
                />
              </div>
              <button class="carousel-button prev">◀</button>
              <button class="carousel-button next">▶</button>
              <div class="carousel-indicators">
                <span v-for="(image, index) in images"></span>
              </div>
            </div>
          </div>
        </div>
      </div>
  );
}

export default Home;
