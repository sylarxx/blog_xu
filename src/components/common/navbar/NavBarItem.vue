<template>
  <div class="nav-bar-item" @click="itemClick">
    <div :style="activeStyle">
      <slot name="item-icon"></slot>
      <slot name="item-text"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBarItem",
  props: {
    path: String,
  },
  computed: {
    isActive() {
      return this.$route.path.indexOf(this.path) !== -1;
    },
    activeStyle() {
      return this.isActive
        ? {
            backgroundImage:
              "linear-gradient(to right, #434343 0%, black 100%)",
            webkitBackgroundClip: "text",
            webkitTextFillColor: "transparent",
          }
        : {};
    },
  },
  methods: {
    itemClick() {
      this.$router.push(this.path);
    },
  },
};
</script>

<style>
.nav-bar-item {
  margin-left: 36px;
  justify-content: flex-start;
  text-align: center;
  height: 49px;
  font-size: 1.2rem;
  font-weight: 700;
  /*设置字体为渐变色*/
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
  cursor: pointer;
  line-height: 49px;
}
</style>