<template>
    <v-footer class="pa-3" fixed height="60">
    <v-spacer></v-spacer>
        <div>&copy; {{ new Date().getFullYear() }}</div>
    <v-spacer></v-spacer>
  </v-footer> 
</template>

<script>
    export default {
        name: 'Footer'
    }
</script>