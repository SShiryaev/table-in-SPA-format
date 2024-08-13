<script setup>
  import IconBarsSort from '@/assets/images/icons/bars-sort.svg';
  import IconDoubleArrow from '@/assets/images/icons/double-arrow.svg';

  defineOptions({
    name: 'SortButton',
  });

  const props = defineProps({
    sortType: String,
    sortOrder: Boolean || null,
  });

  const emit = defineEmits([
    'update:sort'
  ]);

  const onSort = () => {
    emit('update:sort', props.sortType)
  }
</script>

<template>
  <button
    class="sort-button"
    @click="onSort"
  >
    <IconBarsSort
      v-show="sortOrder !== null"
      class="sort-button__bars-sort"
      :class="{direct:  sortOrder}"
    />

    <IconDoubleArrow v-show="sortOrder === null" />
  </button>
</template>

<style lang="scss" scoped>
  .sort-button {
    display: flex;

    padding: 0;

    border: none;
    background-color: transparent;

    &:hover {
      background-color: #ffffff;
    }

    &__bars-sort {
      background-color: #ffffff;

      &.direct {
        transform: rotateX(180deg);
      }
    }
  }
</style>
