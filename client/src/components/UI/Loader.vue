<script setup>
  defineOptions({
    name: 'Loader',
  });
</script>

<template>
  <div class="loader">
    <span class="loader__icon"></span>
  </div>
</template>

<style lang="scss" scoped>
  .loader {
    @include position-stretching(fixed, 1);

    display: flex;
    align-items: center;
    justify-content: center;

    backdrop-filter: blur(4px);

    &__icon {
      position: relative;

      display: flex;

      width: rem(48);
      height: rem(48);

      border-radius: 50%;
      animation: rotate 1s linear infinite;

      &::before {
        content: "";
        box-sizing: border-box;
        position: absolute;
        inset: 0;
        border-radius: 50%;
        border: 5px solid orange;
        animation: prixClipFix 2s linear infinite ;
      }
    }
  }

  @keyframes rotate {
    100%   {transform: rotate(360deg)}
  }

  @keyframes prixClipFix {
    0%   {clip-path:polygon(50% 50%,0 0,0 0,0 0,0 0,0 0)}
    25%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 0,100% 0,100% 0)}
    50%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,100% 100%,100% 100%)}
    75%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,0 100%,0 100%)}
    100% {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,0 100%,0 0)}
  }
</style>
