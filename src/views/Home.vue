<template>
  <el-container class="container">
    <el-header>
      <el-row :gutter="20">
        <el-col :span="6">
          <individual_logo />
        </el-col>
        <el-col :span="6" :offset="12">
          <nav-bar>
            <nav-bar-item>
              <template v-slot:item-icon>
                <i class="el-icon-s-home"></i>
              </template>
              <template v-slot:item-text>首页</template>
            </nav-bar-item>
            <nav-bar-item>
              <template v-slot:item-icon>
                <i class="el-icon-notebook-1"></i>
              </template>
              <template v-slot:item-text>学习笔记</template>
            </nav-bar-item>
            <nav-bar-item>
              <template v-slot:item-icon>
                <i class="el-icon-question"></i>
              </template>
              <template v-slot:item-text>项目BUGS</template>
            </nav-bar-item>
            <nav-bar-item>
              <template v-slot:item-icon>
                <i class="el-icon-search"></i>
              </template>
              <template v-slot:item-text>搜索</template>
            </nav-bar-item>
          </nav-bar>
        </el-col>
      </el-row>
    </el-header>
  </el-container>
</template>

<script>
import individual_logo from "../components/content/Individual_logo.vue";
import NavBar from "../components/common/navbar/NavBar.vue";
import NavBarItem from "../components/common/navbar/NavBarItem.vue";
export default {
  name: "Home",
  components: {
    individual_logo,
    NavBar,
    NavBarItem,
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
</style>