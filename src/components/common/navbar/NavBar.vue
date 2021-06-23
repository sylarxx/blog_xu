<template>
  <div id="nav-bar">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
#nav-bar {
  margin-top: 20px;
  display: flex;
}
</style>