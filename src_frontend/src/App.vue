<template>
  <v-app>
    <main-header />
    <v-content>
      
        <router-view />
    </v-content>
    <main-footer />
  </v-app>
</template>

<script>
import Header from '@/components/main/Header';
import Footer from '@/components/main/Footer';

export default {
  name: "app",
  components: {
    'main-header': Header,
    'main-footer': Footer
  }
}
</script>
