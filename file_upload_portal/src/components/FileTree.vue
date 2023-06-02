<template>
    <ol id="file-tree">
      <tree-item class="item" :item="treeData" />
    </ol>
  </template>
  
  <script>
  import treeItem from './TreeItem.vue'


  export default {
    name: 'file-tree',
    data: function() {
      return {
        treeData: this.$store.state.currentFS,
      }
    },
    components: {
      treeItem,
    },
  }
  </script>
  
  <style scoped>
  body {
    font-family: Menlo, Consolas, monospace;
    color: #444;
    font-size: 12px;
  }  
  </style>