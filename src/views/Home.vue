<template>
  <el-container class="container">
    <el-header>
      <el-row :gutter="20">
        <el-col :span="6">
          <individual_logo />
        </el-col>
        <el-col :span="2" :offset="16">
          <div class="search">
            <i class="el-icon-search"></i>
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <el-row>
        <div class="blog-title">Xu Yi Chen's BLOG</div>
      </el-row>
      <el-row>
        <tab-bar class="learning-notes" path="/learningnotes">
          <h4>学习笔记</h4>
        </tab-bar>
        <tab-bar class="project-bugs" path="/projectbugs">
          <h4>项目BUGS</h4>
        </tab-bar>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import individual_logo from "../components/content/Individual_logo.vue";
import MainNavBar from "../components/content/MainNavBar.vue";
import TabBar from "../components/common/tabbar/TabBar.vue";
export default {
  name: "Home",
  components: {
    individual_logo,
    MainNavBar,
    TabBar,
  },
};
</script>

<style scoped>
.container {
  background-image: url("../assets/img/bg.jpg");
  background-size: 100% 100%;
  background-position: center center;
  background-repeat: no-repeat;
  min-height: 1000px;
}

.search i {
  margin-top: 20px;
  font-weight: 700;
  font-size: 1.4rem;
  text-align: center;
  height: 49px;
  line-height: 49px;
  /*设置字体为渐变色*/
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
  cursor: pointer;
}

.el-main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.blog-title {
  margin-bottom: 5rem;
  font-size: 4rem;
  font-weight: 700;
  /*设置字体为渐变色*/
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(45deg, #93a5cf 0%, #e4efe9 100%);
}

.learning-notes h4,
.project-bugs h4 {
  font-size: 2.5rem;
  text-align: center;
  /*设置字体为渐变色*/
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(45deg, #93a5cf 0%, #e4efe9 100%);
}
</style>