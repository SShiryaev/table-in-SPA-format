<script setup>
  import {computed, ref} from 'vue';

  defineOptions({
    name: 'Filters',
  });

  const filtersInititalValue = {
    name: null,
    type: null,
    rule: null,
  };

  const filtersValues = ref(structuredClone(filtersInititalValue));

  const isDisabledClearButton = computed(() => Object.values(filtersValues.value).every((value) => {
    return !value
  }));

  const types = [{
    label: 'Дата',
    value: 'date',
  }, {
    label: 'Название',
    value: 'name',
  }, {
    label: 'Количество',
    value: 'quantity',
  }, {
    label: 'Расстояние',
    value: 'distance',
  }, ];

  const rules = [{
    label: 'Равно',
    value: 'equals',
  }, {
    label: 'Содержит',
    value: 'contains',
  }, {
    label: 'Больше',
    value: 'more',
  }, {
    label: 'Меньше',
    value: 'less',
  }, ];

  const onSubmit = () => {
    console.log('onSubmit')
  };

  const onClear = () => {
    filtersValues.value = structuredClone(filtersInititalValue);
  };
</script>

<template>
  <div class="filters">
    <h2 class="filters__title">
      Фильтры
    </h2>

    <div class="filters__fields">
      <label class="filters__fields-item" for="value-field">
        Правило сортировки

        <input
          id="value-field"
          class="filters__fields-item-filed"
          v-model="filtersValues.name"
          placeholder="Значение фильтра"
        />
      </label>

      <label class="filters__fields-item" for="type-field">
        Правило сортировки

        <select
          id="type-field"
          class="filters__fields-item-filed"
          v-model="filtersValues.type"
          placeholder="Тип фильтра"
        >
          <option disabled value="" selected>Выберите один из вариантов</option>
          <option
            v-for="(type, index) in types"
            :key="index"
            :value="type"
          >
            {{ type.label }}
          </option>
        </select>
      </label>

      <label class="filters__fields-item" for="rule-field">
        Правило сортировки

        <select
          id="rule-field"
          class="filters__fields-item-filed"
          v-model="filtersValues.rule"
        >
          <option value="" disabled>Выберите один из вариантов</option>
          <option
            v-for="(rule, index) in rules"
            :key="index"
            :value="rule"
          >
            {{ rule.label }}
          </option>
        </select>
      </label>
    </div>

    <div class="filters__actions">
      <button @click="onSubmit">
        Применить
      </button>

      <button
        :disabled="isDisabledClearButton"
        @click="onClear"
      >
        Сбросить
      </button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .filters {
    display: flex;
    flex-direction: column;
    align-items: center;

    width: 100%;

    &__title {
      &:not(:last-child) {
        margin-bottom: rem(16);
      }
    }

    &__fields {
      display: flex;
      gap: rem(8);

      width: 100%;

      &:not(:last-child) {
        margin-bottom: rem(16);
      }

      &-item {
        flex: 1 1 0;

        width: auto;
        min-width: auto;

        &-filed {
          width: 100%;
        }
      }
    }

    &__actions {
      display: flex;
      align-self: flex-end;
      gap: rem(8);
    }
  }
</style>
