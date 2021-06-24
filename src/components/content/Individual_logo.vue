<template>
  <div class="individual_logo">
    <img src="../../assets/img/individual_logo.jpg" />
    <span>徐逸臣</span>
  </div>
</template>

<script>
export default {
  name: "Individual_logo",
};
</script>

<style scoped>
.individual_logo {
  margin-top: 20px;
}
.individual_logo img {
  height: 50px;
  width: 50px;
  vertical-align: middle;
  border-radius: 50%;
  margin-right: 20px;
}

.individual_logo span {
  font-size: 1.4rem;
  font-weight: 700;
  vertical-align: middle;
  /*设置字体为渐变色*/
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-image: linear-gradient(45deg, #93a5cf 0%, #e4efe9 100%);
}
</style>