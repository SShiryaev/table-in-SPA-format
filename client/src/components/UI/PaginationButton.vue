<script setup>
  import IconArrow from "@/assets/images/icons/arrow.svg";

  defineOptions({
    name: 'PaginationButton',
  });

  defineProps({
    isRightArrow: Boolean,
  });

  const emit = defineEmits([
    'update:pagination'
  ]);

  const onChangePage = () => {
    emit( 'update:pagination');
  }
</script>

<template>
  <button
    class="pagination-button"
    :class="{'next': isRightArrow}"
    @click="onChangePage"
  >
    <IconArrow />
  </button>
</template>

<style lang="scss" scoped>
  .pagination-button {
    display: flex;

    padding: 0;

    border: none;
    background-color: transparent;

    &.next {
      transform: rotate(180deg);
    }
  }
</style>
