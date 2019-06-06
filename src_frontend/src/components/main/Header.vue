<template>
  <v-toolbar>
    <v-toolbar-title class="toolbar-title">YouPlayer</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn flat @click.stop="showLoginForm">Login</v-btn>
      <v-btn flat @click.stop="showRegisterForm">Register</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>

  export default {
    methods: {
      showLoginForm() {
        this.$parent.$refs.loginForm.show();
      },
      showRegisterForm() {
        this.$parent.$refs.registerForm.show();
      }
    },
    components: {
      
    }
  }
</script>