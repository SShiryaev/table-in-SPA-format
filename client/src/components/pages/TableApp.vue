<script setup>
  import {inject, onMounted, ref} from 'vue';
  import Container from '@/components/containers/Container.vue';
  import Table from '@/components/view/Table.vue';
  import Filters from '@/components/view/Filters.vue';
  import Loader from '@/components/UI/Loader.vue';
  import NotFound from '@/components/view/NotFound.vue';
  import Pagination from '@/components/view/Pagination.vue';

  defineOptions({
    name: 'TableApp',
  });

  const axios = inject('axios');

  const initialValue = {
    page: 1,
  };

  const isLoading = ref(false);
  const getTableParams = ref(structuredClone(initialValue));
  const tableData = ref(null);
  const paginationRef = ref(null);

  const getTableData = async () => {
    isLoading.value = true;

    try {
      const response = await axios.get('http://127.0.0.1:8000/table', {
        params: getTableParams.value,
      })

      setTimeout(() => {
        tableData.value = response.data;
      }, 500);
    } catch (error) {
      console.error(error);
    } finally {
      setTimeout(() => {
        isLoading.value = false;
      }, 500);
    }
  };

  onMounted( async () => {
    await getTableData();
  });

  const updateFilters = async (filtersValues) => {
    const queryParams = {
      filter_field: filtersValues.type?.value,
      filter_condition: filtersValues.rule?.value,
      filter_value: filtersValues.value,
    };

    getTableParams.value = {
      ...getTableParams.value,
      ...queryParams,
      page: 1,
    };

    paginationRef.value.resetPage();

    await getTableData();
  };

  const clearFilters = async () => {
    getTableParams.value = {
      ordering: getTableParams.value.ordering,
      page: 1,
    };

    paginationRef.value.resetPage();

    await getTableData();
  };

  const onUpdateSort = async (sortValue) => {
    getTableParams.value = {
      ...getTableParams.value,
      ordering: sortValue,
      page: 1,
    };

    paginationRef.value.resetPage();

    await getTableData();
  };

  const onUpdatePagination = async (currentPage) => {
    getTableParams.value.page = currentPage;

    await getTableData();
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

        <Loader v-show="isLoading" />

        <NotFound v-show="!isLoading && !tableData?.results?.length" />

        <Table
          v-show="!isLoading && tableData?.results?.length"
          class="table-app__table"
          :data="tableData?.results"
          @update:sort="onUpdateSort"
        />

        <Pagination
          v-show="!isLoading && tableData?.results?.length"
          ref="paginationRef"
          :table-data="tableData"
          @update:pagination="onUpdatePagination"
        />
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

      &:not(:last-child) {
        margin-bottom: rem(20);
      }
    }
  }
</style>
