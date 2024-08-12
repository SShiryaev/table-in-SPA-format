<script setup>
  import Container from '@/components/containers/Container.vue';
  import Table from '@/components/view/Table.vue';
  import Filters from '@/components/view/Filters.vue';

  defineOptions({
    name: 'TableApp',
  });
</script>

<template>
  <div class="table-app">
    <Container>
      <div class="table-app__wrapper">
        <h1 class="table-app__title"> Table App</h1>

        <Filters class="table-app__filters" />

        <Table class="table-app__table" />
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
