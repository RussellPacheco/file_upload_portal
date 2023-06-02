<template>
    <div class="password-input">
        <input type="password" v-model="password" @keypress.enter="login"/>
        <div v-if="failedLogin" style="margin: 10px">
            {{ password }}
        </div>
        <!-- <div class="warning" v-if="blankPassword">The password cannot be blank</div>
        <div class="warning" v-else-if="failedLogin">The password was incorrect</div> -->
    </div>
</template>

<script>
export default {
    name: "PasswordInput",
    data() {
        return {
            password: "",
            blankPassword: false,
            failedLogin: false
        }
    },
    methods: {
        login: async function() {
            if (this.password == "") {
                this.blankPassword = true                
            } else {
                this.blankPassword = false
                this.failedLogin = false
                const pass = {
                    "password": this.password
                }
                await this.$store.dispatch("login", pass)
                if (this.$store.state.loginSuccess == true) {
                    this.$store.dispatch("getFS")
                    this.$router.push({name: "navi"})
                } else {
                    this.blankPassword = false
                    this.failedLogin = true
                }
            }
        }
    }


}

</script>

<style scoped>
.warning {
    padding-top: 2%;
    color: red;
}
</style>