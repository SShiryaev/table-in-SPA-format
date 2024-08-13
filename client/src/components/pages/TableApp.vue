<script setup>
  import Container from '@/components/containers/Container.vue';
  import Table from '@/components/view/Table.vue';
  import Filters from '@/components/view/Filters.vue';
  import {inject, onMounted, ref} from "vue";

  defineOptions({
    name: 'TableApp',
  });

  const axios = inject('axios');

  const tableData = ref(null);

  const getInititalTableData = async () => {
    const response = await axios.get('http://127.0.0.1:8000/table')
    tableData.value = response.data;
  }

  onMounted( async () => {
    await getInititalTableData();
  });

  const updateFilters = (data) => {
    tableData.value = data;
  }

  const clearFilters = async () => {
    await getInititalTableData();
  }
</script>

<template>
  <div class="table-app">
    <Container>
      <div class="table-app__wrapper">
        <h1 class="table-app__title"> Table App</h1>

        <Filters
          class="table-app__filters"
          @update:filters="updateFilters"
          @clear:filters="clearFilters"
        />

        <Table v-if="tableData?.results?.length" class="table-app__table" :data="tableData?.results" />
      </div>
    </Container>
  </div>
</template>

<style lang="scss" scoped>
  .table-app {
    width: 100%;

    &__wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;

      width: 100%;
    }

    &__title,
    &__filters {
      &:not(:last-child) {
        margin-bottom: rem(20);
      }
    }

    &__title {
      @include text-props(24, 30);
    }

    &__table {
      width: 100%;
    }
  }
</style>
