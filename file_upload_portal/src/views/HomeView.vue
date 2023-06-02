<template>
  <div class="home">
    <PasswordInput class="password-input"/>
  </div>
</template>

<script>
// @ is an alias to /src
import PasswordInput from '@/components/PasswordInput.vue'

export default {
  name: 'HomeView',
  components: {
    PasswordInput
  }
}
</script>

<style scoped>
.home {
  display:flex;
  flex-direction: column;
}

.password-input {
  padding-top: 10%;
}

</style>
