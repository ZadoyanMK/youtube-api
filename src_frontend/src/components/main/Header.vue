<template>
  <v-toolbar>
    <v-toolbar-title class="toolbar-title">YouPlayer</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn flat @click.stop="showLoginForm">Login</v-btn>
      <v-btn flat>Register</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>

  export default {
    methods: {
      showLoginForm() {
        this.$parent.$refs.loginForm.show();
      }
    },
    components: {
      
    }
  }
</script>