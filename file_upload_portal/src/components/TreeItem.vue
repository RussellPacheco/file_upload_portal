<template>
    <li>
      <div
        tabindex="0"
        :class="[{ bold: isDirectory }, { item_name: !isDirectory }]"
        @click="toggle"
      >
        <img class="icon" :src="getSrc" />
        {{ item.name }}
        <span v-if="isDirectory">[{{ isOpen ? '-' : '+' }}]</span>
      </div>
      <ol v-if="isDirectory && isOpen" class="list">
        <tree-item
          class="item"
          v-for="(child, index) in item.contents"
          :key="index"
          :item="child"
        ></tree-item>
      </ol>
    </li>
  </template>
  
  <script>
  export default {
    name: 'tree-item',
    props: {
      item: Object,
    },
    data: function() {
      return {
        isOpen: false,
        type: this.item.type,
      }
    },
    computed: {
      isDirectory: function() {
        return this.item.contents && this.item.contents.length
      },
      getSrc: function() {
        if (this.type === 'file') {
          return 'images/file.png'
        } else if (this.type === 'link') {
          return 'images/link.png'
        } else {
          return 'images/folder.png'
        }
      },
    },
    methods: {
      toggle: function() {
        if (this.isDirectory) {
          this.isOpen = !this.isOpen
        }
      },
    },
  }
  </script>
  
  <style scoped>
  .item {
    cursor: pointer;
  }
  .item_name:focus {
    color: rgb(144, 12, 111);
  }
  .item_name {
    color: rgb(19, 131, 146);
  }
  .bold {
    font-weight: bold;
  }
  li::marker {
    font-weight: bold;
  }
  .icon {
    width: 10px;
  }
  </style>