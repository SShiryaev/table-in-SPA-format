<script setup>
  import {ref} from 'vue';
  import SortButton from '@/components/UI/SortButton.vue';

  defineOptions({
    name: 'Table',
  });

  defineProps({
    data: Object,
  });

  const emit = defineEmits([
    'update:sort'
  ]);

  const sort = ref(null);

  const getSortOrder = (value) => {
    if (!sort.value || sort.value.indexOf(value) === -1) {
      return null;
    }

    return sort.value.indexOf(value) === 0;
  }

  const onUpdateSort = (sortType) => {
    sort.value = sort.value === sortType ? `-${sortType}` : sortType;

    emit('update:sort', sort.value);
  };
</script>

<template>
  <table class="table">
    <thead class="table__head">
      <tr class="table__head-row">
        <th class="table__head-row-item">Дата</th>
        <th class="table__head-row-item">
          <span class="table__head-row-item-content">
             Название

            <SortButton
              sort-type="name"
              :sort-order="getSortOrder('name')"
              @update:sort="onUpdateSort"
            />
          </span>
        </th>

        <th class="table__head-row-item">
          <span class="table__head-row-item-content">
            Количество

            <SortButton
              sort-type="quantity"
              :sort-order="getSortOrder('quantity')"
              @update:sort="onUpdateSort"
            />
          </span>
        </th>

        <th class="table__head-row-item">
          <span class="table__head-row-item-content">
            Расстояние

            <SortButton
              sort-type="distance"
              :sort-order="getSortOrder('distance')"
              @update:sort="onUpdateSort"
            />
          </span>
        </th>
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
      background-color: #f5f5f5;

      &-row {
        &-item {
          &-content {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: rem(8);
          }
        }
      }
    }

    & tr {
      display: flex;

      &:last-child {
        & td {
          border-bottom: rem(1) solid #000;
        }
      }
    }

    & th,
    & td {
      flex: 1 1 0;

      padding: rem(4);

      word-break: break-word;

      border-top: rem(1) solid #000;
      border-left: rem(1) solid #000;

      &:first-child {
        flex: 0 0 rem(150);
      }

      &:last-child {
        border-right: rem(1) solid #000;
      }
    }
  }
</style>
