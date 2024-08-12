<script setup>
  defineOptions({
    name: 'Container',
  });
</script>

<template>
  <div class="container">
    <slot />
  </div>
</template>

<style lang="scss" scoped>
  .container {
    width: 100%;
    max-width: rem(1060);
    margin: 0 auto;
    padding: 0 rem(30);
  }
</style>
