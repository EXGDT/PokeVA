<template>
  <table />
</template>

<script setup lang="ts">
import { onMounted, watch, ref } from 'vue'
import $ from 'jquery'
import 'bootstrap-table'
import 'bootstrap-table/dist/locale/bootstrap-table-pt-BR'

window.jQuery = window.$ = $

const props = defineProps({
  columns: {
    type: Array,
    required: true
  },
  data: {
    type: [Array, Object],
    default: () => undefined
  },
  options: {
    type: Object,
    default: () => ({})
  }
})

const $table = ref(null)
const _hasInit = ref(false)

const deepCopy = (arg) => {
  if (arg === undefined) {
    return arg
  }
  return $.fn.bootstrapTable.utils.extend(
    true,
    Array.isArray(arg)
      ? []
      : {
          ajaxOptions: {
            beforeSend: (xhr) => {
              xhr.setRequestHeader('Authorization', `Bearer ${useKeycloakStore().keycloak.token}`)
            }
          },
          queryParamsType: '',
          search: true,
          pagination: true,
          locale: 'pt-BR',
          sidePagination: 'server'
        },
    arg
  )
}

const initTable = () => {
  const options = {
    ...deepCopy(props.options),
    columns: deepCopy(props.columns),
    data: deepCopy(props.data)
  }
  if (!_hasInit.value) {
    $($table.value).bootstrapTable(options)
    _hasInit.value = true
  } else {
    refreshOptions(options)
  }
}

const refreshOptions = (options) => {
  $($table.value).bootstrapTable('refreshOptions', options)
}

onMounted(() => {
  $table.value = $(el)

  $($table.value).on('all.bs.table', (e, name, args) => {
    let eventName = $.fn.bootstrapTable.events[name]
    eventName = eventName.replace(/([A-Z])/g, '-$1').toLowerCase()
    emit('on-all', ...args)
    emit(eventName, ...args)
  })

  initTable()
})

watch(() => props.options, initTable, { deep: true })
watch(() => props.columns, initTable, { deep: true })
watch(
  () => props.data,
  () => {
    load(deepCopy(props.data))
  },
  { deep: true }
)

const load = (data) => {
  $($table.value).bootstrapTable('load', data)
}

const methods = (() => {
  const res = {}
  for (const method of $.fn.bootstrapTable.methods) {
    res[method] = function (...args) {
      return $($table.value).bootstrapTable(method, ...args)
    }
  }
  return res
})()

const { emit } = defineEmits([
  'on-all',
  ...Object.keys($.fn.bootstrapTable.events).map((name) =>
    name.replace(/([A-Z])/g, '-$1').toLowerCase()
  )
])
</script>

<style lang="scss">
@import 'bootstrap-table/dist/bootstrap-table.css';
</style>
