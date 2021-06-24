<template>
  <div class="nav-bar-item" @click="itemClick">
    <slot name="item-icon"></slot>
    <slot name="item-text"></slot>
  </div>
</template>

<script>
export default {
  name: "NavBarItem",
  props: {
    path: String,
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