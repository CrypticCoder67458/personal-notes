<template>
  <v-app>
    <v-layout>
      <VerticalNavbar />
      <v-main>
        <ViewNotes />
      </v-main>
    </v-layout>
    


    
  </v-app>
</template>

<script setup>
  import VerticalNavbar from './components/VerticalNavbar.vue';
  import ViewNotes from './components/ViewNotes.vue';
</script>

