<script setup>
  defineOptions({
    name: 'Table',
  });

  defineProps({
    data: Object,
  })
</script>

<template>
  <table class="table">
    <thead class="table__head">
      <tr class="table__head-row">
        <th class="table__head-row-item">Дата</th>
        <th class="table__head-row-item">Название</th>
        <th class="table__head-row-item">Количество</th>
        <th class="table__head-row-item">Расстояние</th>
      </tr>
    </thead>

    <tbody class="table__body">
      <tr
        v-for="tableItem in data"
        :key="tableItem.id"
        class="table__body-row"
      >
        <td class="table__body-row-item">{{ tableItem.date }}</td>
        <td class="table__body-row-item">{{ tableItem.name }}</td>
        <td class="table__body-row-item">{{ tableItem.quantity }}</td>
        <td class="table__body-row-item">{{ tableItem.distance }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style lang="scss" scoped>
  .table {
    &__head {
      &-row {
        &-item {

        }
      }
    }

    & th,
    & td {
      padding: rem(4);

      border: rem(1) solid #000;
    }
  }
</style>
