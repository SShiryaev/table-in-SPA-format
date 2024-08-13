<script setup>
  import {ref} from 'vue';
  import PaginationButton from '@/components/UI/PaginationButton.vue';

  defineOptions({
    name: 'Pagination',
  });

  defineProps({
    tableData: Object,
  });

  const currentPage = ref(1);

  const emit = defineEmits([
    'update:pagination'
  ]);

  const resetPage = () => {
    currentPage.value = 1;
  };

  defineExpose({
    resetPage,
  });

  const onUpdatePagination = (isNext = false) => {
    isNext ? currentPage.value++ : currentPage.value--;

    emit('update:pagination', currentPage.value);
  }
</script>

<template>
  <div class="pagination">
    <PaginationButton
      :disabled="!tableData?.previous"
      @update:pagination="onUpdatePagination()"
    />

    {{ currentPage }}

    <PaginationButton
      :is-right-arrow="true"
      :disabled="!tableData?.next"
      @update:pagination="onUpdatePagination(true)"
    />
  </div>

</template>

<style lang="scss" scoped>
  .pagination {
    display: flex;
    justify-content: space-between;
    gap: rem(8);

    width: 100%;
  }
</style>
