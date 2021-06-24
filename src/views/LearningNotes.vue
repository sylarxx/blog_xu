<template>
  <el-container class="container">
    <el-header>
      <el-row :gutter="20">
        <el-col :span="6">
          <individual_logo />
        </el-col>
        <el-col :span="6" :offset="10">
          <main-nav-bar />
        </el-col>
        <el-col :span="2">
          <div class="search">
            <i class="el-icon-search"></i>
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-main> </el-main>
  </el-container>
</template>

<script>
import individual_logo from "../components/content/Individual_logo.vue";
import MainNavBar from "../components/content/MainNavBar.vue";
import { getLearningNotesMultidata } from "../network/learningnotes";
export default {
  name: "LearningNotes",
  components: {
    individual_logo,
    MainNavBar,
  },
  data() {
    return {
      result: null,
    };
  },
  created() {
    // 1.请求多个数据
    getLearningNotesMultidata().then((res) => {
      console.log(res);
      this.result = res;
    });
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
</style>