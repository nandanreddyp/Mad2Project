<template>
  <router-view/>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
* {
  padding: 0; margin: 0; box-sizing: border-box;
  user-select: none;
}
html, body {
  width: 100%; height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50; background-color: antiquewhite;
  position: fixed; /* check if not scrolling */
  height: 100%; width: 100%;
  display: flex; flex-direction: column;
}
</style>
