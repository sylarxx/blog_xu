<template>
  <div class="tab-bar" @click="tabBarClick">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "TabBar",
  props: {
    path: String,
  },
  methods: {
    tabBarClick() {
      this.$router.push(this.path);
    },
  },
};
</script>

<style scoped>
.tab-bar {
  margin: 20px;
  height: 10rem;
  width: 20rem;
  border-radius: 20px;
  box-shadow: 0 15px 35px 20px rgb(50 50 93 / 10%),
    0 5px 15px 8px rgb(0 0 0 / 7%);
  cursor: pointer;
  transition: all 0.2s;
}

.tab-bar:hover {
  /*盒子向上移动*/
  transform: translateY(-8px);
  box-shadow: 0 15px 35px 20px rgb(50 50 93 / 10%),
    0 5px 15px 8px rgb(0 0 0 / 7%);
}
</style>