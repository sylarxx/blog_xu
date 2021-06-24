<template>
  <nav-bar>
    <nav-bar-item path="/home">
      <template v-slot:item-icon>
        <i class="el-icon-s-home"></i>
      </template>
      <template v-slot:item-text>首页</template>
    </nav-bar-item>
    <nav-bar-item path="/learningnotes">
      <template v-slot:item-icon>
        <i class="el-icon-notebook-1"></i>
      </template>
      <template v-slot:item-text>学习笔记</template>
    </nav-bar-item>
    <nav-bar-item path="/projectbugs">
      <template v-slot:item-icon>
        <i class="el-icon-question"></i>
      </template>
      <template v-slot:item-text>项目BUGS</template>
    </nav-bar-item>
  </nav-bar>
</template>

<script>
import NavBar from "../../components/common/navbar/NavBar.vue";
import NavBarItem from "../../components/common/navbar/NavBarItem.vue";
export default {
  name: "MainNavBar",
  components: {
      NavBar,
      NavBarItem
  }
};
</script>

<style>
</style>